import time

n = 46317535
target = 46317534

numbers_list = list(range(n))
numbers_set = set(numbers_list)

start_time = time.perf_counter()
result_list = target in numbers_list
list_time = time.perf_counter() - start_time

start_time = time.perf_counter()
result_set = target in numbers_set
set_time = time.perf_counter() - start_time

print(f"List search: {list_time:.6f} сек")
print(f"Set search: {set_time:.6f} сек")