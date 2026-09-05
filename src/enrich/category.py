CATEGORIES = {

    "Engineering": [
        "engineer",
        "developer",
        "backend",
        "frontend",
        "full stack",
        "fullstack",
        "android",
        "ios",
        "mobile",
        "firmware",
        "infrastructure"
    ],

    "Data": [
        "data analyst",
        "data scientist",
        "data engineer",
        "machine learning scientist",
        "analytics",
        "science lead"
    ],

    "Product": [
        "product manager",
        "product owner",
        "product lead",
        "product designer"
    ],

    "Program Management": [
        "program manager",
        "project manager"
    ],

    "Sales": [
        "account executive",
        "account manager",
        "sales",
        "business development",
        "sales development"
    ],

    "Marketing": [
        "marketing",
        "brand",
        "communications",
        "comms",
        "content",
        "media",
        "events",
        "art director",
        "community"
    ],

    "Finance": [
        "finance",
        "accounting",
        "accounts receivable",
        "controller",
        "entity controller",
        "audit",
        "tax",
        "treasury",
        "pricing",
        "payments performance"
    ],

    "Operations": [
        "operations",
        "implementation",
        "strategy",
        "strategist",
        "business partner",
        "user escalation",
        "tech ops",
        "techops"
    ],

    "Risk & Security": [
        "risk",
        "security",
        "fraud",
        "compliance",
        "sanctions",
        "investigations"
    ],

    "Legal": [
        "legal",
        "counsel",
        "government relations"
    ],

    "HR": [
        "people",
        "recruit",
        "talent",
        "hr",
        "employee",
        "learning",
        "workplace"
    ],

    "Design": [
        "designer",
        "design",
        "ux",
        "ui"
    ],

    "Customer Success": [
        "customer success"
    ],

    "Support": [
        "support"
    ],

    "Solutions Architecture": [
        "solutions architect",
        "solution architect",
        "technical account manager",
        "technical partner manager",
        "technical connectivity specialist"
    ],

    "Partnerships": [
        "partner development",
        "partnership",
        "alliance",
        "strategic alliances"
    ],

    "Administration": [
        "administrative",
        "coordinator",
        "executive engagement",
        "executive compensation"
    ]
}
def extract_category(title):
    title = title.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in title:
                return category

    return "Uncategorized"