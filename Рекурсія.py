def digital_root(n):
    n = abs(n)

    if n < 10:
        return n

    digit_sum = 0

    for digit in str(n):
        digit_sum += int(digit)

    return digital_root(digit_sum)

number = 7292

result = digital_root(number)

print("Цифровий корінь:", result)