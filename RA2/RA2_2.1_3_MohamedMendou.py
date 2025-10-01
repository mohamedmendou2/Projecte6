# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Un programa que demana tres numero i surt per la pantalla el mes gran 
# Especificacions d'entrada: Introduir tres numeros enters

# Demana a l'usuari que introdueixi tres numeros enters i els desa a les variables 'num1', 'num2' i 'num3'
num1 = int(input("Introdueix el primer numero: "))
num2 = int(input("Introdueix el segon numero: "))
num3 = int(input("Introdueix el tercer numero: "))

# Comprova si el primer numero es mes gran que els altres dos
if num1 >= num2 and num1 >= num3:

    # Si el primer numero es mes gran, imprimeix aquest missatge
    print(f"El numero mes gran es: {num1}")

# Comprova si el segon numero es mes gran que els altres dos
if num2 >= num1 and num2 >= num3:

    # Si el segon numero es mes gran, imprimeix aquest missatge
    print(f"El numero mes gran es: {num2}")

# Si el tercer numero es mes gran que els altres dos, imprimeix aquest missatge
if num3 >= num1 and num3 >= num2:
    print(f"El numero mes gran es: {num3}")

if num1 == num2 and num1 == num3 and num2 == num3:
    print("Els numeros son iguals")