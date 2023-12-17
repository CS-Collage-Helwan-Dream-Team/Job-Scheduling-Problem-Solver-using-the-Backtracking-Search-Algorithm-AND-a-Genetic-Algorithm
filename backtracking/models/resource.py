from app.config import MACHINE_CAPACITY,NUM_MACHINES
class Resource:
    def __init__(self, resource_id, capacity):
        self.resource_id = resource_id
        self.capacity = capacity

    def __str__(self):
        return f"Resource {self.resource_id} (Capacity: {self.capacity})"
    @staticmethod
    def generate_random_resources():
        resources = []
        for i in range(NUM_MACHINES):
            resources.append(Resource(i, MACHINE_CAPACITY))
        return resources