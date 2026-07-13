import streamlit as st

# ==========================================================
# INTERVIEW SETUP PAGE
# ==========================================================

def interview_setup():

    # ==========================================================
    # SIDEBAR
    # ==========================================================

    with st.sidebar:

        st.title("🤖 InterviewAI")

        st.divider()

        if st.button(
            "🏠 Dashboard",
            key="sidebar_dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

        st.button(
            "📄 Resume Analyzer",
            key="sidebar_resume",
            disabled=True,
            use_container_width=True
        )

        st.button(
            "📝 Assignment Analyzer",
            key="sidebar_assignment",
            disabled=True,
            use_container_width=True
        )

        st.button(
            "💻 Coding Round",
            key="sidebar_coding",
            disabled=True,
            use_container_width=True
        )

        st.button(
            "📊 Analytics",
            key="sidebar_analytics",
            disabled=True,
            use_container_width=True
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            key="sidebar_logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.page = "hero"

            st.rerun()

    # ==========================================================
    # PAGE HEADER
    # ==========================================================

    st.title("🎤 AI Interview Setup")

    st.caption(
        "Customize your AI interview before starting."
    )

    st.divider()

    left, right = st.columns([2, 1])

    # ==========================================================
    # LEFT COLUMN
    # ==========================================================

    with left:

        company = st.selectbox(
            "🏢 Company",
            [
                "Google",
                "Microsoft",
                "Amazon",
                "Meta",
                "Apple",
                "Netflix",
                "Barclays",
                "JP Morgan",
                "Infosys",
                "TCS",
                "Wipro",
                "General Interview"
            ]
        )

        role = st.selectbox(
            "💼 Role",
            [
                "Software Engineer",
                "Backend Developer",
                "Frontend Developer",
                "Full Stack Developer",
                "Data Analyst",
                "Machine Learning Engineer",
                "HR Interview"
            ]
        )

        difficulty = st.select_slider(
            "⚡ Difficulty",
            options=[
                "Easy",
                "Medium",
                "Hard"
            ],
            value="Medium"
        )

        total_questions = st.slider(
            "❓ Number of Questions",
            min_value=3,
            max_value=10,
            value=5
        )
        topics = st.multiselect(
            "📚 Topics",
            [
                "Python",
                "SQL",
                "DBMS",
                "Operating Systems",
                "Computer Networks",
                "Object Oriented Programming",
                "Data Structures",
                "Algorithms",
                "System Design",
                "Projects",
                "HR"
            ],
            default=[
                "Python",
                "SQL"
            ]
        )

    # ==========================================================
    # RIGHT COLUMN
    # ==========================================================

    with right:

        estimated_time = total_questions * 3

        st.info(f"""
### 📋 Interview Summary

🏢 **Company**

{company}

---

💼 **Role**

{role}

---

⚡ **Difficulty**

{difficulty}

---

❓ **Questions**

{total_questions}

---

⏱ **Estimated Time**

{estimated_time} Minutes
""")

        st.success("""
### 🤖 AI Features

✅ Adaptive Questions

✅ AI Answer Evaluation

✅ Follow-up Questions

✅ Live Technical Score

✅ Final Performance Report

✅ Personalized Feedback
""")

    st.divider()

    # ==========================================================
    # VALIDATION
    # ==========================================================

    if len(topics) == 0:

        st.warning(
            "Please select at least one topic before starting the interview."
        )

        return

    # ==========================================================
    # SELECTED TOPICS
    # ==========================================================

    st.subheader("📚 Selected Topics")

    cols = st.columns(min(len(topics), 4))

    for i, topic in enumerate(topics):

        cols[i % len(cols)].success(topic)

    st.divider()
        # ==========================================================
    # START INTERVIEW
    # ==========================================================

    if st.button(
        "🚀 Start AI Interview",
        key="start_interview",
        type="primary",
        use_container_width=True
    ):

        # Create Interview Session

        st.session_state.interview = {

            "company": company,

            "role": role,

            "difficulty": difficulty,

            "topics": topics,

            "total_questions": total_questions,

            "current_question": 1,

            "current_ai_question": "",

            "conversation": [],

            "technical_scores": [],

            "communication_scores": [],

            "confidence_scores": [],

            "feedback": [],

            "completed": False

        }

        # Navigate to Interview Room

        st.session_state.page = "interview_room"

        st.rerun()
            # ==========================================================
    # NAVIGATION BUTTONS
    # ==========================================================

    st.write("")

    col1, col2 = st.columns(2)

    # --------------------------
    # Back Button
    # --------------------------

    with col1:

        if st.button(
            "⬅ Back to Dashboard",
            key="back_dashboard",
            use_container_width=True
        ):

            st.session_state.page = "dashboard"

            st.rerun()

    # --------------------------
    # Resume Interview
    # --------------------------

    with col2:

        st.button(
            "📄 Resume Interview (Coming Soon)",
            key="resume_interview",
            disabled=True,
            use_container_width=True
        )

    st.divider()

    # ==========================================================
    # INTERVIEW TIPS
    # ==========================================================

    st.subheader("💡 Interview Tips")

    st.info("""
• Read each question carefully before answering.

• Explain your thought process instead of giving only the final answer.

• If you don't know an answer, explain how you would approach solving it.

• Be concise but include important technical details.

• Stay confident—communication is also evaluated.
""")
        # ==========================================================
    # FOOTER
    # ==========================================================

    st.divider()

    st.caption(
        "🤖 Powered by Google Gemini AI • InterviewAI v1.0"
    )

    # ==========================================================
    # DEBUG (REMOVE LATER)
    # ==========================================================

    # Uncomment this while debugging
    #
    # if st.checkbox("Show Interview State"):
    #     st.json(st.session_state.get("interview", {}))

    # ==========================================================
    # END OF FILE
    # ==========================================================

    return
    