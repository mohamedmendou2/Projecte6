

num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

print(f"\nResultats per {num1} i {num2}:")
print("-" * 30)


suma = num1 + num2
print(f"{num1} + {num2} = {suma}")


resta = num1 - num2
print(f"{num1} - {num2} = {resta}")


multiplicacio = num1 * num2
print(f"{num1} * {num2} = {multiplicacio}")

if num2 != 0:
    divisio = num1 / num2
    print(f"{num1} / {num2} = {divisio}")
else:
    print(f"{num1} / {num2} = Error! No es pot dividir per zero")

print("\nGràcies per usar la calculadora!")