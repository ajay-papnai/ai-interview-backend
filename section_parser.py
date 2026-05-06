def extract_sections(text):

    sections = {

        "education": "",
        "experience": "",
        "projects": "",
        "skills": ""

    }

    lines = text.split("\n")

    current_section = None

    for line in lines:

        line_lower = line.lower().strip()

        # Detect sections

        if "education" in line_lower:

            current_section = "education"
            continue

        elif "experience" in line_lower:

            current_section = "experience"
            continue

        elif "project" in line_lower:

            current_section = "projects"
            continue

        elif "skill" in line_lower:

            current_section = "skills"
            continue

        # Append data

        if current_section:
            sections[current_section] += line + "\n"

    return sections