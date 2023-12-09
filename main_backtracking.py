from app.Job import Job
from genetic.Schedule import Schedule

jobs = [
    # Job: C, Duration: 20, Prerequisites: ['A'], Resources: ['r1', 'r2']
    Job('A', 50),
    Job('B', 7),
    Job('C', 20, ['A'], ["r1", "r2"]),
    Job('D', 4, ['C']),
    Job('E', 31, ['B'], ["r3"]),
]
new_jobs = []

for job in jobs:
    if job.is_capacity_exceeded():
        divided_jobs = job.divide_job()
        if divided_jobs:
            new_jobs.extend(divided_jobs)

#add new jobs to jobs list
jobs.extend(new_jobs)

def encode_schedule(jobs):
    # Flatten the list of jobs into a dictionary for easy access
    job_dict = {job.name: job for job in jobs}

    # Initialize an empty schedule
    schedule = []

    # Iterate through jobs and add them to the schedule in a valid order
    for job in jobs:
        if all(prerequisite in schedule for prerequisite in job.prerequisites):
            schedule.append(job.name)

    return schedule

for job in jobs:
    print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}")
print("Schedule: ", encode_schedule(jobs))