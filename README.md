<div align="center">

# 📊 Job Market Intelligence

### An End-to-End Job Market Analytics Platform

**Python ETL • REST APIs • SQLite • SQL • Power BI • GitHub Actions**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-SQLite-lightgrey?logo=sqlite)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automated-black?logo=githubactions)

</div>

---

## 📌 Overview

**Job Market Intelligence** is an end-to-end data analytics platform built to analyze real-world job postings across multiple companies.

The project extracts job data from company career APIs, cleans and enriches the raw data using Python, stores it in a relational SQLite database, performs analytical SQL queries, and presents the results through an interactive Power BI dashboard.

The pipeline is also automated using **GitHub Actions**, allowing job-market data to be refreshed on a scheduled basis.

### Project Flow

```text
Company Career APIs
        ↓
Python Data Extraction
        ↓
Data Cleaning & Transformation
        ↓
Job Enrichment
        ↓
SQLite Database
        ↓
SQL Analysis
        ↓
Power BI Data Model
        ↓
Interactive Dashboard
        ↓
GitHub Actions Automation
```

---

# 🎯 Project Objectives

- Collect real-world job posting data from multiple companies
- Build a reusable Python ETL pipeline
- Clean and standardize job information
- Extract structured information from unstructured job descriptions
- Store the data in a relational database
- Perform business-oriented SQL analysis
- Build an interactive Power BI dashboard
- Automate the complete data-refresh workflow

---

# 🏗️ Architecture

```text
                         JOB MARKET INTELLIGENCE
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │     Company ATS APIs    │
                    │       Greenhouse        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Python Extraction   │
                    │      requests / API     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ Cleaning & Enrichment   │
                    │ HTML Parsing            │
                    │ Work Mode              │
                    │ Experience              │
                    │ Category / Level        │
                    │ Skills                  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      SQLite Database    │
                    │                         │
                    │ companies               │
                    │ jobs                    │
                    │ skills                  │
                    │ job_skills              │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       SQL Analysis      │
                    │ KPIs / Trends / Skills  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Power BI          │
                    │ DAX + Data Model        │
                    │ Interactive Dashboard   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     GitHub Actions      │
                    │    Daily Automation     │
                    └─────────────────────────┘
```

---

# 📦 Dataset Snapshot

The current dataset contains:

| Metric | Value |
|---|---:|
| Job Postings | **2,870** |
| Companies | **10** |
| Unique Skills | **113** |
| Average Skills / Job | **3.66** |
| Jobs Requiring Python | **598** |
| Jobs Requiring SQL | **456** |
| Jobs Requiring Excel | **171** |
| Dashboard Pages | **3** |

> Dataset values represent the current snapshot and can change after an automated refresh.

---

# 🏢 Companies Covered

The current dataset contains job postings from:

- Airtable
- Anthropic
- Brex
- Cloudflare
- Coinbase
- Figma
- GitLab
- Instacart
- MongoDB
- Stripe

The pipeline is designed so additional companies can be added through the company configuration.

---

# 🔄 Data Pipeline

## 1. Data Extraction

Job postings are collected from company career platforms through public ATS APIs.

The current implementation uses the **Greenhouse Job Board API**.

The extraction layer retrieves information such as:

- Job ID
- Job title
- Company
- Location
- Job description
- Publication date
- Updated date
- Job URL
- Department information

### Extraction Modules

```text
src/
└── extract/
    ├── greenhouse.py
    └── greenhouse_details.py
```

---

## 2. Data Cleaning & Transformation

Raw API responses are transformed into a consistent analytical structure.

The transformation process includes:

- HTML cleaning
- Text normalization
- Location cleaning
- Work-mode classification
- Experience extraction
- Job-level classification
- Job-category classification
- Skill extraction
- Missing-value handling

### Transformation Modules

```text
src/
└── transform/
    ├── clean_jobs.py
    ├── merge.py
    └── html_parser.py
```

---

## 3. Job Enrichment

Additional structured attributes are extracted from job descriptions.

Examples include:

- Experience requirements
- Job level
- Job category
- Skills
- Work mode

This converts unstructured job descriptions into fields that can be analyzed using SQL and Power BI.

---

# 🗄️ Database Design

Processed data is stored in SQLite using a normalized relational structure.

```text
companies
    │
    │ 1 → many
    ▼
  jobs
    │
    │ 1 → many
    ▼
job_skills
    ▲
    │ many → 1
    │
  skills
```

### `companies`

Stores company-level information.

### `jobs`

Stores individual job postings and structured attributes such as:

- Job ID
- Company
- Title
- Location
- Level
- Work Mode
- Category
- Publication date
- Updated date
- Job URL

### `skills`

Contains the standardized skill dictionary.

### `job_skills`

Bridge table connecting jobs and skills.

The bridge table enables many-to-many analysis between job postings and required skills.

---

# 🔎 SQL Analysis

SQL is used to perform analytical queries on the relational database.

### Hiring Analysis

- Total job postings
- Hiring volume by company
- Jobs by category
- Jobs by job level
- Jobs by work mode
- Jobs by location

### Company Analysis

- Data roles by company
- Finance roles by company
- Internship opportunities by company
- Senior roles by company
- Category distribution by company

### Skill Analysis

- Most demanded skills
- Skills by company
- Skills by category
- Python demand
- SQL demand
- Excel demand
- Skills associated with SQL
- Skills associated with Python
- Skill combinations

### Data Quality Analysis

- Jobs without extracted skills
- Average skills per job
- Skill coverage across companies

SQL queries are stored in:

```text
sql/
└── queries.sql
```

---

# 📊 Power BI Dashboard

The Power BI report contains **three analytical pages**.

The dashboard uses a relational model connecting:

```text
companies → jobs → job_skills ← skills
```

Global filters allow the analysis to be explored by:

- Company
- Category
- Level
- Work Mode
- Location

---

# 1️⃣ Job Market Overview

### Purpose

Get the big picture of the job market across all companies.

### Key Insights

- Overall hiring volume
- Top job categories
- Work-mode distribution
- Experience-level distribution
- Company hiring comparison
- Top office locations

### Dashboard Preview

![Job Market Overview](screenshots/Page%201%20Overview.png)

### Analysis

The Overview page provides the high-level picture of the complete job market dataset.

The KPI section includes:

- Total Jobs
- Companies Hiring
- Average Skills / Job
- Work Mode %

The page then breaks the market down by:

- Job Category
- Company
- Work Mode
- Experience
- Office Location

This page is designed to answer:

> **What does the overall job market look like across the companies being analyzed?**

---

# 2️⃣ Skills Intelligence

### Purpose

Understand which skills are most demanded across the job market.

### Key Insights

- Most demanded skills
- Skill demand by company
- Skills by job category
- SQL vs Python demand
- Skill combinations

### Dashboard Preview

![Skills Intelligence](screenshots/Page%202%20Skill%20Intelligence.png)

### Analysis

The Skills Intelligence page focuses on employer skill requirements.

### Top Skills by Job Demand

Ranks the most frequently required skills across the dataset.

### Skill Demand by Company

A company × skill matrix compares skill requirements between employers.

### Top Skills by Category

Shows which skills are most associated with different job categories.

### SQL vs Python Demand

Dedicated KPI cards compare the number of jobs requiring SQL and Python.

### Skills Associated with SQL

Shows other skills that frequently appear in jobs that also require SQL.

This allows the analysis to move beyond individual skill counts and examine skill combinations.

This page is designed to answer:

> **What skills are employers asking for, and how do those requirements vary across companies and categories?**

---

# 3️⃣ Company & Role Intelligence

### Purpose

Compare hiring patterns across companies and understand role demand.

### Key Insights

- Company hiring volume
- Roles by company
- Hiring by job level
- Category distribution
- Employment patterns
- Work-mode patterns

### Dashboard Preview

![Company & Role Intelligence](screenshots/Page%203%20Company%20%26%20Role%20Intelligence.png)

### Analysis

The Company & Role Intelligence page focuses on comparing employers and understanding their hiring structures.

### Hiring by Company & Category

Compares hiring volume across companies while showing the category composition of each company's hiring.

### Job Level Mix by Company

Shows how job levels are distributed across companies.

### Top Roles

Ranks the most frequently occurring roles across the dataset.

### Company × Job Level

Provides a detailed matrix showing job-level hiring patterns by company.

### Company Hiring Profile

Allows a company to be selected and analyzed individually.

### Employment Type by Selected Company

Provides a company-specific view of employment patterns.

### Work Mode by Company

Compares Remote, Hybrid and On-site hiring patterns across companies.

This page is designed to answer:

> **How do companies differ in the roles, levels, categories and working patterns they are hiring for?**

---

# 📈 Business Questions Answered

## Hiring

- Which companies are hiring the most?
- Which categories dominate the market?
- Which companies are hiring for Data roles?
- Which companies are hiring for Finance roles?
- Which companies have internship opportunities?

## Skills

- What are the most demanded skills?
- How frequently are SQL and Python required?
- How frequently is Excel required?
- Which skills appear across multiple companies?
- Which skills are associated with SQL?
- Which skills are associated with specific job categories?

## Roles & Experience

- Which roles appear most frequently?
- What experience levels are companies hiring for?
- How does job-level distribution vary between companies?
- Which companies have a greater concentration of senior roles?

## Work Mode

- How many jobs are Remote?
- How many are Hybrid?
- How many are On-site?
- How do work-mode patterns differ between companies?

## Location

- Which office locations have the highest number of opportunities?
- How does location demand vary across companies?

---

# 🧮 Power BI Data Model

The Power BI model follows the relational database structure.

```text
companies[company_id]
        │
        │ 1 → *
        ▼
jobs[company_id]

jobs[job_pk]
        │
        │ 1 → *
        ▼
job_skills[job_pk]

skills[skill_id]
        │
        │ 1 → *
        ▼
job_skills[skill_id]
```

Single-direction relationships are used to maintain controlled filter propagation.

---

# 📐 DAX Measures

The dashboard uses DAX measures for dynamic KPIs and analysis.

### Total Jobs

```DAX
Total Jobs =
COUNTROWS(jobs)
```

### Companies Hiring

```DAX
Companies Hiring =
DISTINCTCOUNT(jobs[company_id])
```

### Total Skills

```DAX
Total Skills =
DISTINCTCOUNT(skills[skill_id])
```

### Average Skills per Job

```DAX
Average Skills per Job =
AVERAGEX(
    VALUES(jobs[job_pk]),
    CALCULATE(COUNTROWS(job_skills))
)
```

### Jobs Requiring SQL

```DAX
Jobs Requiring SQL =
CALCULATE(
    DISTINCTCOUNT(job_skills[job_pk]),
    skills[skill_name] = "SQL"
)
```

### Jobs Requiring Python

```DAX
Jobs Requiring Python =
CALCULATE(
    DISTINCTCOUNT(job_skills[job_pk]),
    skills[skill_name] = "Python"
)
```

The report also uses dynamic filter context so KPIs and visuals respond to selections made through the global filters and dashboard visuals.

---

# ⚙️ Automation

The project uses **GitHub Actions** to automate the pipeline.

The workflow performs:

```text
Scheduled Trigger
       ↓
Checkout Repository
       ↓
Set Up Python
       ↓
Install Dependencies
       ↓
Run main.py
       ↓
Extract Latest Job Data
       ↓
Transform & Enrich Data
       ↓
Rebuild SQLite Database
       ↓
Export Power BI CSV Files
       ↓
Commit Updated Data
       ↓
Push Changes to GitHub
```

The workflow is scheduled to run daily and can also be triggered manually.

Workflow file:

```text
.github/
└── workflows/
    └── job_market_pipeline.yml
```

This allows the data layer to refresh without manually running the pipeline on a local machine.

---

# 🧪 Running the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/jiteshraizada/job-market-intelligence.git
cd job-market-intelligence
```

## 2. Create a virtual environment

```bash
python -m venv venv
```

## 3. Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the pipeline

```bash
python main.py
```

The pipeline will:

1. Extract job postings
2. Transform the raw data
3. Enrich the job records
4. Load the data into SQLite
5. Export Power BI-ready CSV files

---

# 📁 Repository Structure

```text
Job Market Intelligence
│
├── .github/
│   └── workflows/
│       └── job_market_pipeline.yml
│
├── dashboard/
│   └── Job Market Intelligence.pbix
│
├── data/
│   ├── companies.csv
│   ├── job_market.db
│   ├── job_skills.csv
│   ├── jobs.csv
│   ├── processed_jobs.json
│   └── skills.csv
│
├── notebooks/
│
├── raw/
│
├── sql/
│   ├── queries.sql
│   └── schema.sql
│
├── src/
│   ├── extract/
│   │   ├── greenhouse.py
│   │   └── greenhouse_details.py
│   │
│   ├── transform/
│   │   ├── clean_jobs.py
│   │   ├── html_parser.py
│   │   └── merge.py
│   │
│   ├── enrich/
│   │   └── experience.py
│   │
│   └── load/
│       ├── database.py
│       ├── load_jobs.py
│       ├── processed_jobs.py
│       └── export_powerbi.py
│
├── main.py
├── requirements.txt
├── test.py
└── README.md
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Data extraction, transformation and enrichment |
| **Requests** | API requests |
| **Pandas** | Data processing |
| **BeautifulSoup** | HTML parsing and cleaning |
| **SQLite** | Relational data storage |
| **SQL** | Analytical querying |
| **Power BI** | Data modeling, DAX and visualization |
| **Git** | Version control |
| **GitHub** | Repository hosting |
| **GitHub Actions** | Automated pipeline execution |

---

# 📚 Skills Demonstrated

## Data Engineering

- REST API data extraction
- ETL pipeline development
- Data cleaning
- Data transformation
- Data enrichment
- Relational database design
- Automated data refresh

## SQL

- Aggregations
- Joins
- GROUP BY
- DISTINCT counts
- Conditional filtering
- Ranking analysis
- Many-to-many analysis
- Skill association analysis
- Data quality analysis

## Power BI

- Data modeling
- Relationship design
- DAX measures
- Filter context
- Dynamic KPIs
- Interactive slicers
- Matrix analysis
- Drill-down analysis
- Dashboard design

## Business Analytics

- Hiring analysis
- Skill demand analysis
- Company benchmarking
- Job category analysis
- Role analysis
- Work-mode analysis
- Location analysis

---

# 🚀 Roadmap

- [ ] Expand the number of companies tracked
- [ ] Add additional ATS platforms
- [ ] Store historical job snapshots
- [ ] Track newly posted and removed jobs
- [ ] Build job-market trend analysis over time
- [ ] Deploy the data pipeline to Azure
- [ ] Connect cloud-generated data directly to Power BI
- [ ] Add automated data-quality monitoring
- [ ] Add salary analysis where reliable salary data is available
- [ ] Add advanced skill clustering
- [ ] Build predictive job-market insights

---

# 📷 Dashboard Gallery

## Job Market Overview

![Job Market Overview](screenshots/Page%201%20Overview.png)

The overview page summarizes the market through hiring volume, company distribution, categories, work modes, experience and locations.

---

## Skills Intelligence

![Skills Intelligence](screenshots/Page%202%20Skill%20Intelligence.png)

The skills page focuses on employer skill requirements, skill demand by company and category, SQL/Python demand and skill combinations.

---

## Company & Role Intelligence

![Company & Role Intelligence](screenshots/Page%203%20Company%20%26%20Role%20Intelligence.png)

The company and role page compares hiring patterns, categories, job levels, roles and employment characteristics across companies.

---

# 🔗 Repository

**GitHub:**  
https://github.com/jiteshraizada/job-market-intelligence

---

# 👤 Author

## Jitesh Raizada

B.Voc Banking, Financial Services & Insurance  
Ramanujan College, University of Delhi

### Areas of Interest

- Data Analytics
- Business Intelligence
- Finance Analytics
- Banking & FinTech
- SQL
- Python
- Power BI

---

<div align="center">

### Python → SQL → Power BI → Automation

**Job Market Intelligence**

</div>
