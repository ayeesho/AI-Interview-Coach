from core.interview_engine import start_interview

result = start_interview(
    company="Google",
    role="Software Engineer",
    difficulty="Medium",
    topics=["Python", "SQL"]
)

print(result)