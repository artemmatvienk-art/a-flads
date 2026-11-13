n = int(input("Введіть число N: "))

total_sum = 0
primes = []

for num in range(2, n + 1):
    is_prime = True

    for dilnuk in range(2, int(num**0.5) + 1):
        if num % dilnuk == 0:
            is_prime = False
            break

    if is_prime:
        total_sum += num
        primes.append(str(num))

primes_str = "+".join(primes)

print(f"Сума простих чисел від 2 до {n} ({primes_str}): {total_sum}")
