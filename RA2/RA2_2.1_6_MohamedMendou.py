# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Programa que demana una lletra i diu si es vocal o consonant
# Especificacions d'entrada: INdroduir una lletra

# Demana a l'usuari que introdueixi una lletra i la desa a la variable 'lletra'
lletra = input("Introdueix una lletra minuscula: ")

# Comprova si la lletra es una vocal
if lletra == "a" or lletra == "e" or lletra == "i" or lletra == "o" or lletra == "u":

    # Si la lletra es una vocal, imprimeix aquest missatge
    print("La lletra es una vocal")
else:
    # Si la lletra no es una vocal, imprimeix aquest missatge
    print("La lletra es una consonant")