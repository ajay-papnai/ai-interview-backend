import google.generativeai as genai

genai.configure(
    api_key="AIzaSyDuzqufK7a4dpiSFRaKv8oynO1JzyTCmlY"
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def analyze_interview(
        questions,
        answers
):

    prompt = f"""
    You are an expert technical interviewer.

    Analyze this mock interview.

    Questions:
    {questions}

    Answers:
    {answers}

    Give response STRICTLY in this JSON format:

    {{
      "overall_score": 85,
      "technical_score": 80,
      "communication_score": 90,
      "confidence_score": 78,
      "strengths": [
        "Good Android knowledge",
        "Clear communication"
      ],
      "weaknesses": [
        "Needs deeper DSA understanding"
      ],
      "suggestions": [
        "Practice system design",
        "Improve database concepts"
      ]
    }}

    Output ONLY valid JSON.
    """

    response = model.generate_content(prompt)

    return response.text