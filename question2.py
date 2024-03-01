import random
import math

def custom_exponential(rate):
    return -math.log(1 - random.random()) / rate

def fail_generate(mtbf, restore_time, years):
    total_hours = years * 365 * 24  # Total hours in 20 years
    failures = []
    current_time = 0
    while current_time < total_hours:

        next_failure = custom_exponential(1 / mtbf)
        current_time += next_failure
        if current_time < total_hours:
            failures.append((current_time, current_time + restore_time))
            current_time += restore_time  
    return failures

def sys_failure(mtbf, restore_time, years, num_simulations=1000):
    total_failures_time = 0
    for _ in range(num_simulations):
        random.seed()  
        server1_failures = fail_generate(mtbf, restore_time, years)
        server2_failures = fail_generate(mtbf, restore_time, years)

        for f1_start, f1_end in server1_failures:
            for f2_start, f2_end in server2_failures:
                if f1_start < f2_end and f2_start < f1_end:  
                    total_failures_time += min(f1_end, f2_end) - max(f1_start, f2_start)
                    break

    avg_fail_time = total_failures_time / num_simulations
    return avg_fail_time

years_custom = 20
mtbf_custom = 500  
restore_time_custom = 10 
server_failures_custom = fail_generate(mtbf_custom, restore_time_custom, years_custom)

print("First 5 failures and restoration times for a server over 20 years:")
for i, (fail, restore) in enumerate(server_failures_custom[:5], 1):
    print(f"{i}. Failure at hour {fail:.2f}, restored by hour {restore:.2f}")

avg_fail_time = sys_failure(mtbf_custom, restore_time_custom, years_custom)
print(f"\nAverage time until the whole computing system fails: {avg_fail_time}")
