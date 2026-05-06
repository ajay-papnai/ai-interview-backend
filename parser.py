from extractor import (
    extract_text_from_pdf,
    extract_email,
    extract_phone,
    extract_name,
    extract_skills
)

from section_parser import extract_sections


def parse_resume(pdf_path):

    text = extract_text_from_pdf(pdf_path)

    sections = extract_sections(text)

    parsed_data = {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "skills": extract_skills(text),

        "education": sections.get("education", ""),

        "experience": sections.get("experience", ""),

        "projects": sections.get("projects", "")

    }

    return parsed_data


if __name__ == "__main__":

    result = parse_resume("resume.pdf")

    import json

    print(json.dumps(result, indent=4))