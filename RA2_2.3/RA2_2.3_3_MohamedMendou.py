# Autor: Mohamed Mendou
# Data: 17/10/2025
# Versio: 1
#
# Descripció: Programa que mostri la taula de multiplicar d'un numero introduit per l'usuari
# Especificacions d'entrada: Introduir numero enter

# Demana a l'usuari que introdueixi un número enter

try:
    numero = int (input("Introdueix un numero enter"))

# Mostra la taula de multiplicar del número introduït
    for i in range (1, 11):
        resultat = numero * i
        print(f"{numero} x {i} = {resultat}")

except ValueError:
    print("Error: Introdueix un numero enter vàlid.")
