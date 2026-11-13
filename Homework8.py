array = [-4, 5, 3, -2, 7, 2, -4, 5, -2]

current_sum = array[0]
max_sum = array[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(array)):
    if current_sum + array[i] < array[i]:
        current_sum = array[i]
        temp_start = i
    else:
        current_sum += array[i]

    if current_sum > max_sum:
        max_sum = current_sum
        start = temp_start
        end = i

subarray = array[start:end + 1]

print(f"max sum subarray {subarray} {max_sum}")
