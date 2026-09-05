LEVELS = {
    "Intern": ["intern", "internship"],
    "Junior": ["junior", "jr"],
    "Associate": ["associate"],
    "Senior": ["senior", "sr"],
    "Lead": ["lead"],
    "Staff": ["staff"],
    "Principal": ["principal"],
    "Manager": ["manager"],
    "Head": ["head"],
    "Director": ["director"],
    "VP": ["vp", "vice president"],
    "Chief": ["chief", "cto", "ceo", "cfo", "coo"]
}
def extract_job_level(title):
    for level,keywords in LEVELS.items():
        for keyword in keywords:
            if keyword in title.lower():
                return level
    return "Unspecified"
    for job in jobs:
        job['level'] = extract_job_level(job['title'])
        return job