import requests
import pandas as pd
import json
import os
from src.transform.merge import merged_job_data
from src.extract.greenhouse_details import fetch_all_job_details

def fetch_jobs(company,refresh=False):
    cache_file = f"raw/{company}_jobs.json"
    if os.path.exists(cache_file) and not refresh:
        print(f"Loading {company} jobs from cache")
        with open(cache_file, "r",encoding="utf-8") as file:
            return json.load(file)
    else:
        print(f"Fetching {company} jobs from Greenhouse API")
        jobs = fetch_jobs_from_api(company)
        with open(cache_file, "w",encoding="utf-8") as file:
            json.dump(jobs, file,indent=4)
        return jobs
    
def fetch_jobs_from_api(company):
    url =f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        job_list = data['jobs']
        return job_list
    else:
        print(f"{company}: Greenhouse board not found.")
        return None

def extract_jobs(company,refresh=False):
    jobs = fetch_jobs(company,refresh=refresh)
    if jobs is None:
        return []
    jobs_details = fetch_all_job_details(company,jobs,refresh=refresh)
    merged_jobs = merged_job_data(jobs,jobs_details)
    return merged_jobs