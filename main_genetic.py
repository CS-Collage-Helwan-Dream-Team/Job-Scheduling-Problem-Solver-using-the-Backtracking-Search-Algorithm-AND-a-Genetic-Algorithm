from app.Job import Job
from genetic.Schedule import Schedule
from app.config import MACHINE_CAPACITY,NUM_MACHINES,MAX_GENERATIONS,POPULATION_SIZE,MUTATION_RATE
import random

def calc_fitness(full_schedules):
    #calculate fitness for each schedule
    for full_schedule in full_schedules:
        full_schedule.fitness = Schedule.calculate_max_end_time(Schedule.assign_jobs_to_machines(full_schedule,jobs))
    

# Your existing code
jobs = [
    Job('1', 60,),
    Job('2', 50,['1']),
    Job('3', 3,['1']),
    Job('4', 5),
    Job('5', 4,['2'], "r1"),
    Job('6', 15),
    Job('7', 23),
    Job('8', 16),
    Job('9', 1),
    Job('10', 23),
    Job('11', 17),
    Job('12', 7),
    Job('13', 3),
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




# result_schedule = Schedule.assign_jobs_to_machines(full_schedules[0],jobs)
# for item in result_schedule:
#     print(item)

best_schedules_after_crossove=[]
population = Schedule.generate_random_schedules_and_encoding(jobs)
for i in range (MAX_GENERATIONS):
    if i==0:
        #calculate fitness for each schedule
        calc_fitness(population)
        #sort schedules by fitness
        population.sort(key=lambda x: x.fitness)
        #select best schedules
        best_schedules = population[:int(POPULATION_SIZE/2)]
        #crossover
        best_schedules_after_crossover = Schedule.crossovers(best_schedules)
    else:
        #calculate fitness for each schedule
        calc_fitness(best_schedules_after_crossover)
        #sort schedules by fitness
        best_schedules_after_crossover.sort(key=lambda x: x.fitness)
        #select best schedules
        best_schedules = best_schedules_after_crossover[:int(POPULATION_SIZE/2)]
        #crossover
        best_schedules_after_crossover = Schedule.crossovers(best_schedules)
    

#print the best schedule after crossover
print("################### Schedule: #####################")
for item in population:
    print('fitness: ',item.fitness, 'schedule: ',item.encode)
#print the best schedule after crossover
print("################### Best Schedule: #####################")
calc_fitness(best_schedules_after_crossover)
for item in best_schedules_after_crossover:
    print('fitness: ',item.fitness, 'schedule: ',item.encode)