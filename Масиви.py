numbers = [11, 10, 5, 17, 50, 19, 41, 23]
min = numbers[0]
max = numbers[0]

for num in numbers:
    if num > max:
        max = num

    if num < min:
        min = num

sum = max - min

print(f"Minimum number: {min}")
print(f"Maximum number: {max}")
print(f"Sum: {sum}")