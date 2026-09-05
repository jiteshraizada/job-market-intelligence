CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE
);
create table if not exists jobs (
    job_pk INTEGER PRIMARY KEY,
    job_id integer not null,
    company_id integer not null,
    title TEXT NOT NULL,
    location TEXT,
    department TEXT,
    office TEXt,
    level TEXT,
    experience TEXT,
    employment_type text,
    work_mode TEXT,
    category TEXT,
    first_published_at TEXT,
    updated_at TEXT,
    job_url TEXT,
    foreign key (company_id) references companies(company_id),
    unique (job_id, company_id)
);
create table if not exists skills (
    skill_id INTEGER PRIMARY KEY,
    skill_name TEXT NOT NULL UNIQUE
);
create table if not exists job_skills (
    job_skill_pk INTEGER PRIMARY KEY,
    job_pk INTEGER NOT NULL,
    skill_id INTEGER NOT NULL,
    FOREIGN KEY (job_pk) REFERENCES jobs(job_pk),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);
