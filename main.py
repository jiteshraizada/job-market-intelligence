import pandas as pd
import os
from src.load.processed_jobs import load_processed_jobs
from src.load.load_jobs import load_jobs
from src.load.processed_jobs import processed_jobs
from src.load.export_powerbi import export_for_powerbi
from src.load.database import create_db
COMPANIES = [
    "stripe",
    "cloudflare",
    "gitlab",
    "mongodb",
    "hashicorp",
    "figma",
    "brex",
    "airtable",
    "grammarly",
    "anthropic",
    "coinbase",
    "instacart"
]
DB_PATH = "data/job_market.db"
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print("Old database deleted.")
create_db()
processed_jobs = processed_jobs(COMPANIES,refresh=False)
loaded_jobs = load_processed_jobs()
print("Unique job IDs:", len(set(job["job_id"] for job in loaded_jobs)))
print("Total Jobs:", len(loaded_jobs))
load_jobs(loaded_jobs)
export_for_powerbi()
print("\nPipeline completed successfully.")