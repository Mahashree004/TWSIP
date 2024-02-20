import spacy
import re


nlp = spacy.load("en_core_web_sm")

def resume_parser(text):
    doc = nlp(text)
    entities = {}
    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = [ent.text]
        else:
            entities[ent.label_].append(ent.text)
    projects = re.findall(r'-\s([\w\s]+)', text)
    entities['PROJECTS'] = projects
    certifications = re.findall(r'[-\s]([A-Za-z\s]+Certification)', text)
    entities['CERTIFICATIONS'] = certifications
    return entities

def validate_email(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_regex, text)
    return emails

def validate_phone_number(text):
    phone_regex = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\+\d{2}\s\d{10})'
    phone_numbers = re.findall(phone_regex, text)
    return phone_numbers

def extract_skills(text):
    skills = ["Python", "Java", "SQL", "Machine Learning", "Data Analysis","Cloud Security"]
    extracted_skills = []
    for skill in skills:
        if skill.lower() in text.lower():
            extracted_skills.append(skill)
    return extracted_skills

def print_resume_output(resume_output):
    print("{")
    print("    'Name':", f"'{resume_output['Name']}'")
    print("    'Role':", f"'{resume_output['Role']}'")
    print("    'Parsed Entities': {")
    for key, values in resume_output["Parsed Entities"].items():
        print(f"        '{key}': [")
        for value in values:
            print(f"            '{value}',")
        print("        ],")
    print("    },")
    print("    'Projects': [")
    for project in resume_output["Projects"]:
        print(f"        '{project}',")
    print("    ],")
    print("    'Certifications': [")
    for certification in resume_output["Certifications"]:
        print(f"        '{certification}',")
    print("    ],")
    print("    'Emails': [")
    for email in resume_output["Emails"]:
        print(f"        '{email}',")
    print("    ],")
    print("    'Phone Numbers': [")
    for phone_number in resume_output["Phone Numbers"]:
        print(f"        '{phone_number}',")
    print("    ],")
    print("    'Skills': [")
    for skill in resume_output["Skills"]:
        print(f"        '{skill}',")
    print("    ],")
    print("}")

def main():
    resume_text = """
    Maha Shree Baskaran
    shreemaha151@gmail.com
    +91 6385247072

    Skills:
    - Python
    - SQL
    - Data Analysis
    - Java
    - Cloud Security

    Experience:
    - Senior AWS Solution Architect: Evaluate 5+ proposals daily & recommended the best technical solutions to migrate the application to AWS.
    - Created the architecture and created the Cloud Formation template to facilitate deployment.

    Education:
    - Bachelor's degree in Computer Science and Engineering - PSNACET (2022-2026)

    Projects:
    - Bug Tracker
    - Attendance Tracker
    - Movie Ticket Booking System

    Certifications:
    - Microsoft Azure Certifications
    - Google Certified Professional Cloud Architect
    - Amazon Web Services(AWS) Solutions Architect - Associate
    """

    
    parsed_entities = resume_parser(resume_text)
    emails = validate_email(resume_text)
    phone_numbers = validate_phone_number(resume_text)
    skills = extract_skills(resume_text)


    parsed_entities_dict = {}
    for key, values in parsed_entities.items():
        parsed_entities_dict[key] = values

    projects_dict = {"Projects": parsed_entities.get('PROJECTS', [])}
    certifications_dict = {"Certifications": parsed_entities.get('CERTIFICATIONS', [])}
    emails_dict = {"Emails": emails}
    phone_numbers_dict = {"Phone Numbers": phone_numbers}
    skills_dict = {"Skills": skills}

    
    resume_output = {
        "Name": "MAHA SHREE BASKARAN",
        "Role": "CLOUD ANALYST",
        "Parsed Entities": parsed_entities_dict,
        **projects_dict,
        **certifications_dict,
        **emails_dict,
        **phone_numbers_dict,
        **skills_dict
    }


    print_resume_output(resume_output)

if __name__ == "__main__":
    main()
