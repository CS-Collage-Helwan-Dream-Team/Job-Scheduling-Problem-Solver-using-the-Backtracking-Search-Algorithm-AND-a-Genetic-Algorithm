import random
from app.config import NUM_MACHINES, POPULATION_SIZE

class Schedule:
    def generate_random_schedules(jobs):
        schedules = []
        for _ in range(POPULATION_SIZE):
            schedule = [random.randint(0, NUM_MACHINES - 1) for _ in range(len(jobs))]
            schedules.append(schedule)
        return schedules