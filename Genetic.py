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
            Genetic.jobs.append(Job(job['name'],job['duration'],job['prerequisites'],job['machine']))
        

    def run(MACHINE_CAPACITY,num_machines):
        Job.handle_split_dependencies(Genetic.jobs,MACHINE_CAPACITY)
        best_schedules_after_crossover=[]
        Schedule(num_machines,Genetic.jobs)
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
                if(len(Genetic.jobs)!=1):
                    best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
                else:
                    best_schedules_after_crossover=best_schedules
            else:
                #calculate fitness for each schedule
                Genetic.__calc_fitness(best_schedules_after_crossover)
                #sort schedules by fitness
                best_schedules_after_crossover.sort(key=lambda x: x.fitness)
                #select best schedules
                best_schedules = best_schedules_after_crossover[:int(POPULATION_SIZE/2)]
                #crossover
                if(len(Genetic.jobs)!=1):
                    best_schedules_after_crossover = Schedule.crossovers_mutations(best_schedules)
                else:
                    best_schedules_after_crossover=best_schedules
            
        Genetic.__calc_fitness(best_schedules_after_crossover)
        best_schedule_decoded=Schedule.assign_jobs_to_machines(best_schedules_after_crossover[0],Genetic.jobs)
        

        return best_schedule_decoded
            

    def __calc_fitness(full_schedules):
        #calculate fitness for each schedule
        for full_schedule in full_schedules:
            full_schedule.fitness = Schedule.calculate_max_end_time(Schedule.assign_jobs_to_machines(full_schedule,Genetic.jobs))
        full_schedules.sort(key=lambda x: x.fitness)
        

  


    
    






