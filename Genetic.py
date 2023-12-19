from app.Job import Job
from genetic.Schedule import Schedule
from app.config import POPULATION_SIZE, MAX_GENERATIONS

class Genetic:
    MACHINE_CAPACITY = 0
    jobs = [Job]
    def __init__(self):
        pass
    def add_jobs(jobs):
        Genetic.jobs=[]
        for job in jobs:
            Genetic.jobs.append(Job(job['name'],job['duration'],[job['prerequisites']] if job['prerequisites']!='' else [],job['machine']))

    def run(MACHINE_CAPACITY,num_machines):
        Job.handle_split_dependencies(Genetic.jobs,MACHINE_CAPACITY)
        # print("################### New Jobs: #####################")
        # for job in Genetic.jobs:
        #     print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}")
        best_schedules_after_crossover=[]
        Schedule(num_machines)
        population = Schedule.generate_random_schedules_and_encoding(Genetic.jobs)
        for i in range (MAX_GENERATIONS):
            if i==0:
                #calculate fitness for each schedule
                Genetic.__calc_fitness(population)
                #sort schedules by fitness
                population.sort(key=lambda x: x.fitness)
                #select best schedules
                best_schedules = population[:int(POPULATION_SIZE/2)]
                #crossover
                best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
            else:
                #calculate fitness for each schedule
                Genetic.__calc_fitness(best_schedules_after_crossover)
                #sort schedules by fitness
                best_schedules_after_crossover.sort(key=lambda x: x.fitness)
                #select best schedules
                best_schedules = best_schedules_after_crossover[:int(POPULATION_SIZE/2)]
                #crossover
                best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
            
        Genetic.__calc_fitness(best_schedules_after_crossover)
        best_schedule_decoded=Schedule.assign_jobs_to_machines(best_schedules_after_crossover[0],Genetic.jobs)


        return best_schedule_decoded
            

    def __calc_fitness(full_schedules):
        #calculate fitness for each schedule
        for full_schedule in full_schedules:
            full_schedule.fitness = Schedule.calculate_max_end_time(Schedule.assign_jobs_to_machines(full_schedule,Genetic.jobs))
        full_schedules.sort(key=lambda x: x.fitness)
        

    # # # Your existing code

    # # jobs = [
    # #     Job('1', 60,),
    # #     Job('2', 50,['1']),
    # #     Job('3', 3,['1']),
    # #     Job('4', 5),
    # #     Job('5', 4,[2], "1"),
    # #     Job('6', 15),
    # #     Job('7', 23),
    # #     Job('8', 16),
    # #     Job('9', 1),
    # #     Job('10', 23),
    # #     Job('11', 60,['4'],2),
    # #     Job('12', 7),
    # #     Job('13', 3),
    # # ]

    # max_time = MACHINE_CAPACITY * NUM_MACHINES
    # total_job_time = Job.TOTAL_TIME
    # if max_time < total_job_time:
    #     print("Total time of jobs exceeded the available")

    # Job.handle_split_dependencies(jobs)


    # print("###################  #####################")


    # best_schedules_after_crossove=[]
    # population = Schedule.generate_random_schedules_and_encoding(jobs)
    # for i in range (MAX_GENERATIONS):
    #     if i==0:
    #         #calculate fitness for each schedule
    #         __calc_fitness(population)
    #         #sort schedules by fitness
    #         population.sort(key=lambda x: x.fitness)
    #         #select best schedules
    #         best_schedules = population[:int(POPULATION_SIZE/2)]
    #         #crossover
    #         best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
    #     else:
    #         #calculate fitness for each schedule
    #         __calc_fitness(best_schedules_after_crossover)
    #         #sort schedules by fitness
    #         best_schedules_after_crossover.sort(key=lambda x: x.fitness)
    #         #select best schedules
    #         best_schedules = best_schedules_after_crossover[:int(POPULATION_SIZE/2)]
    #         #crossover
    #         best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
        


    # #print the best schedule after crossover
    # print("################### Best Schedule: #####################")
    # __calc_fitness(best_schedules_after_crossover)
    # best_schedule=best_schedules_after_crossover[0]
    # best_schedule_decoded=Schedule.assign_jobs_to_machines(best_schedules_after_crossover[0],jobs)

    # print('fitness: ',best_schedule.fitness, 'schedule: ',best_schedule.encode)

    # print("###################  #####################")
    # for item in best_schedule_decoded:
    #     print('Job: ',item['name'], 'Machine: ',item['machine_number'], 'Start Time: ',item['start_time'], 'End Time: ',item['end_time'])
        



    
    


jobss=[
    {'name': '1', 'duration': 60, 'machine': 1, 'prerequisites': ''},
    {'name': '2', 'duration': 50, 'machine': 1, 'prerequisites': '1'},
    {'name': '3', 'duration': 3, 'machine': 1, 'prerequisites': '1'},
    {'name': '4', 'duration': 5, 'machine': 1, 'prerequisites': ''},
    {'name': '5', 'duration': 4, 'machine': 2, 'prerequisites': '2'},
    {'name': '6', 'duration': 15, 'machine': 2, 'prerequisites': ''},
    {'name': '7', 'duration': 23, 'machine': 2, 'prerequisites': ''},
    {'name': '8', 'duration': 16, 'machine': 2, 'prerequisites': ''},
    {'name': '9', 'duration': 1, 'machine': 2, 'prerequisites': ''},
    {'name': '10', 'duration': 23, 'machine': 2, 'prerequisites': ''},
    {'name': '11', 'duration': 60, 'machine': 2, 'prerequisites': '4'},
    {'name': '12', 'duration': 7, 'machine': 2, 'prerequisites': ''},
    {'name': '13', 'duration': 3, 'machine': 2, 'prerequisites': ''},
]







