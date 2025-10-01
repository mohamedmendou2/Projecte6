# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Un programa que donat un numero digui si es mes gran o no que 0
# Especificacions d'entrada: Un numero enter

# Demana a l'usuari que introdueixi un numero enter i el desa a la variable 'numero'
numero = int(input("Introdueix un numero: "))  

# Comprova si el numero es igual que 0
if numero == 0:

    # Si el numero es igual que 0, imprimeix aquest missatge
    print("El numero es igual que 0")  
if numero < 0:

    # Si el numero es mes petit que 0, imprimeix aquest missatge
    print("El numero es mes petit que 0")

# Si el numero no es igual que 0 ni mes petit que 0, imprimeix aquest missatge
if numero > 0:
    print ("El numero es mes gran que 0")