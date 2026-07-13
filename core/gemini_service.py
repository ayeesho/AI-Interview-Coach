from google import genai
from config import GEMINI_API_KEY


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model = "gemini-2.5-flash"

    # =====================================================
    # Generic Prompt
    # =====================================================

    def ask(self, prompt):

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return {

                "success": True,

                "text": response.text.strip()

            }

        except Exception as e:

            return {

                "success": False,

                "text": str(e)

            }

    # =====================================================
    # JSON Prompt
    # =====================================================

    def ask_json(self, prompt):

        result = self.ask(prompt)

        if not result["success"]:

            return result

        return {

            "success": True,

            "text": result["text"]

        }


# Singleton
gemini = GeminiService()

