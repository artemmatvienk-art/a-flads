def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Знижка має бути від 0 до 100")

    final_price = price - (price * discount_percent / 100)

    return final_price

assert calculate_discount(100.0, 0.0) == 100.0
assert calculate_discount(100.0, 100.0) == 0.0
assert calculate_discount(0.0, 50.0) == 0.0
try:
    calculate_discount(-100.0, 15.0)
    assert False
except ValueError:
    pass

try:
    calculate_discount(100.0, 150.0)
    assert False
except ValueError:
    pass

try:
    calculate_discount(100.0, -10.0)
    assert False
except ValueError:
    pass

print("Автотести пройшли успішно")
print(calculate_discount(140.0, 20.0))
