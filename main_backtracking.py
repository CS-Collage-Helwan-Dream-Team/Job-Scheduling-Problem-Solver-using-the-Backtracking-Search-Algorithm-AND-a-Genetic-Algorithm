from backtracking.models.resource import Resource
from backtracking.models.job import Job
from backtracking.models.job_scheduling_problem import JobSchedulingProblem
from backtracking.backtracking_algorithm import BacktrackingAlgorithm

# Define the job scheduling problem instance
jobs = [
    Job(1, 1),
    Job(2, 5, dependency=1, requiredResource_id=1),
    Job(3, 1, dependency=2, requiredResource_id=1),
    Job(4, 4, dependency=3),
    Job(5, 1, dependency=3, requiredResource_id=2),
    # Job(6, 1, dependency=3),
    # Job(7, 1, dependency=3),
    # Job(8, 1, dependency=3),
    # Job(9, 1, dependency=3),
    # Job(10, 1, dependency=3),
]

resources = Resource.generate_random_resources()


# TODO: split the large jop to two or more if needed 
if(not Job.check_total_processing_time(jobs, resources)):
    print("Exceeded the total resource capacity")

[invalid_assigned_jobs_ids, resource_id] = Job.check_exceeded_require_resource_capacity(jobs, resources)

if(invalid_assigned_jobs_ids is not None):
    joined_ids = ', '.join(str(job_id) for job_id in invalid_assigned_jobs_ids)
    print(f"Warning: Total processing time for jobs {joined_ids} assigned to Resource {resource_id} exceeds its capacity.")

problem_instance = JobSchedulingProblem(jobs, resources)

# Create an instance of the BacktrackingAlgorithm and solve the problem
backtracking_algorithm = BacktrackingAlgorithm(problem_instance)
backtracking_algorithm.solve()
