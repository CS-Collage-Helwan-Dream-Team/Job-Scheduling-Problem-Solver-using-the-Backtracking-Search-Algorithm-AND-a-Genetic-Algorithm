from app.config import MACHINE_CAPACITY, NUM_MACHINES

class BacktrackingAlgorithm:
    def __init__(self, jobs):
        self.jobs = jobs
        self.best_schedule = None

    def is_valid_schedule(self, schedule):
        # resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}

        self.print_schedule(schedule)
        for job, resource_id in schedule:
            # Check Resource Capacity
            # if resource_occupancy[resource.resource_id] + job.processing_time > resource.capacity:
            #     return False

            # Check if the job can only run on a specific resource
            if job.resources is not None and resource_id != job.resources:
                return False

            # Check job dependencies
            if job.prerequisites is not None and job.prerequisites not in [j.job_id for j, _ in schedule]:
                return False

            # Update Resource Occupancy
            # resource_occupancy[resource.resource_id] += job.processing_time

        return True

    def backtrack(self, schedule, remaining_jobs):
        if not remaining_jobs:
            if self.is_valid_schedule(schedule):
                if self.best_schedule is None or len(schedule) < len(self.best_schedule):
                    self.best_schedule = schedule.copy()
            return

        current_job = remaining_jobs[0]

        for id in range(MACHINE_CAPACITY):
            new_schedule = schedule.copy()
            new_schedule.append((current_job, id))

            new_remaining_jobs = remaining_jobs[1:]
            self.backtrack(new_schedule, new_remaining_jobs)

    def solve(self):
        initial_schedule = []
        remaining_jobs = self.jobs.copy()
        self.backtrack(initial_schedule, remaining_jobs)
        if self.best_schedule:
            self.print_schedule(self.best_schedule)
        else:
            print("No valid schedule found.")

        # if self.best_schedule:
        #     self.display_schedule()
        # else:
        #     print("No valid schedule found.")

    # def display_schedule(self):
    #     print("Optimal Schedule:")
    #     job_start_times = {job.name: 0 for job in self.jobs}

    #     for assignment in self.best_schedule:
    #         job = assignment[0]
    #         resource = assignment[1]

    #         # Calculate the start time considering dependencies
    #         dependency_start_time = job_start_times[job.prerequisites] if job.prerequisites is not None else 0
    #         start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)

    #         end_time = start_time + job.processing_time

    #         print(f"Job {job.job_id} scheduled on Resource {resource.resource_id} "
    #             f"Start Time: {start_time}, End Time: {end_time}")

    #         # Update Resource Occupancy and Job Start Times
    #         resource_occupancy[resource.resource_id] = end_time
    #         job_start_times[job.job_id] = end_time
    def print_schedule(self, schedule):
        for job, machine_number in schedule:
            start_time = sum(j.duration for j, m in schedule if m == machine_number)
            end_time = start_time + job.duration
            print(f"Name: {job.name}, Machine Number: {machine_number}, Start Time: {start_time}, End Time: {end_time}")



