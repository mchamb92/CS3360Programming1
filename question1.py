import random
import math

def custom_random(rate):
    return -math.log(1 - random.random()) / rate

def generate_sequence(total_procs, lambda_rate, mu_rate):
    procs = []
    current_time = 0
    for proc_id in range(total_procs):

        arrival_gap = custom_random(lambda_rate)
        current_time += arrival_gap

        service_duration = custom_random(mu_rate)
        procs.append((proc_id + 1, current_time, service_duration))
    return procs

total_procs_custom = 1000
lambda_rate_custom = 2  
mu_rate_custom = 1      
scheduled_processes_custom = generate_sequence(total_procs_custom, lambda_rate_custom, mu_rate_custom)

arrival_intervals_custom = [process[1] for process in scheduled_processes_custom]
durations_custom = [process[2] for process in scheduled_processes_custom]
real_arrival_rate_custom = total_procs_custom / (arrival_intervals_custom[-1] - arrival_intervals_custom[0])
average_duration_custom = sum(durations_custom) / len(durations_custom)

print("Process ID, Time of Arrival, Requested time of Service")
for process in scheduled_processes_custom:
    print(process)

print("\nCalculated average rate of arrival:", real_arrival_rate_custom)
print("Calculated average service duration:", average_duration_custom)
