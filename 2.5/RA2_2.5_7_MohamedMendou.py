# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio maxim que dona el numero mes gran entre els tres
# Instruccions de entrada: 

def maxim(a, b, c):
    return max(a, b, c)

def maxim(a, b, c):
    major = a
    if b > major:
        major = b
    if c > major:
        major = c
    return major

print(maxim(3,7,10))