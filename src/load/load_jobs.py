import sqlite3
DB_PATH = "data/job_market.db"

def load_jobs(jobs):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute("""
            INSERT OR IGNORE INTO companies (company_name)
            VALUES (?)
        """, (job["company"],))
        cursor.execute("""
            SELECT company_id
            FROM companies
            WHERE company_name = ?
        """, (job["company"],))   
        company_id = cursor.fetchone()[0]
        cursor.execute("""
            INSERT OR IGNORE INTO jobs (
            job_id,
            company_id,
            title,
            location,
            department,
            office,  
            level,
            experience,
            employment_type,
            work_mode,
            category,
            first_published_at,
            updated_at,
            job_url
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
        job["job_id"],
        company_id,
        job["title"],
        job["location"],
        job["department"],
        job["office"],
        job["level"],
        job["experience"],
        job["employment_type"],
        job["work_mode"],
        job["category"],
        job["first_published_at"],
        job["updated_at"],
        job["job_url"]
        ))
        cursor.execute("""
            SELECT job_pk
            FROM jobs
            WHERE job_id = ?
            AND company_id = ?
        """, (job["job_id"], company_id))
        job_pk = cursor.fetchone()[0]
        for skill in job["skills"]:
            cursor.execute("""
            INSERT OR IGNORE INTO skills (skill_name)
            VALUES (?)
            """, (skill,))
            cursor.execute("""
            SELECT skill_id
            FROM skills
            WHERE skill_name = ?
            """, (skill,))
            skill_id = cursor.fetchone()[0]
            cursor.execute("""
            INSERT OR IGNORE INTO job_skills (job_pk, skill_id)
            VALUES (?, ?)
            """, (job_pk, skill_id))
    conn.commit()
    conn.close()
