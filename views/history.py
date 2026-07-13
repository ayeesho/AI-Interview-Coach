import streamlit as st

from database.database import get_interview_history


def history_page():

    st.title("📋 Interview History")
    import streamlit as st

def history_page():

    col1, col2 = st.columns([8, 2])

    with col1:
        st.title("📋 Interview History")

    with col2:
        st.write("")
        st.write("")

        if st.button("⬅ Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

    st.divider()

    user = st.session_state.user

    username = user[1]

    history = get_interview_history(username)

    if len(history) == 0:

        st.info("No interviews found.")

        return

    for interview in history:

        st.divider()

        st.subheader(f"🏢 {interview[2]}")

        st.write(f"**Role:** {interview[3]}")

        st.write(f"**Difficulty:** {interview[4]}")

        st.write(f"**Date:** {interview[6]}")

        st.write(f"**Overall Score:** {interview[7]}%")