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

        Skills:
        {skills}

        Company:
        {company}

        Generate ONLY ONE professional follow-up interview question.

        IMPORTANT RULES:
        - Return ONLY the question
        - No introduction
        - No headings
        - No explanations
        - No numbering
        - Do not say:
          "Here is a follow-up question"
        - Keep it short and professional
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

        result = (
            response.choices[0]
            .message.content
        )

        # CLEAN RESPONSE

        result = result.replace(
            "Here is a follow-up question:",
            ""
        )

        result = result.replace(
            "Here’s a follow-up question:",
            ""
        )

        result = result.replace(
            "Follow-up question:",
            ""
        )

        result = result.replace(
            "Follow up question:",
            ""
        )

        result = result.replace(
            "*",
            ""
        )

        result = result.strip()

        return result

    except Exception as e:

        print("FOLLOWUP ERROR:", e)

        return (
            "Can you explain that in more detail?"
        )