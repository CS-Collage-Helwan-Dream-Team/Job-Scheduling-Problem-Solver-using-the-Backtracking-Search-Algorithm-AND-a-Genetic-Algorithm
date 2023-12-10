import random

from app.config import POPULATION_SIZE,NUM_MACHINES

class Schedule:
    
    def generate_random_schedules_and_encoding(jobs):
        schedules = []
        for _ in range(POPULATION_SIZE):
            schedule = []
            for job in jobs:
                if job.resources:
                    machine = int(job.resources.replace("r", "")) 
                    # FIXME: validate the resource number in our range in this example between 0 and 3
                    schedule.append(machine)
                else:
                    schedule.append(random.randint(0, NUM_MACHINES - 1))
            schedules.append(schedule)
        return schedules
        
    def decode_schedule(schedule, jobs):
        decoded_schedule = []
        for i,machine in enumerate(schedule):
            jobs[i].machine_number = machine
            decoded_schedule.append(jobs[i])
            
        return decoded_schedule




    def assign_jobs_to_machines(jobs):
        schedule = []
        machine_finish_times = {machine_number: 0 for machine_number in set(job.machine_number for job in jobs)}
    
        #sort jobs by number of prerequisites
        jobs.sort(key=lambda x: len(x.prerequisites))
        #split the jobs into two arrays, one with prerequisites and one without
        jobs_with_prerequisites = [job for job in jobs if job.prerequisites]
        jobs_without_prerequisites = [job for job in jobs if not job.prerequisites]
        #sort jobs with prerequisites by prerequisite float number descending
        jobs_with_prerequisites.sort(key=lambda x: float(x.prerequisites[0]))
        #merge the two arrays
        jobs =  jobs_without_prerequisites +jobs_with_prerequisites 

        result_schedule = []
        

        for job in jobs:
            start_time = max(machine_finish_times[job.machine_number], Schedule.get_prerequisite_finish_time(job, schedule))
            end_time = start_time + job.duration
            schedule.append((job.name, job.machine_number, start_time, end_time))
            machine_finish_times[job.machine_number] = end_time
            result_schedule.append({"name":job.name, "machine_number":job.machine_number, "start_time":start_time, "end_time":end_time})
            
            # result_schedule.append(f"Job: {job.name}, Machine: {job.machine_number}, Start Time: {start_time}, End Time: {end_time}")

        return result_schedule

    def get_prerequisite_finish_time(job, schedule):
        if not job.prerequisites:
            return 0

        max_time = 0
        for prereq in job.prerequisites:
            for s in schedule:
                if s[0] == prereq:
                    max_time = max(max_time, s[3])

        return max_time





    def calculate_max_end_time(schedule):
        max_end_time = max(job['end_time'] for job in schedule)
        return max_end_time
        

