from app.Job import Job
from genetic.Schedule import Schedule
from app.config import MACHINE_CAPACITY,NUM_MACHINES
from backtracking.backtracking_algorithm import BacktrackingAlgorithm

# Your existing code
jobs = [
    Job('1', 40,),
    Job('2', 50,['1']),
    Job('3', 4,['2'], 1),
]

max_time = MACHINE_CAPACITY * NUM_MACHINES
total_job_time = Job.TOTAL_TIME
if max_time < total_job_time:
    print("Total time of jobs exceeded the available ")

# دي اللي بتظبط الجوبات
Job.handle_split_dependencies(jobs)

# دا عرض مطبوع
print("################### New Jobs: #####################")
for job in jobs:
    print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}")

# هتكمل بال (jobs)
backtracking_algorithm = BacktrackingAlgorithm(jobs)
backtracking_algorithm.solve()