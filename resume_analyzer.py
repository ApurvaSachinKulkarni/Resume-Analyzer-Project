import re
import PyPDF2

# Define a set of skills to search for
SKILL_KEYWORDS = [
    "python", "java", "c++", "c#", "c", "javascript", "html", "css",
    "django", "flask", "react", "angular", "node.js", "mysql","sql",
    "postgresql", "machine learning", "deep learning", "nlp","ml","dl","ai", "artificial intelligence",
    "data analysis", "pandas", "numpy", "git", "aws", "azure",
    "docker", "kubernetes", "data science"
]

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a PDF file."""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.lower()

def extract_skills(text):
    """Finds skills from text using keyword matching."""
    found_skills = []
    for skill in SKILL_KEYWORDS:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)
    return found_skills

def analyze_resume(file_path):
    """
    Main function to analyze resume and return:
    - matched skills
    - score percentage
    """
    text = extract_text_from_pdf(file_path)
    matched = extract_skills(text)
    score = int((len(matched) / len(SKILL_KEYWORDS)) * 100) if SKILL_KEYWORDS else 0
    return matched, score
