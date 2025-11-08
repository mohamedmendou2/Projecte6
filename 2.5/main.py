import calculadora

num1 = int(input("Introdueix el primer nombre: "))
num2 = int(input("Introdueix el segon nombre: "))

resultat = calculadora.suma(num1, num2)

print(f"La suma de {num1} i {num2} és: {resultat}")

resultat = calculadora.resta(num1, num2)

print(f"La resta de {num1} i {num2} és: {resultat}")

resultat = calculadora.multiplicacio(num1, num2)

print(f"La multiplicació de {num1} i {num2} és: {resultat}")

resultat = calculadora.divisio(num1, num2)

print(f"La divisió de {num1} i {num2} és: {resultat}")