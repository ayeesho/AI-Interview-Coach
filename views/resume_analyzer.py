import streamlit as st
from core.resume_parser import extract_resume_text
from core.gemini_service import gemini
def resume_analyzer():
 import streamlit as st
import json

from core.resume_parser import extract_resume_text
from core.gemini_service import gemini
from core.prompts import RESUME_ANALYZER_PROMPT


def resume_analyzer():

    st.title("📄 Resume Analyzer")
    col1, col2 = st.columns([8, 2])

    with col1:
        st.title("📄 Resume Analyzer")

    with col2:
        st.write("")
        st.write("")

        if st.button("⬅ Dashboard"):
            st.session_state.page = "dashboard"
            st.rerun()

    st.write(
        "Upload your resume and receive an AI-powered ATS analysis."
    )

    st.divider()

    st.subheader("Supported Formats")

    st.success("✔ PDF")
    st.success("✔ DOCX")

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success("✅ Resume uploaded successfully!")

        st.write(f"**File Name:** {uploaded_file.name}")
        st.write(f"**File Type:** {uploaded_file.type}")
        st.write(f"**File Size:** {round(uploaded_file.size/1024,2)} KB")

        st.divider()

        if st.button("🔍 Analyze Resume", use_container_width=True):

            # STEP 1 : Read Resume
            with st.spinner("Reading Resume..."):
                resume_text = extract_resume_text(uploaded_file)

            st.success("✅ Resume Read Successfully!")

            # STEP 2 : Create Prompt
            prompt = RESUME_ANALYZER_PROMPT.format(
                resume=resume_text
            )

            # STEP 3 : Send to Gemini
            with st.spinner("Analyzing Resume..."):
                response = gemini.ask(prompt)

            if not response["success"]:
                st.error(response["text"])
                return
            text = response["text"].strip()

            # Remove markdown if Gemini returns ```json ... ```
            if text.startswith("```json"):
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

            # STEP 4 : Convert JSON
            try:
                
                report = json.loads(text)

            except Exception:

                st.error("Gemini returned invalid JSON.")

                st.subheader("Raw Gemini Response")

                st.code(text)

                return

            st.success("✅ Resume Analysis Complete!")

            st.metric(
                "ATS Score",
                f"{report['ats_score']}%"
            )

            st.divider()

            st.subheader("💪 Strengths")

            for item in report["strengths"]:
                st.success(item)

            st.divider()

            st.subheader("⚠ Weaknesses")

            for item in report["weaknesses"]:
                st.warning(item)

            st.divider()

            st.subheader("🚀 Missing Skills")

            for skill in report["missing_skills"]:
                st.info(skill)

            st.divider()

            st.subheader("📝 Grammar Feedback")

            st.write(report["grammar_feedback"])

            st.divider()

            st.subheader("📄 Formatting Feedback")

            st.write(report["formatting_feedback"])

            st.divider()

            st.subheader("🎯 Recommendations")

            for item in report["recommendations"]:
                st.success(item)

    else:

        st.button(
            "🔍 Analyze Resume",
            disabled=True,
            use_container_width=True
        )