from fastapi import APIRouter, UploadFile, File
from backend.services import cvParser, jobFetcher, matcher, generator

router = APIRouter()

PROFILE = {}
JOBS = []
MATCHED = []

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    global PROFILE
    PROFILE = await resume_parser.parse_resume(file)
    return {"message": "Resume parsed", "profile": PROFILE}

@router.post("/jobs/fetch")
def fetch_jobs():
    global JOBS
    JOBS = job_fetcher.fetch_jobs()
    return {"jobs_fetched": len(JOBS)}

@router.post("/jobs/match")
def match_jobs():
    global MATCHED
    MATCHED = matcher.match_jobs(PROFILE, JOBS)
    return {"matched_jobs": MATCHED}

@router.post("/applications/generate")
def generate_apps():
    applications = []
    for job in MATCHED:
        app = generator.generate_application(PROFILE, job)
        applications.append(app)
    return {"applications": applications}