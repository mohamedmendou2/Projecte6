# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Comptar les linies d'un fitxer 
# Instruccions de entrada: 

with open("sortida.txt", "r") as f:
    linies = f.readlines()
    print("El fitxer té", len(linies), "línies.")
