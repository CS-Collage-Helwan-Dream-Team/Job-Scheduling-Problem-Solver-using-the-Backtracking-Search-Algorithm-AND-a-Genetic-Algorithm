from genetic.Job import Job
from genetic.Schedule import Schedule
from app.config import MACHINE_CAPACITY,NUM_MACHINES




# Your existing code
jobs = [
    Job('1', 60,),
    Job('2', 50,['1']),
    Job('3', 4,['2'], "r1"),
]

max_time = MACHINE_CAPACITY * NUM_MACHINES
total_job_time = Job.TOTAL_TIME
if max_time < total_job_time:
    print("Total time of jobs exceeded the available ")

Job.handle_split_dependencies(jobs)

print("################### New Jobs: #####################")
for job in jobs:
    print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}")
print("###################  #####################")

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

