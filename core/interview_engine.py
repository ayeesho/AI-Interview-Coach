import json

from core.gemini_service import gemini

from core.prompts import (
    build_first_question_prompt,
    build_evaluation_prompt,
    build_final_report_prompt
)


# ==========================================================
# START INTERVIEW
# ==========================================================

def start_interview(
    company,
    role,
    difficulty,
    topics
):
    """
    Generate the first interview question.
    """

    prompt = build_first_question_prompt(
        company=company,
        role=role,
        difficulty=difficulty,
        topics=topics
    )

    response = gemini.ask(prompt)

    if not response["success"]:
        return {
            "success": False,
            "message": response["text"]
        }

    return {
        "success": True,
        "question": response["text"]
    }


# ==========================================================
# SAFE JSON PARSER
# ==========================================================

def parse_json(text):
    """
    Converts Gemini JSON string into Python dictionary.
    """

    try:

        # Remove markdown if Gemini returns ```json ... ```
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        data = json.loads(text)

        return {
            "success": True,
            "data": data
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }


# ==========================================================
# EVALUATE ANSWER
# ==========================================================

def evaluate_answer(
    company,
    role,
    difficulty,
    question,
    answer
):
    """
    Evaluate one interview answer.
    """

    prompt = build_evaluation_prompt(
        company=company,
        role=role,
        difficulty=difficulty,
        question=question,
        answer=answer
    )

    response = gemini.ask_json(prompt)

    if not response["success"]:

        return {
            "success": False,
            "message": response["text"]
        }

    parsed = parse_json(response["text"])

    if not parsed["success"]:

        return {
            "success": False,
            "message": parsed["message"]
        }

    return {
        "success": True,
        "result": parsed["data"]
    }
# ==========================================================
# FINISH INTERVIEW
# ==========================================================

def finish_interview(conversation):
    """
    Generate the final interview report.
    """

    prompt = build_final_report_prompt(conversation)

    response = gemini.ask_json(prompt)

    if not response["success"]:

        return {
            "success": False,
            "message": response["text"]
        }

    parsed = parse_json(response["text"])

    if not parsed["success"]:

        return {
            "success": False,
            "message": parsed["message"]
        }

    return {
        "success": True,
        "report": parsed["data"]
    }


# ==========================================================
# CALCULATE AVERAGE
# ==========================================================

def calculate_average(values):

    if not values:
        return 0

    return round(sum(values) / len(values), 2)


# ==========================================================
# CALCULATE OVERALL SCORES
# ==========================================================

def overall_score(
    technical_scores,
    communication_scores,
    confidence_scores
):

    technical = calculate_average(technical_scores)

    communication = calculate_average(communication_scores)

    confidence = calculate_average(confidence_scores)

    overall = round(
        (
            technical +
            communication +
            confidence
        ) / 3,
        2
    )

    return {

        "technical": technical,

        "communication": communication,

        "confidence": confidence,

        "overall": overall

    }


# ==========================================================
# CREATE INTERVIEW STATE
# ==========================================================

def create_interview_state(
    company,
    role,
    difficulty,
    topics,
    total_questions
):

    return {

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


# ==========================================================
# UPDATE INTERVIEW STATE
# ==========================================================

def update_interview_state(
    interview,
    evaluation
):

    interview["technical_scores"].append(
        evaluation["technical"]
    )

    interview["communication_scores"].append(
        evaluation["communication"]
    )

    interview["confidence_scores"].append(
        evaluation["confidence"]
    )

    interview["feedback"].append(
        evaluation["feedback"]
    )

    interview["current_ai_question"] = (
        evaluation["next_question"]
    )

    interview["current_question"] += 1

    if interview["current_question"] > interview["total_questions"]:

        interview["completed"] = True

    return interview


# ==========================================================
# RESET INTERVIEW
# ==========================================================

def reset_interview():

    return {

        "company": "",

        "role": "",

        "difficulty": "",

        "topics": [],

        "total_questions": 0,

        "current_question": 1,

        "current_ai_question": "",

        "conversation": [],

        "technical_scores": [],

        "communication_scores": [],

        "confidence_scores": [],

        "feedback": [],

        "completed": False

    }
