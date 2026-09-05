from src.enrich.enrich_jobs import enrich_jobs
import re
def transform_job(job):
    clean_department = re.sub(r'^\d+\s+', '',job['departments']).strip()
    raw_location = job['location']['name'].strip()
    clean_job = {
        'job_id': job['id'],
        'title': job['title'].strip(),
        'company': job['company_name'].strip(),
        'location': raw_location,
        'department': clean_department,
        'office': job['offices'].strip(),
        'first_published_at':job['first_published'].strip(),
        'updated_at': job['updated_at'].strip(),
        'job_url': job['absolute_url'].strip(),
        'description': clean_html(job['content']).strip()
    }
    return clean_job

def transform_jobs(job_list):
    transformed_jobs = []
    for job in job_list:
        transformed_jobs.append(transform_job(job))
    transformed_jobs = enrich_jobs(transformed_jobs)
    return transformed_jobs

import html
from bs4 import BeautifulSoup

def clean_html(content):
    content = html.unescape(content)
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text("\n", strip=True)

