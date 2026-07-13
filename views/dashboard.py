import streamlit as st

from database.database import (
    get_total_interviews,
    get_average_score
)

# ==========================================================
# SIDEBAR
# ==========================================================

def sidebar():

    with st.sidebar:

        st.title("🤖 InterviewAI")
        st.caption("Your AI Career Coach")

        st.divider()

        if st.button(
            "🏠 Dashboard",
            key="sidebar_dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

        if st.button(
            "🎤 AI Interview",
            key="sidebar_interview",
            use_container_width=True
        ):
            st.session_state.page = "interview"
            st.rerun()

        if st.button(
            "📄 Resume Analyzer",
             use_container_width=True
        ):
            st.session_state.page = "resume"
            st.rerun()

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

        st.button(
            "📑 Reports",
            key="sidebar_reports",
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
# DASHBOARD
# ==========================================================

def show_dashboard(user):

    sidebar()

    user_id = user[0]
    name = user[1]

    total = get_total_interviews(user_id)
    average = get_average_score(user_id)

    st.title(f"👋 Welcome, {name}")

    st.caption("Practice interviews, improve your skills, and track your progress.")

    st.divider()
    if st.button(
            "📋 Interview History",
            use_container_width=True
        ):
            st.session_state.page = "history"
            st.rerun()

    # ======================================================
    # FIRST-TIME USER
    # ======================================================

    if total == 0:

        st.info("""
# 🚀 Welcome to InterviewAI

Looks like this is your first interview.

Complete your first interview to unlock:

- 📊 Analytics
- 📄 AI Reports
- 🏆 Career Readiness
- 🎯 Personalized Feedback
""")

        st.write("")

        col1, col2, col3 = st.columns(3)

        # ---------------- AI Interview ---------------- #

        with col1:

            st.markdown("""
            <div class="card">
                <h2>🎤 AI Interview</h2>
                <p>Practice realistic technical and HR interviews powered by Gemini AI.
                </p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(
                "🚀 Start Interview",
                key="first_start_interview",
                use_container_width=True
            ):
                st.session_state.page = "interview"
                st.rerun()

        # ---------------- Resume Analyzer ---------------- #

        with col2:

            st.markdown("""
<div class="card">
<h2>📄 Resume Analyzer</h2>
<p>
Analyze your resume, receive ATS score and AI suggestions.
</p>
</div>
""", unsafe_allow_html=True)

            if st.button(
                "📄 Resume Analyzer",
            key="first_resume_btn",
            use_container_width=True
            ):
                 st.session_state.page = "resume"
                 st.rerun()

        # ---------------- Coding Round ---------------- #

        with col3:

            st.markdown("""
<div class="card">
<h2>💻 Coding Round</h2>
<p>
Solve coding questions and receive AI feedback.
</p>
</div>
""", unsafe_allow_html=True)

            st.button(
                "Coding Round (Coming Soon)",
                key="first_coding_btn",
                disabled=True,
                use_container_width=True
            )

        st.divider()

        st.subheader("🔥 Today's Challenge")

        st.success("""
### SQL Challenge

Explain the difference between:

• INNER JOIN

• LEFT JOIN

• RIGHT JOIN

Estimated Time: **15 Minutes**
""")

        st.divider()

        st.subheader("🔒 Unlock After Your First Interview")

        c1, c2 = st.columns(2)

        with c1:

            st.warning("📊 Analytics Dashboard")
            st.warning("🏆 Career Readiness Score")

        with c2:

            st.warning("📄 AI Reports")
            st.warning("🧠 Personalized Study Plan")

        return

    # ======================================================
    # RETURNING USER
    # ======================================================

    st.subheader("📊 Your Performance")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Interviews", total)

    with m2:
        st.metric("Average Score", f"{average}%")

    with m3:

        readiness = min(
            100,
            int((average * 0.7) + total * 2)
        )

        st.metric(
            "Career Readiness",
            f"{readiness}%"
        )

    st.divider()

    # ======================================================
    # QUICK ACTIONS
    # ======================================================

    st.subheader("🚀 Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
<div class="card">
<h3>🎤 AI Interview</h3>
<p>Start a new AI interview.</p>
</div>
""", unsafe_allow_html=True)

        if st.button(
            "Start New Interview",
            key="return_start_interview",
            use_container_width=True
        ):
            st.session_state.page = "interview"
            st.rerun()

    with col2:

        st.markdown("""
<div class="card">
<h3>📄 Resume Analyzer</h3>
<p>AI-powered ATS and resume review.</p>
</div>
""", unsafe_allow_html=True)

        if st.button(
            "📄 Resume Analyzer",
            key="return_resume_btn",
            use_container_width=True
        ):
            st.session_state.page = "resume"
            st.rerun()

    with col3:

        st.markdown("""
<div class="card">
<h3>💻 Coding Round</h3>
<p>Practice coding interview questions.</p>
</div>
""", unsafe_allow_html=True)

    st.divider()

    # ======================================================
    # PROGRESS
    # ======================================================

    st.subheader("📈 Progress")

    st.progress(readiness / 100)

    st.write(
        f"Current Interview Readiness: **{readiness}%**"
    )

    st.divider()

    # ======================================================
    # RECENT ACTIVITY
    # ======================================================

    st.subheader("📅 Recent Activity")

    st.info(
        "Your completed interviews will appear here."
    )

    st.divider()

    # ======================================================
    # AI RECOMMENDATION
    # ======================================================

    st.subheader("🤖 AI Recommendation")

    if average < 60:

        st.warning(
            "Focus on Python, SQL, DBMS and Operating Systems before attempting harder interviews."
        )

    elif average < 80:

        st.info(
            "Good progress! Try company-specific interview practice to improve further."
        )

    else:

        st.success(
            "Excellent work! You're ready for advanced interview simulations."
        )

    st.divider()

    st.caption(
        "InterviewAI • Powered by Streamlit + Gemini AI"
    )