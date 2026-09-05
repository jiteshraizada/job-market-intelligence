EMPLOYMENT_TYPES = {
    "Full-time": ["full-time", "full time"],
    "Part-time": ["part-time", "part time"],
    "Contract": ["contract", "contractor"],
    "Internship": ["intern", "internship"],
    "Temporary": ["temporary", "temp"]
}
def extract_employment_type(description):
    description = description.lower()

    for emp_type, keywords in EMPLOYMENT_TYPES.items():
        for keyword in keywords:
            if keyword in description:
                return emp_type

    return "Unspecified"