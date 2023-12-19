# import random
# import string

# def add_colors_to_jobs(jobs, results):
#     # Create a dictionary to store colors for jobs
#     job_colors = {}

#     # Helper function to generate random color code
#     def generate_random_color():
#         return ''.join(random.choices(string.hexdigits[:-6], k=6))

#     # Helper function to get the color for a job considering prerequisites
#     def get_color_for_job(job_name):
#         if '.' in job_name:
#             base_job_name = job_name.split('.')[0]
#             if base_job_name in job_colors:
#                 return job_colors[base_job_name]
#         elif job_name in job_colors:
#             return job_colors[job_name]

#         return None

#     # Assign random colors to jobs
#     for job in jobs:
#         job_name = job['name']
#         if job_name not in job_colors:
#             color = generate_random_color()
#             job_colors[job_name] = color

#     # Update colors based on prerequisites
#     for _ in range(len(jobs)):
#         for job in jobs:
#             job_name = job['name']
#             color = get_color_for_job(job_name)
#             prerequisites = job.get('prerequisites', '').split(',')
#             prerequisite_colors = [job_colors[p] for p in prerequisites if p in job_colors]

#             if color is None and all(prerequisite_colors):
#                 color = prerequisite_colors[0]
#                 job_colors[job_name] = color

#     # Add color information to the results
#     for result in results:
#         job_name = result['name']
#         color = get_color_for_job(job_name)
#         if color:
#             result['color'] = color

#     return results

# # Example usage
# jobs = [
#     {'name': '1', 'duration': 10.0, 'machine': '', 'prerequisites': ''},
#     {'name': '2', 'duration': 25.0, 'machine': '', 'prerequisites': '1'},
#     {'name': '3', 'duration': 15.0, 'machine': '', 'prerequisites': '1'}
# ]

# results = [
#     {'name': '1', 'start_time': 0, 'end_time': 10.0, 'machine': 2},
#     {'name': '2', 'start_time': 10.0, 'end_time': 15.0, 'machine': 1},
#     {'name': '3', 'start_time': 15.0, 'end_time': 30.0, 'machine': 1},
#     {'name': '2.2', 'start_time': 15.0, 'end_time': 35.0, 'machine': 0}
# ]

# results_with_colors = add_colors_to_jobs(jobs, results)
# print(results_with_colors)




##############################
##############################
##############################
##############################
##############################


import matplotlib.pyplot as plt

def add_colors_to_jobs(jobs, results):
    # Create a dictionary to store colors for each job
    job_colors = {}

    # Assign unique colors to jobs with no dependencies
    color_index = 0
    for job in jobs:
        if job['prerequisites'] == '':
            job_colors[job['name']] = plt.cm.get_cmap('tab10')(color_index)
            color_index += 1

    # Assign colors to jobs based on dependencies
    for job in jobs:
        if job['prerequisites'] != '':
            prerequisites = job['prerequisites'].split(',')
            job_color = None
            for prereq in prerequisites:
                if prereq in job_colors:
                    job_color = job_colors[prereq]
                    break
            if job_color is None:
                job_color = plt.cm.get_cmap('tab10')(color_index)
                color_index += 1
            job_colors[job['name']] = job_color

    # Add colors to results
    results_with_colors = []
    for result in results:
        result_copy = result.copy()
        job_name = result_copy['name']
        if job_name in job_colors:
            color_hex = '#{:02x}{:02x}{:02x}'.format(
                int(job_colors[job_name][0] * 255),
                int(job_colors[job_name][1] * 255),
                int(job_colors[job_name][2] * 255)
            )
            result_copy['color'] = color_hex
        else:
            # Assign a default color if job not found in job_colors
            result_copy['color'] = '#000000'  # Black color
        results_with_colors.append(result_copy)

    # Assign same color to dependent job '2.2' as its prerequisite '2'
    for result in results_with_colors:
        if result['name'] == '2.2':
            for dependent_job in results_with_colors:
                if dependent_job['name'] == '2':
                    result['color'] = dependent_job['color']

    return results_with_colors

# Your existing data
jobs = [
    {'name': '1', 'duration': 10.0, 'machine': '', 'prerequisites': ''},
    {'name': '2', 'duration': 25.0, 'machine': '', 'prerequisites': ''},
    {'name': '3', 'duration': 15.0, 'machine': '', 'prerequisites': '1'},
    {'name': '4', 'duration': 15.0, 'machine': '', 'prerequisites': '3'}
]

results = [
    {'name': '1', 'start_time': 0, 'end_time': 10.0, 'machine': 2},
    {'name': '2', 'start_time': 10.0, 'end_time': 15.0, 'machine': 1},
    {'name': '3', 'start_time': 15.0, 'end_time': 30.0, 'machine': 1},
    {'name': '2.2', 'start_time': 15.0, 'end_time': 35.0, 'machine': 0},
    {'name': '4', 'start_time': 15.0, 'end_time': 30.0, 'machine': 1}
]

# Adding colors to jobs based on dependencies
results_with_colors = add_colors_to_jobs(jobs, results)
print(results_with_colors)




