import google.generativeai as genai

genai.configure(
    api_key="AIzaSyDuzqufK7a4dpiSFRaKv8oynO1JzyTCmlY"
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_questions(skills, company):

    prompt = f"""
    Generate 5 interview questions.

    Skills:
    {skills}

    Company:
    {company}

    Output only questions.
    """

    response = model.generate_content(prompt)

    questions = response.text.split("\n")

    cleaned_questions = []

    for question in questions:

        question = question.strip()

        if question:
            cleaned_questions.append(question)

    return cleaned_questions