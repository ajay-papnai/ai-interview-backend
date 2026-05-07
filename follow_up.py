from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),

    base_url="https://openrouter.ai/api/v1"
)


def generate_follow_up_question(
        previous_question,
        user_answer,
        skills,
        company
):

    try:

        prompt = f"""
        Previous Question:
        {previous_question}

        User Answer:
        {user_answer}

        Generate ONE follow-up interview question.
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

        print("FOLLOWUP ERROR:", e)

        return (
            "Can you explain that in more detail?"
        )