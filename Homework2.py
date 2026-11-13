number = int(input("Ввід: число = "))

chuslo1 = number // 100

chuslo2 = (number // 10) % 10

chuslo3 = number % 10

sum_kvadrativ = chuslo1 * 2 + chuslo2 * 2 + chuslo3 * 2 

print(f"вивід: сума квадратів ({chuslo1}^2 + {chuslo2}^2 + {chuslo3}^2)")
