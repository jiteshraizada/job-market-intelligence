import json
from src.extract.greenhouse import extract_jobs
from src.transform.clean_jobs import transform_jobs
def processed_jobs(COMPANIES,refresh=False):
    all_jobs=[]
    for company in COMPANIES:
        raw_jobs = extract_jobs(company, refresh=refresh)
        if not raw_jobs:
            print(f"{company}: No jobs found.")
            continue
        all_jobs.extend(transform_jobs(raw_jobs))
        print(f"Extracted {len(all_jobs)} jobs ")
    with open("data/processed_jobs.json", "w") as f:
        json.dump(all_jobs, f)
    print(f"Processed {len(all_jobs)} jobs")

def load_processed_jobs():
    with open("data/processed_jobs.json", "r", encoding="utf-8") as f:
        return json.load(f)
