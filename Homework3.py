import math

def calculate_trukytnuk(a,b,expected_c):
    c = math.sqrt(a**2 + b**2)
    perumetr = a + b + c 
    
    is_match = (c - expected_c) < 1e-6
    print(f"гіпотенуза: {c}, периметр: {perumetr}, зходиться: {is_match:}")
    
a_val = 3.0
b_val = 4.0
expected_c_val = 5.0

calculate_trukytnuk(a_val , b_val , expected_c_val)
