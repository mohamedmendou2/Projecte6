# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Un programa que al ingresar un nuemro de l'1 al 10 digui si esta suspes o aprovat
# Especificacions d'entrada: Introduir un numero enter de l'1 al 10

# Demana a l'usuari que introdueixi un numero enter de l'1 al 10 i el desa a la variable 'nota'
nota = int(input("Introdueix un numero de l'1 al 10: "))

# Comprova si la nota es mes gran o igual que 5
if nota >= 5:

    # Si la nota es mes gran o igual que 5, imprimeix aquest missatge
    print("Aprovat")

# Si la nota es mes petit que 5, imprimeix aquest missatge
elif nota < 5:
    print("Suspès")
