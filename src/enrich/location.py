import re
WORK_MODE_TERMS = [
    "remote",
    "hybrid",
    "distributed",
    "in-office",
    "in office",
    "onsite",
    "on-site"
]
def clean_location(location):
    if not location:
        return None
    location = location.strip()
    # If the entire location is actually a work mode
    for mode in WORK_MODE_TERMS:
        if location.lower() == mode:
            return None
    # Remove work-mode terms from beginning or end
    for mode in WORK_MODE_TERMS:
        pattern = rf'\s*[-,:]?\s*\b{re.escape(mode)}\b\s*[-,:]?\s*'
        location = re.sub(
            pattern,
            '',
            location,
            flags=re.IGNORECASE
        )
        location = re.sub(r'\(\s*\)', '', location)
        location = re.sub(r'\s+', ' ', location)
    return location.strip() or "Unspecified"