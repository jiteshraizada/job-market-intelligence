import re
def extract_experience(description):
    match = re.search(
        r"(\d+)\s*(?:\+|-)\s*(?:\d+)?\s*years?|(\d+)\s*years?",
        description,
        re.IGNORECASE
    )
    if match:
        if match.group(1):
            experience = match.group(1)
        else:
            experience = match.group(2)
        return f"{experience}+ years"
    return "Unspecified"