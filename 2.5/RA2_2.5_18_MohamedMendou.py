# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio calcula factiorials de diferents numeros 
# Instruccions de entrada: 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(7))  
print(factorial(3))  
print(factorial(5))  

