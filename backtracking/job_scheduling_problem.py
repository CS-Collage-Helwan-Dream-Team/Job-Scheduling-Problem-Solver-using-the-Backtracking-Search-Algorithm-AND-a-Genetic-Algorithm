from backtracking.models.resource import Resource
class JobSchedulingProblem:
    def __init__(self, jobs, resources=None):
        self.jobs = jobs
        random_res=Resource.generate_random_resources()
        self.resources = resources if resources is not None else random_res
