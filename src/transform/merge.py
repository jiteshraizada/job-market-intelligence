def merged_job_data(jobs,details):
    merged_data = []
    for job,detail in zip(jobs,details):
        job.update(detail)
        merged_data.append(job)
    return merged_data