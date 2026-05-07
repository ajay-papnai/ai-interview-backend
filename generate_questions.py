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
        Generate exactly 10 technical interview questions.

        Skills:
        {skills}

        Company:
        {company}

        IMPORTANT RULES:
        - Return ONLY questions
        - No introduction
        - No headings
        - No explanations
        - No numbering
        - One question per line
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

        text = (
            response.choices[0]
            .message.content
        )

        questions = []

        for line in text.split("\n"):

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            # REMOVE unwanted intro lines

            if (
                    "here are" in lower
                    or "interview questions" in lower
                    or "questions:" in lower
            ):
                continue

            # remove numbering

            if "." in line[:3]:

                try:
                    line = line.split(
                        ".", 1
                    )[1].strip()

                except:
                    pass

            questions.append(line)

        # Ensure only 10

        questions = questions[:10]

        return questions

    except Exception as e:

        print("QUESTION ERROR:", e)

        return [

            "Tell me about yourself.",

            "Explain your strongest project.",

            "What is Firebase Authentication?",

            "Explain RecyclerView in Android.",

            "Why should we hire you?"
        ]