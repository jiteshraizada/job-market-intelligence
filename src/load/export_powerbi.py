import sqlite3
import csv
from pathlib import Path


# Project root
BASE_DIR = Path(__file__).resolve().parents[2]

DB_PATH = BASE_DIR / "data" / "job_market.db"
DATA_DIR = BASE_DIR / "data"


def export_table(connection, query, output_file):
    """Export a SQL query result to CSV."""

    cursor = connection.execute(query)

    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    output_path = DATA_DIR / output_file

    # Remove embedded line breaks from text fields
    cleaned_rows = []

    for row in rows:
        cleaned_row = [
            value.replace("\r\n", " ").replace("\r", " ").replace("\n", " ")
            if isinstance(value, str)
            else value
            for value in row
        ]

        cleaned_rows.append(cleaned_row)

    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(
            f,
            quoting=csv.QUOTE_ALL,
            lineterminator="\n"
        )

        writer.writerow(columns)
        writer.writerows(cleaned_rows)

    print(f"Exported {len(rows)} rows → {output_file}")
    
def export_for_powerbi():
    """Export Power BI tables from SQLite."""

    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    connection = sqlite3.connect(DB_PATH)

    try:

        # Companies
        export_table(
            connection,
            """
            SELECT *
            FROM companies
            """,
            "companies.csv"
        )

        # Jobs
        export_table(
            connection,
            """
            SELECT *
            FROM jobs
            """,
            "jobs.csv"
        )

        # Skills
        export_table(
            connection,
            """
            SELECT *
            FROM skills
            """,
            "skills.csv"
        )

        # Job-Skill bridge table
        export_table(
            connection,
            """
            SELECT *
            FROM job_skills
            """,
            "job_skills.csv"
        )

    finally:
        connection.close()

    print("\nPower BI CSV export completed.")


if __name__ == "__main__":
    export_for_powerbi()