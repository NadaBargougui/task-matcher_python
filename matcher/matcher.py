import os
import fitz  # PyMuPDF
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Define known skills
SKILL_SET = ["python", "java", "sql", "devops", "aws", "docker", "kubernetes", "linux", "tensorflow", "react"]

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.lower()

def extract_skills(text):
    doc = nlp(text)
    skills = set()
    for token in doc:
        if token.text.lower() in SKILL_SET:
            skills.add(token.text.lower())
    return list(skills)

def get_unassigned_employees(resume_folder):
    employees = []
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(os.path.join(resume_folder, filename))
            skills = extract_skills(text)
            name = filename[:-4]
            employees.append({"name": name, "skills": skills})
    return employees

def extract_task_skills(task_description):
    return extract_skills(task_description.lower())

def match_task_to_employee(task_skills, employees):
    matches = []
    for emp in employees:
        if not emp['skills']:
            score = 0
        else:
            score = len(set(emp['skills']) & set(task_skills)) / len(set(task_skills))
        matches.append((emp['name'], score))
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches   