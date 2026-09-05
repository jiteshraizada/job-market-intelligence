import sqlite3
DB_PATH = "data/job_market.db"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open("sql/schema.sql", "r") as f:
        schema = f.read()
        cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Database created successfully.")

if __name__ == "__main__":
    create_db()