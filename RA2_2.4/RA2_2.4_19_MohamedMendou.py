# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Multiplicar per 2 una llista de numeros

llista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def multiplicar_per_dos(llista):
    llista_multiplicada = []
    for numero in llista:
        llista_multiplicada.append(numero * 2)
    return llista_multiplicada

llista_resultat = multiplicar_per_dos(llista_numeros)

print("Llista multiplicada per 2:", llista_resultat)

