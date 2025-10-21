# Autor: Mohamed Mendou
# Data: 8/10/2025
# Versio: 1
#
# Descripció: Imprimeix tots els numeros parells des de el 0 fins al numero introduit per el usuari 
# Instruccions de entrada: Introduir numero enter

try:
    # Demanar un número a l'usuari
    n = int(input("Introdueix un nombre enter positiu: "))
    
    # Comprovar si el número és positiu
    if n < 0:
        print("Error: Has d'introduir un nombre enter positiu.")
    else:
        # Mostrar els números parells 
        print(f"Nombres parells des de 0 fins a {n}:")
        for num in range(0, n + 1, 2):
            print(num, end=" ")
            
# Salta el error si l'usuari no introdueix un número enter
except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")