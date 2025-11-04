# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars
# Instruccions de entrada: Introduir una 10 números enters

# Creem dues llistes buides per als números parells i senars
parells = []
senars = []
# Demana a l'usuari que introdueixi 10 números enters
for i in range(10):
    numero = int(input("Introdueix un número enter: "))
    
    # Comprova si el número és parell o senar i l'afegeix a la llista corresponent
    if numero % 2 == 0:
        parells.append(numero)
    else:
        senars.append(numero)
# Mostra les dues llistes
print("Llista de números parells:", parells)
print("Llista de números senars:", senars)
