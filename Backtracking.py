from backtracking.models.resource import Resource
from backtracking.models.job import Job
from backtracking.models.job_scheduling_problem import JobSchedulingProblem
from backtracking.backtracking_algorithm import BacktrackingAlgorithm


class Backtracking:
    resources = [Resource]
    jobs = [Job]
    def __init__(self):
        pass
    def add_resources(machines,capacity):
        Backtracking.resources= Resource.generate_random_resources(machines,capacity)
    
    def add_jobs(jobs):
        Backtracking.jobs=[]
        for job in jobs:
            Backtracking.jobs.append(Job(job['name'],job['duration'],dependency=job['prerequisites'],requiredResource_id=job['machine']))
        print(Backtracking.jobs)
    
    def run():
        if(not Job.check_total_processing_time(Backtracking.jobs, Backtracking.resources)):
            print("Exceeded the total resource capacity")

        [invalid_assigned_jobs_ids, resource_id] = Job.check_exceeded_require_resource_capacity(Backtracking.jobs, Backtracking.resources)

        if(invalid_assigned_jobs_ids is not None):
            joined_ids = ', '.join(str(job_id) for job_id in invalid_assigned_jobs_ids)
            print(f"Warning: Total processing time for jobs {joined_ids} assigned to Resource {resource_id} exceeds its capacity.")

        preparedJobs = Job.check_and_split_large_jobs(Backtracking.jobs,Backtracking.resources)

        problem_instance = JobSchedulingProblem(preparedJobs, Backtracking.resources)

        # Create an instance of the BacktrackingAlgorithm and solve the problem
        backtracking_algorithm = BacktrackingAlgorithm(problem_instance)
        backtracking_algorithm.solve()


# # Define the job scheduling problem instance
# jobs = [
#     Job('1', 21),
#     Job('2', 5, requiredResource_id=2),
#     Job('3', 1, requiredResource_id=2),
#     Job('4', 4),
#     Job('5', 20, dependency='1'),
# ]




# if(not Job.check_total_processing_time(jobs, resources)):
#     print("Exceeded the total resource capacity")

# [invalid_assigned_jobs_ids, resource_id] = Job.check_exceeded_require_resource_capacity(jobs, resources)

# if(invalid_assigned_jobs_ids is not None):
#     joined_ids = ', '.join(str(job_id) for job_id in invalid_assigned_jobs_ids)
#     print(f"Warning: Total processing time for jobs {joined_ids} assigned to Resource {resource_id} exceeds its capacity.")

# preparedJobs = Job.check_and_split_large_jobs(jobs,resources)

# # for job in jobs:
# #     print(f'id: {job.job_id}, time: {job.processing_time}, depend: {job.dependency}, required: {job.requiredResource_id}')
# # for job in preparedJobs:
# #     print(f'id: {job.job_id}, time: {job.processing_time}, depend: {job.dependency}, required: {job.requiredResource_id}')

# problem_instance = JobSchedulingProblem(preparedJobs, resources)

# # Create an instance of the BacktrackingAlgorithm and solve the problem
# backtracking_algorithm = BacktrackingAlgorithm(problem_instance)
# backtracking_algorithm.solve()
