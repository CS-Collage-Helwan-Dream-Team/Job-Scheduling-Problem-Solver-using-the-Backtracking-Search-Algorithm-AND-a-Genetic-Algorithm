import random

from app.config import POPULATION_SIZE,MUTATION_RATE
from DataModels.FullSchedule import FullSchedule
from app import Job

class Schedule:
    NUM_MACHINES=0
    jobs_with_resources = []
    jobs=[]
    def __init__(self,NUM_MACHINES, jobs):
        Schedule.NUM_MACHINES= NUM_MACHINES
        Schedule.jobs = jobs
    def generate_random_schedules_and_encoding(jobs):
        
        # schedules = []
        full_schedule = []
        for _ in range(POPULATION_SIZE):
            encode = []
            for job in jobs:
                if job.resources or job.resources == 0:
                    machine = int(job.resources)
                    #check if the job has not been added to the jobs_with_resources list
                    if job not in Schedule.jobs_with_resources:
                        Schedule.jobs_with_resources.append(job)
                    encode.append(machine)
                else:
                    rand= random.randint(0, Schedule.NUM_MACHINES - 1)
                    encode.append(rand)
            # schedules.append(encode)
            full_schedule.append(FullSchedule(encode, -1))
        return full_schedule
        
    def decode_schedule(schedule, jobs):
        decoded_schedule = []
        for i,machine in enumerate(schedule):
            jobs[i].machine_number = machine
            decoded_schedule.append(jobs[i])
            
        return decoded_schedule

    def check_if_job_has_resources(job_name):
        for job in Schedule.jobs_with_resources:
            if job.name == job_name:
                return True
        return False

    def assign_jobs_to_machines(FullSchedule: FullSchedule, jobslist):

        jobs = Schedule.decode_schedule(FullSchedule.encode,jobslist)
        schedule = []
        machine_finish_times = {machine_number: 0 for machine_number in set(job.machine_number for job in jobs)}
    
        #sort jobs by number of prerequisites
        jobs.sort(key=lambda x: len(x.prerequisites))
        #split the jobs into two arrays, one with prerequisites and one without
        jobs_with_prerequisites = [job for job in jobs if job.prerequisites]
        jobs_without_prerequisites = [job for job in jobs if not job.prerequisites]
        #sort jobs with prerequisites by prerequisite float number asinding
        jobs_with_prerequisites.sort(key=lambda x: float(x.prerequisites[0]))
        #merge the two arrays
        jobs =  jobs_without_prerequisites +jobs_with_prerequisites 

        result_schedule = []
        

        for job in jobs:
            start_time = max(machine_finish_times[job.machine_number], Schedule.get_prerequisite_finish_time(job, schedule))
            end_time = start_time + job.duration
            schedule.append((job.name, job.machine_number, start_time, end_time))
            machine_finish_times[job.machine_number] = end_time
            result_schedule.append({"name":job.name, "start_time":start_time, "end_time":end_time,"machine":job.machine_number})
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
    
    def __crossover(parent1, parent2):
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        return child1, child2
    def __mutate(child):
        mutate_point = random.randint(0, len(child) - 1)
        decoded_child = Schedule.decode_schedule(child, Schedule.jobs)
        if Schedule.check_if_job_has_resources(decoded_child[mutate_point].name):
            child[mutate_point] = decoded_child[mutate_point].resources
        else:
            child[mutate_point] = random.randint(0, Schedule.NUM_MACHINES - 1)
        return child
    def crossovers_mutations(full_schedule: [FullSchedule]):
        after_crossover = []
        for _ in range(len(full_schedule)):
            parent1 = random.choice(full_schedule)
            parent2 = random.choice(full_schedule)
            child1, child2 = Schedule.__crossover(parent1.encode, parent2.encode)
            random_number = random.random()
            if random_number < MUTATION_RATE:
                after_crossover.append(FullSchedule(Schedule.__mutate(child1), -1))
                after_crossover.append(FullSchedule(Schedule.__mutate(child2), -1))
            else:
                after_crossover.append(FullSchedule(child1, -1))
                after_crossover.append(FullSchedule(child2, -1))
        #sort schedules by fitness
        return after_crossover
        

