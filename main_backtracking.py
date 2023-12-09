from app.Job import Job
from genetic.Schedule import Schedule

jobs = [
    Job('A', 100),
    Job('B', 7),
    Job('C', 100, ['A','b'], ["r1", "r2"]),
    Job('D', 4, ['C']),
    Job('E', 31, ['B'], ["r3"]),
]
new_jobs = []

for job in jobs:
    if job.is_capacity_exceeded():
        divided_jobs = job.divide_job()
        if divided_jobs:
            new_jobs.extend(divided_jobs)

for job in new_jobs:
    print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}")