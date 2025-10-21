# Autor: Mohamed Mendou
# Data: 21/10/2025
# Versio: 1
#
# Descripció: Imprimeix tots els numeros parells des de el 0 fins al numero introduit per el usuari 
# Instruccions de entrada: Introduir numero enter

try:
    # Demanar número a l'usuari
    n = int(input("Introdueix un nombre enter positiu: "))
    
    # Comprovar si el número és positiu
    if n < 1:
        print("Error: Has d'introduir un nombre enter positiu major que 0.")
    else:
        print(f"Nombres primers des de 2 fins a {n}:")
        
        # Recórrer tots els números des de 2 fins a n
        for num in range(2, n + 1):
            es_primer = True
            
            # Comprovar si el número és primer
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    es_primer = False
                    break
            
            # Si és primer, mostrar-lo
            if es_primer:
                print(num, end=" ")
            
except ValueError:
    print("Error: Has d'introduir un nombre enter vàlid.")