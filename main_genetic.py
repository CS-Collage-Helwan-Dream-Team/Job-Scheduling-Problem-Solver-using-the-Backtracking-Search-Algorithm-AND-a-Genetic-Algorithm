from app.Job import Job
from genetic.Schedule import Schedule


class Genetic:
    MACHINE_CAPACITY,NUM_MACHINES,MAX_GENERATIONS,POPULATION_SIZE =0
    def __init__
    def __calc_fitness(full_schedules):
        #calculate fitness for each schedule
        for full_schedule in full_schedules:
            full_schedule.fitness = Schedule.calculate_max_end_time(Schedule.assign_jobs_to_machines(full_schedule,jobs))
        full_schedules.sort(key=lambda x: x.fitness)
        

    # Your existing code

    jobs = [
        Job('1', 60,),
        Job('2', 50,['1']),
        Job('3', 3,['1']),
        Job('4', 5),
        Job('5', 4,[2], "1"),
        Job('6', 15),
        Job('7', 23),
        Job('8', 16),
        Job('9', 1),
        Job('10', 23),
        Job('11', 60,['4'],2),
        Job('12', 7),
        Job('13', 3),
    ]

    max_time = MACHINE_CAPACITY * NUM_MACHINES
    total_job_time = Job.TOTAL_TIME
    if max_time < total_job_time:
        print("Total time of jobs exceeded the available")

    Job.handle_split_dependencies(jobs)

    print("################### New Jobs: #####################")
    for job in jobs:
        print(f"Job: {job.name}, Duration: {job.duration}, Prerequisites: {job.prerequisites}, Resources: {job.resources}")
    print("###################  #####################")


    best_schedules_after_crossove=[]
    population = Schedule.generate_random_schedules_and_encoding(jobs)
    for i in range (MAX_GENERATIONS):
        if i==0:
            #calculate fitness for each schedule
            __calc_fitness(population)
            #sort schedules by fitness
            population.sort(key=lambda x: x.fitness)
            #select best schedules
            best_schedules = population[:int(POPULATION_SIZE/2)]
            #crossover
            best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
        else:
            #calculate fitness for each schedule
            __calc_fitness(best_schedules_after_crossover)
            #sort schedules by fitness
            best_schedules_after_crossover.sort(key=lambda x: x.fitness)
            #select best schedules
            best_schedules = best_schedules_after_crossover[:int(POPULATION_SIZE/2)]
            #crossover
            best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
        


    #print the best schedule after crossover
    print("################### Best Schedule: #####################")
    __calc_fitness(best_schedules_after_crossover)
    best_schedule=best_schedules_after_crossover[0]
    best_schedule_decoded=Schedule.assign_jobs_to_machines(best_schedules_after_crossover[0],jobs)

    print('fitness: ',best_schedule.fitness, 'schedule: ',best_schedule.encode)

    print("###################  #####################")
    for item in best_schedule_decoded:
        print('Job: ',item['name'], 'Machine: ',item['machine_number'], 'Start Time: ',item['start_time'], 'End Time: ',item['end_time'])
        








    
    









