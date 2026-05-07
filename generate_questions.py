from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(

    api_key=os.getenv("OPENROUTER_API_KEY"),

    base_url="https://openrouter.ai/api/v1"
)


def generate_questions(skills, company):

    try:

        prompt = f"""
        Generate 10 interview questions.

        Skills:
        {skills}

        Company:
        {company}

        Output only questions.
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

        text =response.choices[0].message.content

        questions = []

        for line in text.split("\n"):

            line = line.strip()

            if line:

                questions.append(line)

        return questions

    except Exception as e:

        print("QUESTION ERROR:", e)

        return [
            "Tell me about yourself."
        ]