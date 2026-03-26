# kaazi
#AI Job Application Agent

An intelligent machine learning system that automatically finds relevant job postings, matches them to your profile, and autonomously applies on your behalf.

---

#Overview

The **AI Job Application Agent** is designed to streamline and automate the job search process by combining:

* Resume parsing
* Machine learning-based job matching
* Automated application generation
* Optional semi/fully automated job applications

This project helps job seekers save time and increase application efficiency by targeting only the most relevant opportunities.

---

# Features

# Resume Parsing

* Upload PDF/DOCX resumes
* Extract:

  * Skills
  * Experience
  * Education
* Convert into structured data

---

# Job Aggregation

* Fetch recent job postings from:

  * APIs (Greenhouse, Lever, etc.)
  * Job boards (Indeed, RemoteOK)
* Store jobs locally for processing

---

#Smart Job Matching (ML)

* Uses NLP to compare resumes with job descriptions
* Supports:

  * TF-IDF + Cosine Similarity
  * Sentence Transformers
* Scores and ranks jobs based on relevance

---

#Application Generator

* Automatically generates:

  * Tailored cover letters
  * Answers to screening questions
* Context-aware responses using job description + resume

---

#Auto-Apply Engine (Optional)

* Modes:

  * Manual (user approval)
  * Semi-automated (form autofill)
  * Fully automated (submission)

Note: Some platforms (e.g., LinkedIn) may restrict automation.

---

#Feedback Learning Loop

* Tracks:

  * Applications sent
  * Responses/interviews
* Improves matching over time

---

#Project Structure

```
job-ai-agent/
│── backend/
│   ├── api/                # FastAPI routes
│   ├── scraper/            # Job fetching logic
│   ├── matcher/            # ML matching engine
│   ├── applier/            # Automation logic
│   ├── resume_parser/      # Resume extraction
│
│── frontend/
│   └── dashboard/          # React UI (optional)
│
│── models/
│   └── job_matcher_model.pkl
│
│── data/
│   └── jobs.db
│
│── requirements.txt
│── README.md
```

---

#Tech Stack

#Backend

* Python
* FastAPI
*PostgreSQL

#Machine Learning

* scikit-learn
* sentence-transformers
* NumPy / Pandas

#Automation

* Playwright (browser automation)

#Frontend

* React

---

#Installation

```bash
# Clone repository
git clone https://github.com/OtienoFaithAtieno/kaazi.git
cd kaazi

# Create virtual environment
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\\Scripts\\activate     # (Windows)

# Install dependencies
pip install -r requirements.txt
```

---

#Usage

### 1. Start Backend Server

```bash
uvicorn backend.api.main:app --reload
```

---

### 2. Upload Resume

* Endpoint: `POST /upload-resume`
* Accepts: PDF/DOCX

---

### 3. Fetch Jobs

```bash
POST /jobs/fetch
```

---

### 4. Run Job Matching

```bash
POST /jobs/match
```

---

### 5. Generate Applications

```bash
POST /applications/generate
```

---

### 6. Apply to Jobs

```bash
POST /applications/apply
```

---

#Example Workflow

1. Upload your resume
2. Fetch latest jobs
3. Run matching algorithm
4. Review top matches
5. Generate applications
6. Apply (manual or automated)

---

#Safety & Compliance

* Avoid aggressive scraping (respect platform terms)
* Use APIs where available
* Prefer semi-automated workflows
* Implement rate limiting and delays

---

#Future Improvements

* Reinforcement learning for better job targeting
* Multi-resume support (different roles)
* Chrome extension for 1-click apply
* Interview prediction scoring
* Email integration (auto-track replies)

---

#Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

---

#Disclaimer

This tool is intended for educational and productivity purposes. Users are responsible for complying with job platform policies and terms of service.

---

#Inspiration

Built to eliminate repetitive job applications and empower smarter job searching using AI.

---

## 📬 Contact

For questions or collaboration:

* Open an issue
* Submit a PR

---
If you like this project, consider starring the repo!
