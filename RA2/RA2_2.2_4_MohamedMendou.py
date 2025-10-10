# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Program que genera un aletori entre l'1 i el 100 i demana a l'usuari que l'encerti 
# Especificacions d'entrada: Introduir un numero entre l'1 i el 100

# Importa la biblioteca random per generar números aleatoris
import random

# Genera un número aleatori entre 1 i 100
numero = random.randint(1, 100)
numero_usuari = int(input("Introdueix un numero entre l'1 i el 100: "))

# Mostra el número generat (per a propòsits de prova)
print(numero)
while numero_usuari != numero:
    if numero_usuari < numero:
        print("El nuemero es mes petit")
    else:
        print("El numero es mes gran")
    numero_usuari = int(input("Introdueix un altre numero: "))

# Quan l'usuari encerta el número, imprimeix un missatge de felicitació
print("Has encertat el numero!")
    
