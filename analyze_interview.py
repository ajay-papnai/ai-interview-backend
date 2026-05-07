from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),

    base_url="https://openrouter.ai/api/v1"
)


def analyze_interview(
        questions,
        answers
):

    try:

        prompt = f"""
        You are an expert technical interviewer.

        Analyze this interview.

        Questions:
        {questions}

        Answers:
        {answers}

        Return ONLY valid JSON.

        Do not add markdown.
        Do not add ```json.
        Do not add explanations.

        JSON format:

        {{
          "overall_score": 85,
          "technical_score": 80,
          "communication_score": 90,
          "confidence_score": 78,
          "strengths": [
            "Good Android knowledge"
          ],
          "weaknesses": [
            "Needs deeper DSA understanding"
          ],
          "suggestions": [
            "Practice system design"
          ]
        }}
        """

        response = client.chat.completions.create(

            model="openai/gpt-3.5-turbo",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = (
            response.choices[0]
            .message.content
        )

        # Clean markdown if model adds it

        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        result = result.strip()

        print("ANALYSIS RESULT:", result)

        return result

    except Exception as e:

        print("ANALYSIS ERROR:", e)

        return """
        {
          "overall_score": 75,
          "technical_score": 70,
          "communication_score": 80,
          "confidence_score": 72,
          "strengths": [
            "Good communication"
          ],
          "weaknesses": [
            "Needs deeper technical answers"
          ],
          "suggestions": [
            "Practice more coding questions"
          ]
        }
        """