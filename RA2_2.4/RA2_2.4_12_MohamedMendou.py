# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Emmagatzema 5 paraules en una llista
# Instruccions de entrada: Introduir una 5 paraules

paraules = []

for i in range(5):
    paraula = input("Introdueix una paraula: ")
    paraules.append(paraula)

print("La llista de paraules és:", paraules)
