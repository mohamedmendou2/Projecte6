# Autor: Mohamed Mendou
# Data: 31/10/2025
# Versio: 1
#
# Descripció: Verifica si la paraula es un palíndrom
# Instruccions de entrada: Introduir una paraula

# Demana a l'usuari que introdueixi una paraula
paraula = input("Introdueix una paraula: ")

# Comprova si la paraula es igual a la seva reversa
if paraula == paraula[::-1]:
    print(f"La paraula '{paraula}' és un palíndrom.")
else:
    print(f"La paraula '{paraula}' no és un palíndrom.")

