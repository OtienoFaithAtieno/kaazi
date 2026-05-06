import pdfplumber
import docx

async def parse_resume(file):
    content = await file.read()
    
    text = ""
    
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    profile = {
        "raw_text": text,
        "skills": extract_skills(text)
    }

    return profile


def extract_skills(text):
    keywords = ["python", "ml", "ai", "data", "api", "react"]
    return [k for k in keywords if k.lower() in text.lower()]