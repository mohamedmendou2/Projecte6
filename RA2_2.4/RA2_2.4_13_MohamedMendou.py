# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Funcio que suma tots els nombres d'una llista


def suma_llista(llista):
    total = 0
    for nombre in llista:
        total += nombre
    return total

numeros = [10, 5, 20, 18, 45]
resultat = suma_llista(numeros)
print("La suma de tots els nombres de la llista és:", resultat)
