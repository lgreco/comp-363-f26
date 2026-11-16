def has_duplicate_brute_force(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
    return False


def has_duplicates_efficiently(nums):
    n = len(nums)
    sorted_nums = sorted(nums)
    for i in range(n-1):
        if sorted_nums[i] == sorted_nums[i+1]:
            return True
    return False

import random, time
rng = random.Random(2026)  # seed for consistent results
range_min = 1
range_max = 5
size = 14096
# Create test array
test_array = rng.sample(range(1,size+1),size)
#print(f"\n{test_array}")
# Test brute force
start_time = time.perf_counter_ns()
result = has_duplicate_brute_force(test_array)
stop_time = time.perf_counter_ns()
print(f"\nBrute force took {stop_time-start_time:,d} ns")
# Test adjacency search
start_time = time.perf_counter_ns()
result = has_duplicates_efficiently(test_array)
stop_time = time.perf_counter_ns()
print(f"Efficient method took {stop_time-start_time:,d} ns")