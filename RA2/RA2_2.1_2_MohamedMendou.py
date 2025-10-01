# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Donat un numero el programa diu si es parell o inparell
# Especificacions d'entrada: Indroduir un numero enter

# Demana a l'usuari que introdueixi un numero enter i el desa a la variable 'numero'
numero = int(input("Introdueix un numero: "))

# Comprova si el numero es parell
if numero % 2 == 0:

    # Si el numero es parell, imprimeix aquest missatge
    print("El numero es parell")

# Si el numero no es parell, imprimeix aquest missatge
elif numero % 2 != 0:
    print("El numero es inparell")
