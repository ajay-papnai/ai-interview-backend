import pdfplumber
import re
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_path):

    text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        print("PDF Extraction Error:", e)

    return text


def extract_email(text):

    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def extract_phone(text):

    pattern = r"\+?\d[\d\s-]{8,13}\d"

    match = re.search(pattern, text)

    return match.group(0) if match else ""


def extract_name(text):

    try:

        doc = nlp(text)

        for ent in doc.ents:

            if ent.label_ == "PERSON":
                return ent.text

    except Exception as e:

        print("Name Extraction Error:", e)

    return ""


def extract_skills(text):

    skills_db = [

        "python",
        "java",
        "c++",
        "sql",
        "android",
        "kotlin",
        "machine learning",
        "deep learning",
        "nlp",
        "react",
        "node",
        "javascript",
        "html",
        "css",
        "docker",
        "kubernetes",
        "aws",
        "git",
        "firebase",
        "fastapi",
        "mongodb"

    ]

    found = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return list(set(found))