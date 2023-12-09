from app.Job import Job
from genetic.Schedule import Schedule
from app.config import MACHINE_CAPACITY,NUM_MACHINES

jobs = [
    Job('A', 100),
    Job('B', 7),
    Job('C', 100, ['A'], "r0"),
    Job('D', 4, ['C']),
    Job('E', 31, ['B'], "r2"),
]
max_time = MACHINE_CAPACITY * NUM_MACHINES
totla_job_time= Job.TOTAL_TIME
if(max_time<totla_job_time):
    print("Total time of jobs exceeded the aviliable ")

new_jobs = []
for job in jobs:
    if job.is_capacity_exceeded():
        divided_jobs = job.divide_job()
        if divided_jobs:
            new_jobs.extend(divided_jobs)

jobs.extend(new_jobs)



decoded_jobs = Schedule.decode_schedule(Schedule.generate_random_schedules_and_encoding(jobs)[0],jobs)

result_schedule = Schedule.assign_jobs_to_machines(decoded_jobs)

for item in result_schedule:
    print(item)


# print("\nSchedule Table:")
# for i, job in enumerate(assign_jobs_to_machine(best_schedule_after_crossover[0]['schedule'], jobs, NUM_MACHINES)):
#     print(f"Job {job['job_name']} - Machine {job['machine_number']}: Start Time: {job['start_time']}, End Time: {job['end_time']}")

# print("################### After decode: #####################")
# for job in Schedule.decode_schedule(Schedule.generate_random_schedules_and_encoding(jobs)[0],jobs):
#     print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}, Machine: {job.machine_number}")



# print(new_jobs)

