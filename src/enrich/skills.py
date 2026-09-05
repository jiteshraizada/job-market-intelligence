import re
SKILLS = {

    "Engineering": {
        "Python": ["python"],
        "Java": ["java"],
        "JavaScript": ["javascript", "js"],
        "TypeScript": ["typescript"],
        "C++": ["c++"],
        "C#": ["c#", "c sharp"],
        "Go": ["golang"],
        "Rust": ["rust"],
        "PHP": ["php"],
        "Ruby": ["ruby"],
        "Kotlin": ["kotlin"],
        "Swift": ["swift"],

        "HTML": ["html"],
        "CSS": ["css"],
        "React": ["react"],
        "Angular": ["angular"],
        "Vue.js": ["vue.js"],
        "Node.js": ["node.js", "nodejs"],
        "Express.js": ["express.js"],
        "Next.js": ["next.js", "nextjs"],

        "Django": ["django"],
        "Flask": ["flask"],
        "FastAPI": ["fastapi", "fast api"],
        "Spring Boot": ["spring boot"],
        ".NET": [".net", "dotnet", "asp.net"],

        "Docker": ["docker"],
        "Kubernetes": ["kubernetes", "k8s"],
        "Terraform": ["terraform"],
        "AWS": ["aws", "amazon web services"],
        "Azure": ["azure"],
        "GCP": ["gcp", "google cloud platform"],

        "Redis": ["redis"],
        "Kafka": ["kafka"],
        "Git": ["git"],
        "GitHub": ["github"],
        "GitLab": ["gitlab"],
        "REST API": ["rest api", "restful api"],
        "GraphQL": ["graphql"],
        "Linux": ["linux"]
    },

    "Data": {
        "SQL": ["sql"],
        "Python": ["python"],
        "Excel": ["excel"],
        "R": [" r "],
        "Power BI": ["power bi","powerbi","power-bi","microsoft power bi","power bi desktop","power bi service"],
        "Tableau": ["tableau"],
        "Pandas": ["pandas","python pandas"],
        "Power Query": ["power query","powerquery"],
        "NumPy": ["numpy"],
        "Matplotlib": ["matplotlib"],
        "Seaborn": ["seaborn"],
        "DAX": ["dax","data analysis expressions"],
        "Tableau": ["tableau"],
        "Looker": ["looker"],
        "Looker Studio": ["looker studio"],
        "Qlik": ["qlik"],
        "Alteryx": ["alteryx"],
        "SAS": ["sas"],
        "SPSS": ["spss"],
        "Stata": ["stata"],

        "Apache Spark": ["apache spark", "spark"],
        "Hadoop": ["hadoop"],
        "Airflow": ["airflow"],
        "dbt": ["dbt"],
        "Snowflake": ["snowflake"],
        "Databricks": ["databricks"],

        "Machine Learning": ["machine learning"],
        "Deep Learning": ["deep learning"],
        "TensorFlow": ["tensorflow"],
        "PyTorch": ["pytorch"],
        "Scikit-learn": ["scikit-learn","scikit learn","sklearn","sci-kit learn"],
        "XGBoost": ["xgboost"]
    },

    "Product": {
        "Product Management": ["product management"],
        "Product Strategy": ["product strategy"],
        "Roadmapping": ["roadmapping"],
        "User Research": ["user research"],
        "A/B Testing": ["a/b testing", "ab testing"],
        "Wireframing": ["wireframing"],
        "Prototyping": ["prototyping"],
        "Figma": ["figma"],
        "Jira": ["jira"],
        "Confluence": ["confluence"],
        "Mixpanel": ["mixpanel"],
        "Amplitude": ["amplitude"]
    },

    "Design": {
        "Figma": ["figma"],
        "Adobe XD": ["adobe xd"],
        "Sketch": ["sketch"],
        "Photoshop": ["photoshop"],
        "Illustrator": ["illustrator"],
        "UI Design": ["ui design"],
        "UX Design": ["ux design"],
        "Design Systems": ["design systems"]
    },

    "Finance": {
        "Excel": ["excel"],
        "SQL": ["sql"],
        "Power BI": ["power bi","powerbi","power-bi","microsoft power bi","power bi desktop","power bi service"],
        "SAP": ["sap"],
        "Oracle ERP": ["oracle erp"],
        "NetSuite": ["netsuite"],
        "QuickBooks": ["quickbooks"],
        "Hyperion": ["hyperion"],
        "Financial Modeling": ["financial modeling"],
        "Forecasting": ["forecasting"],
        "Budgeting": ["budgeting"],
        "Accounting": ["accounting"]
    },

    "Risk & Security": {
        "Risk Management": ["risk management"],
        "Fraud Detection": ["fraud detection"],
        "Cybersecurity": ["cybersecurity"],
        "AML": ["aml"],
        "KYC": ["kyc"],
        "IAM": ["iam"],
        "SIEM": ["siem"],
        "ISO 27001": ["iso 27001"],
        "PCI DSS": ["pci dss"]
    },

    "Marketing": {
        "SEO": ["seo"],
        "SEM": ["sem"],
        "Google Analytics": ["google analytics", "ga4"],
        "HubSpot": ["hubspot"],
        "Marketo": ["marketo"],
        "Content Marketing": ["content marketing"],
        "Email Marketing": ["email marketing"]
    },

    "Sales": {
        "Salesforce": ["salesforce"],
        "CRM": ["crm"],
        "Lead Generation": ["lead generation"],
        "Sales Strategy": ["sales strategy"],
        "Negotiation": ["negotiation"]
    },

    "Customer Success": {
        "Customer Success": ["customer success"],
        "Zendesk": ["zendesk"],
        "Salesforce": ["salesforce"],
        "CRM": ["crm"]
    },

    "HR": {
        "HRIS": ["hris"],
        "Workday": ["workday"],
        "Performance Management": ["performance management"]
    },

    "Legal": {
        "Contract Management": ["contract management"],
        "Corporate Law": ["corporate law"],
        "Legal Research": ["legal research"],
        "GDPR": ["gdpr"]
    },

    "Operations": {
        "Project Management": ["project management"],
        "ERP": ["erp"],                 # Removed "enterprise"
        "Lean": ["lean"],
        "Six Sigma": ["six sigma"]
    }
}

COMPILED_SKILLS = {}
for domain, domain_skills in SKILLS.items():
    for skill, keywords in domain_skills.items():
        COMPILED_SKILLS[skill] = [
            re.compile(rf"\b{re.escape(keyword.lower())}\b")
            for keyword in keywords
        ]
def extract_skills(description):
    description = description.lower()
    skills = set()
    for skill, patterns in COMPILED_SKILLS.items():
        for pattern in patterns:
            if pattern.search(description):
                skills.add(skill)
                break
    return sorted(skills)