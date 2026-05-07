import google.generativeai as genai

genai.configure(
    api_key="AIzaSyDuzqufK7a4dpiSFRaKv8oynO1JzyTCmlY"
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def generate_follow_up_question(

        previous_question,

        user_answer,

        skills,

        company
):

    prompt = f"""
    You are an AI technical interviewer.

    Previous Question:
    {previous_question}

    User Answer:
    {user_answer}

    Candidate Skills:
    {skills}

    Target Company:
    {company}

    Generate ONE natural follow-up interview question.

    Rules:
    - Ask deeper technical question
    - Be conversational
    - Keep concise
    - Behave like real interviewer
    - Output only question
    """

    response = model.generate_content(prompt)

    return response.text