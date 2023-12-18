class Job:
    def __init__(self, job_id, processing_time, dependency=None, requiredResource_id=None):
        self.job_id = job_id
        self.processing_time = processing_time
        self.dependency = dependency
        self.requiredResource_id = requiredResource_id

    def __str__(self):
        return f"Job {self.job_id} (Processing Time: {self.processing_time}, Dependency: {self.dependency})"
    
    @staticmethod
    def check_total_processing_time(jobs, resources):
        total_processing_time = sum(job.processing_time for job in jobs)
        total_resource_capacity = sum(resource.capacity for resource in resources)
        if total_processing_time > total_resource_capacity:
            return  False
        return True
    
    @staticmethod
    def check_exceeded_require_resource_capacity(jobs, resources):
        for resource in resources:
            assigned_jobs = [job for job in jobs if job.requiredResource_id == resource.resource_id]
            total_processing_time = sum(job.processing_time for job in assigned_jobs)
            if total_processing_time > resource.capacity:
                return [[job.job_id for job in assigned_jobs ], resource.resource_id]

        return [None, None]
    
    @staticmethod
    def check_and_split_large_jobs(jobs, resources):
        max_capacity = max(resource.capacity for resource in resources)
        dependency_id_to_replace = []
        new_jobs = []
        for job in jobs:
            if job.processing_time > max_capacity:
                # Split the job into smaller ones
                num_splits = job.processing_time // max_capacity
                remainder = job.processing_time % max_capacity
                last_split_id = job.job_id

                for i in range(num_splits):
                    job_dependency =  job.dependency if i == 0 else f'{job.job_id}.{i-1}'
                    new_job = Job(job_id=f"{job.job_id}.{i+1}", processing_time=max_capacity,dependency=job_dependency, requiredResource_id=job.requiredResource_id)
                    new_jobs.append(new_job)
                    last_split_id = f"{job.job_id}.{i+1}"

                if remainder > 0:
                    # Create a last job with the remaining processing time
                    last_job = Job(job_id=f"{job.job_id}.{num_splits + 1}", processing_time=remainder,
                                    dependency=f"{job.job_id}.{num_splits}", requiredResource_id=job.requiredResource_id)
                    new_jobs.append(last_job)
                    last_split_id = f"{job.job_id}.{num_splits + 1}"
                
                dependency_id_to_replace.append((job.job_id, last_split_id))
            else:
                new_jobs.append(job)

        for job in new_jobs:
            for job_id, splitted_id in dependency_id_to_replace:
                if(job.dependency == job_id):
                    job.dependency = splitted_id

        return new_jobs