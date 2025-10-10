# Autor: Mohamed Mendou
# Data: 8/10/2025
# Versio: 1
#
# Descripció: Mostra els primers 10 numeros de la sequencia de Fibonacci

a, b = 0, 1
comptador = 0
while comptador < 10:
    print(a, end=' ')
    suma_termes = a + b
    a=b
    b=suma_termes
    comptador += 1
print()
