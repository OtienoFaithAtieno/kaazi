from sklearn.metrics.pairwise import cosine_similarity #computes similarity between vectors
from backend.models.embedding import encode
from backend.config import SIMILARITY_THRESHOLD, TOP_K

def match_jobs(profile, jobs):
    results = [] #list to store matched jobs

    profile_vec = encode(profile["raw_text"]) #encodes the raw text from the profile into a vector using the encode function

    for job in jobs:
        job_vec = encode(job["description"])
        score = cosine_similarity([profile_vec], [job_vec])[0][0] # computes similarity between the profile and job vector extracting the scalar score
        
        if score > SIMILARITY_THRESHOLD:
            job["score"] = float(score)
            results.append(job)

    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results[:TOP_K]