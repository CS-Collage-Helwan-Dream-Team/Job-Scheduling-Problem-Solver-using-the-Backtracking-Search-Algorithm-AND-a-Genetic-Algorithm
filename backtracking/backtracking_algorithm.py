class BacktrackingAlgorithm:
    def __init__(self, problem_instance):
        self.problem_instance = problem_instance
        self.best_schedule = None

    def is_valid_schedule(self, schedule):
        resource_occupancy = {resource.resource_id: 0 for resource in self.problem_instance.resources}

        for job, resource in schedule:
            if resource_occupancy[resource.resource_id] + job.processing_time > resource.capacity:
                return False

            if job.requiredResource_id is not None and resource.resource_id != job.requiredResource_id:
                return False

            if job.dependency is not None and job.dependency not in [j.job_id for j, _ in schedule]:
                return False

            resource_occupancy[resource.resource_id] += job.processing_time

        return True

    def backtrack(self, schedule, remaining_jobs):
        if not remaining_jobs:
            if self.is_valid_schedule(schedule):
                if self.best_schedule is None or len(schedule) < len(self.best_schedule):
                    self.best_schedule = schedule.copy()
            return

        current_job = remaining_jobs[0]

        for resource in self.problem_instance.resources:
            new_schedule = schedule.copy()
            new_schedule.append((current_job, resource))

            new_remaining_jobs = remaining_jobs[1:]
            self.backtrack(new_schedule, new_remaining_jobs)

    def solve(self):
        initial_schedule = []
        remaining_jobs = self.problem_instance.jobs.copy()
        self.backtrack(initial_schedule, remaining_jobs)

        if self.best_schedule:
   
            return self.display_schedule()
        else:
            print("No valid schedule found.")

     #method to get prerequisite finish time
    def get_prerequisite_finish_time(job, schedule):
            if not job.dependency:
                return 0

            max_time = 0
            for s in schedule:
                if s[0] == job.dependency:
                     max_time = max(max_time, s[3])

            return max_time
    def display_schedule(self):
        
        #///////////////////////////////
        #calc machine finish time
        machine_finish_times = {machine_number: 0 for machine_number in set(job[1].resource_id for job in self.best_schedule)}
        #print machine finish times
        print(machine_finish_times)
        schedule_best=self.best_schedule.copy()
        #sort jobs by number of prerequisites and check if none
        schedule_best.sort(key=lambda x: len(x[0].dependency) if x[0].dependency else 0)
        #split the jobs into two arrays, one with prerequisites and one without
        jobs_with_prerequisites = [job for job in schedule_best if job[0].dependency]
        jobs_without_prerequisites = [job for job in schedule_best if not job[0].dependency]
        #sort jobs with prerequisites by prerequisite float number
        jobs_with_prerequisites.sort(key=lambda x: float(x[0].dependency))
        #merge the two arrays
        schedule_best =  jobs_without_prerequisites +jobs_with_prerequisites
        result_schedule = []
        schedule=[]
        for job in schedule_best:
            start_time = max(machine_finish_times[job[1].resource_id], BacktrackingAlgorithm.get_prerequisite_finish_time(job[0], schedule))
            end_time = start_time + job[0].processing_time
            schedule.append((job[0].job_id, job[1].resource_id, start_time, end_time))
            machine_finish_times[job[1].resource_id] = end_time
            result_schedule.append({"name":job[0].job_id, "start_time":start_time, "end_time":end_time,"machine":job[1].resource_id})

        return result_schedule
            # result_schedule.append(f"Job: {job.name}, Machine: {job.machine_number}, Start Time: {start_time}, End Time: {end_time}")
        #////////////////////////////////
       
        # for assignment in self.best_schedule:
        #     job = assignment[0]
        #     resource = assignment[1]

        #     # Calculate the start time considering dependencies
        #     dependency_start_time = job_start_times[job.dependency] if job.dependency is not None else 0
        #     start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)

        #     end_time = start_time + job.processing_time
        #     resource_occupancy[resource.resource_id] = end_time
        #     job_start_times[job.job_id] = end_time
        #     jobs_start_time[job.job_id] = start_time

        # for assignment in self.best_schedule:
        #     job = assignment[0]
        #     resource = assignment[1]

        #     if(not job.dependency): continue
        #     dependency_start_time = job_start_times[job.dependency] if job.dependency is not None else 0
        #     start_time = max(resource_occupancy[resource.resource_id], dependency_start_time)

        #     end_time = start_time + job.processing_time
        #     resource_occupancy[resource.resource_id] = end_time
        #     job_start_times[job.job_id] = end_time
        #     jobs_start_time[job.job_id] = start_time

        # for assignment in self.best_schedule:
        #     job = assignment[0]
        #     resource = assignment[1]
        #     start_time = jobs_start_time[job.job_id]
        #     end_time = start_time + job.processing_time
        #     jobs.append({"name":job.job_id, "start_time":start_time, "end_time":end_time,"machine":resource.resource_id})

        
        
        # return jobs

