

class Job:
    TOTAL_TIME = 0
    machine_number=-1
    def __init__(self, name, duration, prerequisites=None, resources=None):
        self.name = name
        self.duration = duration
        self.prerequisites = prerequisites if prerequisites is not None else []
        self.resources = resources if resources is not None else []
        Job.TOTAL_TIME += duration

    def is_capacity_exceeded(self,MACHINE_CAPACITY):
        return self.duration > MACHINE_CAPACITY

    def divide_job(self,MACHINE_CAPACITY):
        divided_jobs = []
        part_number = 2  # Start parts from 2
        while self.is_capacity_exceeded(MACHINE_CAPACITY):
            remaining_duration = self.duration
            if remaining_duration <= MACHINE_CAPACITY:
                divided_jobs.append(Job(f"{self.name}.{part_number}", remaining_duration, [f"{self.name}.{part_number - 1}"],
                                        self.resources))
                break

            new_duration = min(remaining_duration, MACHINE_CAPACITY)
            if divided_jobs:
                divided_jobs.append(Job(f"{self.name}.{part_number}", new_duration,
                                        [f"{self.name}.{part_number - 1}"], self.resources))
            else:
                divided_jobs.append(Job(f"{self.name}.{part_number}", new_duration, [self.name], self.resources))
            self.duration -= new_duration
            part_number += 1
        return divided_jobs if divided_jobs else None

    @staticmethod
    def handle_split_dependencies(jobs,MACHINE_CAPACITY):
        new_jobs = []
        for job in jobs:
            if job.is_capacity_exceeded(MACHINE_CAPACITY):
                divided_jobs = job.divide_job(MACHINE_CAPACITY)
                if divided_jobs:
                    new_jobs.extend(divided_jobs)
                    # Check if there are dependencies on the original job
                    for dependent_job in jobs:
                        if job.name in dependent_job.prerequisites:
                            dependent_job.prerequisites.remove(job.name)
                            dependent_job.prerequisites.append(divided_jobs[-1].name)  # Add the last split part as a prerequisite

        jobs.extend(new_jobs)