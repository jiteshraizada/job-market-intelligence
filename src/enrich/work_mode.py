WORK_MODES = {
    "Remote": [
        "remote",
        "work from home",
        "wfh",
        "distributed",
        "telecommute",
        "telecommuting",
        "work from anywhere",
        "work from anywhere",
        "remote work",
        "remote work",
        "home office",
        "home office",
        "from home",
        "from home",
        "at home",
        "at home",
        "at home"
    ],

    "Hybrid": [
        "hybrid"
    ],

    "On-site": [
        "on-site",
        "onsite",
        "in office",
        "in-office",
        "office-based",
        "office based"
    ]
}
def extract_work_mode(location,description):
    sources = [location,description]
    for source in sources:
        source = source.lower()
        for mode, keywords in WORK_MODES.items():
            for keyword in keywords:
                if keyword in source:
                    return mode
    return "Unspecified"