# Autor: Mohamed Mendou
# Data: 17/10/2025
# Versio: 1
#
# Descripció: Calcula la suma de tots el nombres enter de de 1 fins al numero introduit per l'usuari
# Especificacions d'entrada: Introduir numero enter
try:

# Demana a l'usuari que introdueixi un número enter

    numero_usuari = int(input("Introdueix un numero enter: "))

# Inicialitza la variable suma a 0
    suma = 0
    comptador = 1  
    while comptador <= numero_usuari:
        suma += comptador
        comptador += 1

# Mostra la suma total
    print("La suma dels nombres enters de 1 fins a", numero_usuari, "és:", suma)

# Si el usuari introdueix un valor no enter, el programa mostrarà un error.

    numero_usuari = int(input("Introdueix un numero enter: "))
except ValueError:
    print("Error: Introdueix un numero enter vàlid.")
