# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció:   Validar i llegir nombres enters des d'un fitxer
# Instruccions de entrada: 

with open("nombres.txt", "r") as f:
    for linia in f:
        try:
            numero = int(linia.strip())
            print("Nombre vàlid:", numero)
        except ValueError:
            print("AVÍS: Aquesta línia no és un enter:", linia.strip())
