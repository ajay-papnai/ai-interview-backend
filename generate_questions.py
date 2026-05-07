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

    Return ONLY questions.
    One question per line.
    """

    response = model.generate_content(prompt)

    raw_text = response.text

    questions = []

    for line in raw_text.split("\n"):

        line = line.strip()

        if line:

            # remove numbering
            line = line.replace("*", "")

            if "." in line[:3]:

                line = line.split(".", 1)[1].strip()

            questions.append(line)

    return questions