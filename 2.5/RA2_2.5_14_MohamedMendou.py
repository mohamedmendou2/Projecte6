# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: comprova si diferents numeros son parells
# Instruccions de entrada: 

def es_parell(numero):
    return numero % 2 == 0

llista = [1, 2, 3, 4, 5, 6]

for n in llista:
    print(f"El número {n} és parell: {es_parell(n)}")
