"""
Prompt Builder

This file contains all prompts used by Gemini.

Never call Gemini from here.
Only return prompt strings.
"""


# ==========================================================
# FIRST QUESTION PROMPT
# ==========================================================

def build_first_question_prompt(
    company,
    role,
    difficulty,
    topics
):

    return f"""
You are an expert technical interviewer.

Conduct an interview for:

Company: {company}

Role: {role}

Difficulty: {difficulty}

Topics:
{topics}

Rules:

- Ask ONE interview question only.
- The question should match the difficulty.
- Do not give hints.
- Do not explain the answer.
- Wait for the candidate's response.
- Do not ask multiple questions.

Return ONLY the interview question.
"""


# ==========================================================
# ANSWER EVALUATION PROMPT
# ==========================================================

def build_evaluation_prompt(
    question,
    answer,
    company,
    role,
    difficulty
):

    return f"""
You are an expert interviewer at {company}.

Role:
{role}

Difficulty:
{difficulty}

Interview Question:

{question}

Candidate Answer:

{answer}

Evaluate the answer.

Return ONLY valid JSON.

Do NOT use markdown.

Return this exact structure:

{{
    "technical": 0,
    "communication": 0,
    "confidence": 0,
    "feedback": "",
    "strengths": "",
    "improvements": "",
    "next_question": ""
}}

Scoring Rules

Technical:
0-100

Communication:
0-100

Confidence:
0-100

Feedback should be 2-3 sentences.

Strengths should be short.

Improvements should be short.

Generate ONE next interview question.

Return ONLY JSON.
"""
# ==========================================================
# FINAL REPORT PROMPT
# ==========================================================

def build_final_report_prompt(
    conversation
):

    return f"""
You are an experienced technical interviewer.

Below is the complete interview conversation.

{conversation}

Generate a detailed interview report.

Return ONLY valid JSON.

Do not use markdown.

Return this format:

{{
    "overall_score": 0,
    "technical_summary": "",
    "communication_summary": "",
    "confidence_summary": "",
    "strengths": "",
    "weaknesses": "",
    "recommended_topics": "",
    "overall_feedback": ""
}}

Overall Score:
0-100

Keep every summary concise.

Return ONLY JSON.
"""


# ==========================================================
# RESUME ANALYZER PROMPT
# ==========================================================




# ==========================================================
# ASSIGNMENT ANALYZER PROMPT
# ==========================================================

def build_assignment_prompt(
    assignment_text
):

    return f"""
You are an expert professor.

Review the assignment below.

{assignment_text}

Return ONLY JSON.

{{
    "score":0,
    "grammar":"",
    "logic":"",
    "improvements":"",
    "feedback":""
}}

Return ONLY JSON.
"""


# ==========================================================
# CODING INTERVIEW PROMPT
# ==========================================================

def build_coding_prompt(
    language,
    difficulty
):

    return f"""
You are a senior software engineer.

Generate ONE coding interview question.

Language:

{language}

Difficulty:

{difficulty}

Return ONLY JSON.

{{
    "title":"",
    "question":"",
    "constraints":"",
    "example_input":"",
    "example_output":""
}}

Return ONLY JSON.
"""


# ==========================================================
# HR INTERVIEW PROMPT
# ==========================================================

def build_hr_prompt(
    company,
    role
):

    return f"""
You are an HR interviewer at {company}.

Interviewing for:

{role}

Generate ONE professional HR interview question.

Return ONLY the question.

Do not explain.

Do not use markdown.
"""
RESUME_ANALYZER_PROMPT = """
You are a professional ATS Resume Reviewer.

Analyze the following resume.

Return ONLY valid JSON.

{{
  "ats_score": 0,
  "strengths": [],
  "weaknesses": [],
  "missing_skills": [],
  "grammar_feedback": "",
  "formatting_feedback": "",
  "recommendations": []
}}

Resume:

{resume}
"""
