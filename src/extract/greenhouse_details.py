import os
import json
import requests
import pandas as pd

def fetch_all_job_details(company, job_list,refresh=False):
    cache_file = f"raw/{company}_job_details.json"
    if os.path.exists(cache_file) and not refresh:
        print(f"Loading {company} jobs_details from cache")
        with open(cache_file, "r",encoding="utf-8") as file:
            return json.load(file)
    else:
        print(f"Fetching {company} jobs_details from API")
        all_jobs = []
        for i, job in enumerate(job_list):
            print(f"{i+1}/{len(job_list)}")
            job_details = fetch_job_details(company, job['id'])
            all_jobs.append(job_details)
        with open(cache_file, "w",encoding="utf-8") as file:
            json.dump(all_jobs, file,indent=4)
        return all_jobs

def fetch_job_details(company,job_id):
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs/{job_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "content": data['content'],
            'departments': data['departments'][0]['name'] if data['departments'] else 'Not Specified',
            'offices': data['offices'][0]['name'] if data['offices'] else 'Not Specified'
        }
    else:
        print("Error fetching job details")
        return None
