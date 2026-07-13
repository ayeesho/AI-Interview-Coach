import streamlit as st


def feature_card(icon,title,text):

    st.markdown(f"""

    <div class="card">

    <h1>{icon}</h1>

    <h3>{title}</h3>

    <p>{text}</p>

    </div>

    """,unsafe_allow_html=True)