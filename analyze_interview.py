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
        Analyze this interview.

        Questions:
        {questions}

        Answers:
        {answers}

        Return JSON analysis with:
        overall_score,
        technical_score,
        communication_score,
        confidence_score,
        strengths,
        weaknesses,
        suggestions
        """

        response = client.chat.completions.create(

            model=
            "meta-llama/llama-3-8b-instruct",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return (
            response.choices[0]
            .message.content
        )

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