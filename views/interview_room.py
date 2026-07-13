import streamlit as st

from core.interview_engine import (
    start_interview,
    evaluate_answer,
    update_interview_state,
    overall_score,
    finish_interview
)

from database.database import save_interview

# ==========================================================
# INTERVIEW ROOM
# ==========================================================

def interview_room():

    # ======================================================
    # CHECK SESSION
    # ======================================================

    if "interview" not in st.session_state:

        st.error("❌ No active interview found.")

        if st.button(
            "⬅ Return to Dashboard",
            key="missing_interview",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

        return

    interview = st.session_state.interview

    # Prevent duplicate saves
    interview.setdefault("saved", False)

    # ======================================================
    # GENERATE FIRST QUESTION
    # ======================================================

    if interview["current_ai_question"] == "":

        with st.spinner("🤖 Gemini is preparing your interview..."):

            result = start_interview(

                company=interview["company"],

                role=interview["role"],

                difficulty=interview["difficulty"],

                topics=interview["topics"]

            )

        if not result["success"]:

            st.error(result["message"])

            if st.button(
                "🔄 Try Again",
                key="retry_first_question"
            ):
                st.rerun()

            return

        interview["current_ai_question"] = result["question"]

        st.session_state.interview = interview

    # ======================================================
    # HEADER
    # ======================================================

    st.title("🎤 AI Interview Room")

    st.caption(
        f"🏢 {interview['company']}   |   "
        f"💼 {interview['role']}   |   "
        f"⚡ {interview['difficulty']}"
    )

    st.divider()

    # ======================================================
    # SAFE PROGRESS BAR
    # ======================================================

    current = interview["current_question"]

    total = interview["total_questions"]

    progress = min(
        max((current - 1) / total, 0.0),
        1.0
    )

    st.progress(progress)

    left, right = st.columns([4, 1])

    with left:

        st.subheader(
            f"Question {current} / {total}"
        )

    with right:

        st.metric(
            "Progress",
            f"{int(progress * 100)}%"
        )

    st.divider()

    # ======================================================
    # AI QUESTION
    # ======================================================

    st.subheader("🤖 AI Interviewer")

    st.info(
        interview["current_ai_question"]
    )

    st.divider()
        # ======================================================
    # CANDIDATE ANSWER
    # ======================================================

    answer = st.text_area(
        "✍ Your Answer",
        value="",
        height=250,
        placeholder="Write your answer here..."
    )

    submit = st.button(
        "🚀 Submit Answer",
        key="submit_answer",
        type="primary",
        use_container_width=True
    )

    # ======================================================
    # SUBMIT ANSWER
    # ======================================================

    if submit:

        if answer.strip() == "":

            st.warning(
                "Please enter your answer before submitting."
            )

        else:

            with st.spinner("🤖 Gemini is evaluating your answer..."):

                result = evaluate_answer(

                    company=interview["company"],

                    role=interview["role"],

                    difficulty=interview["difficulty"],

                    question=interview["current_ai_question"],

                    answer=answer

                )

            # ----------------------------------------------
            # Gemini Error
            # ----------------------------------------------

            if not result["success"]:

                st.error(result["message"])

                st.stop()

            evaluation = result["result"]

            # ----------------------------------------------
            # Save Conversation
            # ----------------------------------------------

            interview["conversation"].append({

                "question": interview["current_ai_question"],

                "answer": answer,

                "feedback": evaluation.get("feedback", "")

            })

            # ----------------------------------------------
            # Store Individual Scores
            # ----------------------------------------------

            interview["technical_scores"].append(

                evaluation.get("technical", 0)

            )

            interview["communication_scores"].append(

                evaluation.get("communication", 0)

            )

            interview["confidence_scores"].append(

                evaluation.get("confidence", 0)

            )

            interview["feedback"].append(

                evaluation.get("feedback", "")

            )
                        # ==================================================
            # GENERATE NEXT QUESTION
            # ==================================================

            if interview["current_question"] < interview["total_questions"]:

                with st.spinner("🤖 Preparing next question..."):

                    next_result = start_interview(

                        company=interview["company"],

                        role=interview["role"],

                        difficulty=interview["difficulty"],

                        topics=interview["topics"]

                    )

                if next_result["success"]:

                    interview["current_ai_question"] = next_result["question"]

                else:

                    st.error(next_result["message"])

                    st.stop()

                # ------------------------------------------
                # Move to Next Question
                # ------------------------------------------

                interview["current_question"] += 1

            else:

                # ------------------------------------------
                # Interview Finished
                # ------------------------------------------

                interview["completed"] = True

                interview["current_question"] = interview["total_questions"]

            # ----------------------------------------------
            # Save Updated Interview
            # ----------------------------------------------

            st.session_state.interview = interview

            st.rerun()

    # ======================================================
    # STOP HERE IF INTERVIEW IS FINISHED
    # ======================================================

    if interview["completed"]:

        st.success("✅ All interview questions completed!")

        st.divider()
            # ======================================================
    # INTERVIEW COMPLETED
    # ======================================================

    if interview["completed"]:

        st.balloons()

        st.header("🎉 Interview Completed")

        # --------------------------------------------------
        # Generate Final Report
        # --------------------------------------------------

        with st.spinner("📄 Generating Final Report..."):

            report = finish_interview(

                interview["conversation"]

            )

        if not report["success"]:

            st.error(report["message"])

            st.stop()

        final_report = report["report"]

        overall = max(
            0,
            min(final_report.get("overall_score", 0), 100)
        )

        # --------------------------------------------------
        # SAVE TO DATABASE (ONLY ONCE)
        # --------------------------------------------------

        if not interview.get("saved", False):

            save_interview(

                username=st.session_state.user[1],

                company=interview["company"],

                role=interview["role"],

                difficulty=interview["difficulty"],

                topics=interview["topics"],

                overall_score=overall,

                technical_score=overall_score(
                    interview["technical_scores"],
                    interview["communication_scores"],
                    interview["confidence_scores"]
                ).get("technical", 0),


                communication_score=overall_score(
                    interview["technical_scores"],
                    interview["communication_scores"],
                    interview["confidence_scores"]
                ).get("communication", 0),

                confidence_score=overall_score(
                    interview["technical_scores"],
                    interview["communication_scores"],
                    interview["confidence_scores"]
                ).get("confidence", 0),

                feedback=final_report.get(
                    "overall_feedback",
                    ""
                ),

                conversation=interview["conversation"]

            )

            interview["saved"] = True

            st.session_state.interview = interview

        # --------------------------------------------------
        # OVERALL SCORE
        # --------------------------------------------------

        st.metric(

            "⭐ Overall Score",

            f"{overall}%"

        )

        st.progress(overall / 100)

        st.divider()

        # --------------------------------------------------
        # STRENGTHS
        # --------------------------------------------------

        st.subheader("💪 Strengths")

        strengths = final_report.get(

            "strengths",

            []

        )

        if isinstance(strengths, list):

            for item in strengths:

                st.success(f"✅ {item}")

        else:

            st.success(strengths)

        # --------------------------------------------------
        # WEAKNESSES
        # --------------------------------------------------

        st.subheader("📉 Areas to Improve")

        weaknesses = final_report.get(

            "weaknesses",

            []

        )

        if isinstance(weaknesses, list):

            for item in weaknesses:

                st.warning(f"⚠ {item}")

        else:

            st.warning(weaknesses)

        # --------------------------------------------------
        # RECOMMENDED TOPICS
        # --------------------------------------------------

        st.subheader("📚 Recommended Topics")

        recommendations = final_report.get(

            "recommended_topics",

            []

        )

        if isinstance(recommendations, list):

            for topic in recommendations:

                st.info(f"📖 {topic}")

        else:

            st.info(recommendations)

        # --------------------------------------------------
        # OVERALL FEEDBACK
        # --------------------------------------------------

        st.subheader("📝 Overall AI Feedback")

        st.write(

            final_report.get(

                "overall_feedback",

                "No feedback generated."

            )

        )

        st.divider()
            # ======================================================
    # ACTION BUTTONS
    # ======================================================

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # Return to Dashboard
    # ------------------------------------------------------

    with col1:

        if st.button(
            "🏠 Return to Dashboard",
            key="return_dashboard",
            use_container_width=True
        ):

            if "interview" in st.session_state:
                del st.session_state["interview"]

            st.session_state.page = "dashboard"

            st.rerun()

    # ------------------------------------------------------
    # Start New Interview
    # ------------------------------------------------------

    with col2:

        if st.button(
            "🔄 Start New Interview",
            key="new_interview",
            use_container_width=True
        ):

            if "interview" in st.session_state:
                del st.session_state["interview"]

            st.session_state.page = "interview"

            st.rerun()

    st.divider()

    # ======================================================
    # SIDEBAR
    # ======================================================

    with st.sidebar:

        st.title("📋 Interview Status")

        st.metric(
            "Question",
            f"{interview['current_question']} / {interview['total_questions']}"
        )

        st.metric(
            "Company",
            interview["company"]
        )

        st.metric(
            "Role",
            interview["role"]
        )

        st.metric(
            "Difficulty",
            interview["difficulty"]
        )

        st.divider()

        st.subheader("📚 Topics")

        for topic in interview["topics"]:

            st.success(topic)

            st.divider()

            st.caption("🤖 AI Interview Coach")

    # ======================================================
    # FOOTER
    # ======================================================

    st.divider()

    st.caption(
        "© 2026 AI Interview Coach • Powered by Google Gemini"
    )
    