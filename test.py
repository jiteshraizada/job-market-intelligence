import sqlite3

connection = sqlite3.connect("data/job_market.db")

query = """
SELECT COUNT(*)
FROM job_skills js
LEFT JOIN jobs j
    ON js.job_pk = j.job_pk
WHERE j.job_pk IS NULL
"""

result = connection.execute(query).fetchone()

print("Unmatched job_skills job_pk values:", result[0])

connection.close()