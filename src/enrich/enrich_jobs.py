from src.enrich.level import extract_job_level
from src.enrich.experience import extract_experience
from src.enrich.employment import extract_employment_type
from src.enrich.work_mode import extract_work_mode
from src.enrich.category import extract_category    
from src.enrich.skills import extract_skills
from src.enrich.location import clean_location
def enrich_jobs(jobs):

    for job in jobs:

        job["level"] = extract_job_level(job["title"])
        job["experience"] = extract_experience(job["description"])
        job["employment_type"] = extract_employment_type(job["description"])
        job["work_mode"] = extract_work_mode(job["location"],job["description"])
        job["category"] = extract_category(job["title"])
        job["skills"] = extract_skills(job["description"])
        job["location"] = clean_location(job["location"])

    return jobs
