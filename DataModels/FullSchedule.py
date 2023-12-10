from DataModels.ScheduledJob import ScheduledJop

class FullSchedule:
    jobs= list[ScheduledJop]
    max_end_time = int
    