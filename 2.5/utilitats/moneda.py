# Autor: Mohamed Mendou
# Data: 8/11/2025
# Versio: 1
#
# Descripció: Aquest mòdul conté funcions per convertir entre euros i dòlars.
# Instruccions de entrada:


def euros_a_dolars(euros):
    canvi = 1.07   
    return euros * canvi

def dolars_a_euros(dolars):
    canvi = 1.07
    return dolars / canvi

print(euros_a_dolars(50))
print(dolars_a_euros(100))
