# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio factorial que calcula el factorial d'un nombre de forma recursiva
# Instruccions de entrada: 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))