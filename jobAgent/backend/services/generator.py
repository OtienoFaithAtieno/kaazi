def generate_application(profile, job):
    template = f"""
Dear Hiring Manager,

I am excited to apply for the {job['title']} role at {job['company']}.

My experience in {", ".join(profile.get("skills", []))} aligns well with this role.

I am confident I can contribute effectively to your team.

Best regards,
Candidate
"""

    return {
        "job": job["title"],
        "company": job["company"],
        "cover_letter": template,
        "url": job["url"]
    }