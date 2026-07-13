import streamlit as st
from pathlib import Path

# ==========================================================
# AUTHENTICATION
# ==========================================================

from auth import create_user, login_user

# ==========================================================
# PAGES
# ==========================================================

from views.dashboard import show_dashboard
from views.interview import interview_setup
from views.interview_room import interview_room
from views.history import history_page
from views.resume_analyzer import resume_analyzer
# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="InterviewAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    css_path = Path("assets/style.css")

    if css_path.exists():

        with open(css_path, "r", encoding="utf-8") as file:

            st.markdown(
                f"<style>{file.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==========================================================
# SESSION STATE DEFAULTS
# ==========================================================

DEFAULTS = {

    "page": "hero",

    "logged_in": False,

    "user": None,

    "interview": None

}

for key, value in DEFAULTS.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================================================
# PAGE SWITCH HELPER
# ==========================================================

def switch_page(page):

    st.session_state.page = page

    st.rerun()

# ==========================================================
# HERO PAGE
# ==========================================================

def hero_page():

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            """
            <h1 style="text-align:center;
            font-size:70px;
            color:white;">
            🤖 InterviewAI
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <h3 style="text-align:center;
            color:#94A3B8;">
            Ace Every Interview with AI
            </h3>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            """
            <p style="text-align:center;
            color:#CBD5E1;
            font-size:20px;
            line-height:1.8;">

            Practice Technical Interviews<br>

            Receive AI Feedback<br>

            Analyze Your Resume<br>

            Track Your Progress

            </p>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "🚀 Get Started",
            use_container_width=True
        ):

            switch_page("login")

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="card">

            <h2>🎤 AI Interviews</h2>

            <p>Practice Technical & HR Interviews</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="card">

            <h2>📄 Resume Analyzer</h2>

            <p>ATS Score & AI Feedback</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="card">

            <h2>📊 Analytics</h2>

            <p>Track Your Growth</p>

            </div>
            """,
            unsafe_allow_html=True
        )
        # ==========================================================
# LOGIN PAGE
# ==========================================================

def login_page():

    left, center, right = st.columns([1, 1.3, 1])

    with center:

        st.title("Welcome Back 👋")

        st.caption("Login to continue.")

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            user = login_user(
                email,
                password
            )

            if user:

                st.session_state.logged_in = True
                st.session_state.user = user

                switch_page("dashboard")

            else:

                st.error(
                    "Invalid email or password."
                )

        st.write("")

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            switch_page("signup")


# ==========================================================
# SIGNUP PAGE
# ==========================================================

def signup_page():

    left, center, right = st.columns([1, 1.3, 1])

    with center:

        st.title("Create Account")

        name = st.text_input(
            "Full Name"
        )

        email = st.text_input(
            "Email"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            if name.strip() == "":

                st.warning(
                    "Please enter your name."
                )

            elif email.strip() == "":

                st.warning(
                    "Please enter your email."
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif len(password) < 6:

                st.warning(
                    "Password must contain at least 6 characters."
                )

            else:

                success = create_user(
                    name,
                    email,
                    password
                )

                if success:

                    st.success(
                        "Account created successfully!"
                    )

                    st.info(
                        "Please login to continue."
                    )

                    switch_page("login")

                else:

                    st.error(
                        "An account with this email already exists."
                    )

        st.write("")

        if st.button(
            "⬅ Back to Login",
            use_container_width=True
        ):

            switch_page("login")
            # ==========================================================
# ROUTER
# ==========================================================

def router():

    page = st.session_state.page

    # ======================================================
    # USER LOGGED IN
    # ======================================================

    if st.session_state.logged_in:

        if page == "dashboard":

            show_dashboard(st.session_state.user)

        elif page == "interview":

            interview_setup()

        elif page == "interview_room":

            interview_room()

        elif page == "history":

            history_page()

        elif page == "resume":

            resume_analyzer()

    # ======================================================
    # USER NOT LOGGED IN
    # ======================================================

    else:

        if page == "hero":

            hero_page()

        elif page == "login":

            login_page()

        elif page == "signup":

            signup_page()

        else:

            st.session_state.page = "hero"

            st.rerun()
            # ==========================================================
# MAIN
# ==========================================================

def main():

    router()


# ==========================================================
# START APPLICATION
# ==========================================================

if __name__ == "__main__":

    main()
