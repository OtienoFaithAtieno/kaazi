import requests

def fetch_jobs():
    jobs = []

    # RemoteOK API
    try:
        res = requests.get("https://remoteok.com/api")
        data = res.json()
        for job in data[1:]:
            jobs.append({
                "title": job.get("position"),
                "company": job.get("company"),
                "description": job.get("description", ""),
                "url": job.get("url")
            })
    except:
        pass

    return jobs