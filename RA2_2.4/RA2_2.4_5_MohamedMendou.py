# Autor: Mohamed Mendou
# Data: 31/10/2025
# Versio: 1
#
# Descripció: Substitueix totes les lletres a per @ en una frase donada
# Instruccions de entrada: Introduir una frase

# Demna a l'usuari que introdueixi una frase
frase = input("Introdueix una frase")

# Substitueix totes les lletres 'a' i 'A' per '@'
frase_modificada = frase.replace('a', '@').replace('A', '@')

# Mostra la frase modificada
print(frase_modificada)