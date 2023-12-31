import tkinter as tk
import matplotlib.pyplot as plt
from Backtracking import Backtracking
from Genetic import Genetic
import numpy as np
import time
import random
from tkinter import messagebox
jobs = []
results = []
backtracking_execution_time=0.0
genetic_algorithm_execution_time=0.0
def validate(jobs):
        # add validation if 
    print(jobs)
    total_jobs_time=0

    for job in jobs:
        total_jobs_time += int(job['duration'])
    if(not capacity_entry.get() or not machines_entry.get()):
        messagebox.showerror("Error","please add the capacity and the number of machines")
        return False
    if(total_jobs_time==0):
        messagebox.showerror("Error","no jobs have been added")
        return False
    
    if(total_jobs_time> int(machines_entry.get()) * int(capacity_entry.get())):
        print(total_jobs_time)
        print(int(machines_entry.get()) * int(capacity_entry.get()))
        messagebox.showerror("Error","the total proccessing time of jobs exceeded the total capacity of resourses")
        return False
    
    
    
    return True
# start matplotlib code
def plot_timeline(jobs,title):

    
    fig, ax = plt.subplots()

    machines = {}
    for i, job in enumerate(jobs):
        machine = int(job['machine'])
        if machine not in machines:
            machines[machine] = []
        machines[machine].append((job['name'], job['start_time'], job['end_time'],job['color']))

    #get max machine number
    max_machine_number = max(int(machine) for machine in machines.keys())
    #add the missing machines to the bigest machine number
    for i in range(max_machine_number):
        if i not in machines:
            #append machine number with empty list
            machines[i] = []

    #sort machines by number
    machines = dict(sorted(machines.items(), key=lambda x: int(x[0])))

    yticks = []
    ylabels = []
    for i, (machine, job_list) in enumerate(machines.items()):
        yticks.append(i)
        ylabels.append(f"Machine {machine}")
        for j, (job_name, start_time, end_time,color) in enumerate(job_list):
             
            margin = 0.1
            duration = end_time - start_time
            ax.barh(i, duration, left=start_time + j * margin, height=0.5, align='center', color= color, alpha=0.7)
            ax.text((start_time + end_time) / 2, i, f"{job_name}\n{duration}", ha='center', va='center')


    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels)
    ax.set_xlabel('Time')
    ax.set_title(title)

    plt.show()

#start tkinter code
    
def add_job():
    job_name = job_entry.get()
    duration = float(duration_entry.get())
    machine = machine_entry.get()
    if(not job_name.isdigit()):
        messagebox.showerror("Error","job id must be number")
        return
    if(duration <= 0):
        messagebox.showerror("Error","duration must be bigger 0")
        return
    
    if(machine != ""):
        if(int(machine) >= int(machines_entry.get())):
            machine = None
        else:
            machine = machine

    else:
        machine = None
    prerequisites = prerequisites_entry.get()
    if(prerequisites or machine):
        if (duration > int(capacity_entry.get())):
            messagebox.showerror("Error","Can't add prerequisite or machine for job has duration bigger than machine capacity")
            return
    if (duration > int(capacity_entry.get())):
            messagebox.showerror("Warning","The time will be exceed the limit")
            

    jobs.append({'name': job_name, 'duration': duration, 'machine': machine, 'prerequisites': prerequisites})
    update_job_list()
    job_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)
    end_time_entry.delete(0, tk.END)
    machine_entry.delete(0, tk.END)
    prerequisites_entry.delete(0, tk.END)

def delete_job():
    selected = job_listbox.curselection()
    if selected:
        index = selected[0]
        del jobs[index]
        update_job_list()

def update_job_list():
    job_listbox.delete(0, tk.END)
    for job in jobs:
        job_listbox.insert(tk.END, f"{job['name']} - {job['duration']}  - Machine: {job['machine']} - Prerequisites: {job['prerequisites']}")

#add colors
def extract_base_job_name(job_name):
    # Extract the base job name (e.g., '2' from '2.2' or '1' from '1.2')
    split_name = job_name.split('.')
    return split_name[0]

def add_colors_to_jobs(jobs, results):
    # Create a dictionary to store colors for each job
    job_colors = {}

    # Assign unique colors to jobs with no dependencies
    color_index = 0
    for job in jobs:
        base_job_name = extract_base_job_name(job['name'])
        if base_job_name not in job_colors:
            job_colors[base_job_name] = plt.cm.get_cmap('tab10')(color_index)
            color_index += 1

    # Assign colors to jobs based on dependencies
    for job in jobs:
        base_job_name = extract_base_job_name(job['name'])
        if job['prerequisites'] != '':
            prerequisites = job['prerequisites'].split(',')
            job_color = None
            for prereq in prerequisites:
                prereq_base_name = extract_base_job_name(prereq)
                if prereq_base_name in job_colors:
                    job_color = job_colors[prereq_base_name]
                    break
            if job_color is None:
                job_color = plt.cm.get_cmap('tab10')(color_index)
                color_index += 1
            job_colors[base_job_name] = job_color

    # Add colors to results
    results_with_colors = []
    for result in results:
        result_copy = result.copy()
        job_name = extract_base_job_name(result_copy['name'])
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

    return results_with_colors


Backtracking()
def show_backtracking_timeline():
    if(not validate(jobs)):
        return
    Backtracking.add_resources(int(machines_entry.get()),int(capacity_entry.get()))
    
    #claculate execution time and memory space
    start_time = time.time()
    Backtracking.add_jobs(jobs)
    results = Backtracking.run()
    end_time = time.time()
    global backtracking_execution_time
    backtracking_execution_time = end_time - start_time
    if results is None:
        return
    plot_timeline(add_colors_to_jobs(jobs,results),f"Backtracking Timeline Execution Time: {backtracking_execution_time} s")
Genetic()
def show_genetic_timeline():
    if(not validate(jobs)):
        return
    Genetic.add_jobs(jobs)
    #claculate execution time and memory space
    start_time = time.time()
    results = Genetic.run(int(capacity_entry.get()),int(machines_entry.get()))
    end_time = time.time()
    global genetic_algorithm_execution_time
    genetic_algorithm_execution_time = end_time - start_time
    if results is None:
        return
    plot_timeline(add_colors_to_jobs(jobs,results),f"Genetic Timeline Execution Time: {genetic_algorithm_execution_time} s")


def show_plots ():
    print(backtracking_execution_time,genetic_algorithm_execution_time)
    plt.bar(['Backtracking', 'Genetic Algorithm'], [backtracking_execution_time, genetic_algorithm_execution_time])
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (s)')
    plt.title('Comparison of Execution Times between Backtracking and Genetic Algorithm')
    plt.show()
    ###############
    # plt.bar(['Backtracking', 'Genetic Algorithm'], [backtracking_memory_space, genetic_algorithm_memory_space])
    # plt.xlabel('Algorithms')
    # plt.ylabel('memory space')
    # plt.title('Comparison of memory space between Backtracking and Genetic Algorithm')
    # plt.show()
root = tk.Tk()
root.title("Job Schedule Timeline")

label_job = tk.Label(root, text="Job Name:")
label_job.grid(row=0, column=0, padx=10, pady=5)
job_entry = tk.Entry(root)
job_entry.grid(row=0, column=1, padx=10, pady=5)

label_duration = tk.Label(root, text="duration :")
label_duration.grid(row=1, column=0, padx=10, pady=5)
duration_entry = tk.Entry(root)
duration_entry.grid(row=1, column=1, padx=10, pady=5)

label_end_time = tk.Label(root, text="End Time:")
label_end_time.grid(row=2, column=0, padx=10, pady=5)
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=2, column=1, padx=10, pady=5)

label_machine = tk.Label(root, text="Machine:")
label_machine.grid(row=3, column=0, padx=10, pady=5)
machine_entry = tk.Entry(root)
machine_entry.grid(row=3, column=1, padx=10, pady=5)

label_prerequisites = tk.Label(root, text="Prerequisites:")
label_prerequisites.grid(row=2, column=0, padx=10, pady=5)
prerequisites_entry = tk.Entry(root)
prerequisites_entry.grid(row=2, column=1, padx=10, pady=5)

add_button = tk.Button(root, text="Add Job", command=add_job)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Job", command=delete_job)
delete_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

label_job_list = tk.Label(root, text="Current Jobs:")
label_job_list.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
job_listbox = tk.Listbox(root, width=40)
job_listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Machines Section
label_machines = tk.Label(root, text="Number of Machines:")
label_machines.grid(row=0, column=2, padx=10, pady=5)
machines_entry = tk.Entry(root)
machines_entry.grid(row=0, column=3, padx=10, pady=5)

label_capacity = tk.Label(root, text="Machines Capacity:")
label_capacity.grid(row=1, column=2, padx=10, pady=5)
capacity_entry = tk.Entry(root)
capacity_entry.grid(row=1, column=3, padx=10, pady=5)

show_plots_btn = tk.Button(root, text="show_plots", command=show_plots)
show_plots_btn.grid(row=6, column=3, columnspan=2, padx=10, pady=5)

show_button_genetic = tk.Button(root, text="Show genetic Timeline", command=show_genetic_timeline)
show_button_genetic.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

show_button_backtracking = tk.Button(root, text="Show backtracking Timeline", command=show_backtracking_timeline)
show_button_backtracking.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
