# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció:  Comprovar si es pot escriure en un fitxer
# Instruccions de entrada: 

try:
    with open("resultats.txt", "w") as f:
        f.write("Prova d'escriptura.\n")
except PermissionError:
    print("ERROR: No tens permís per escriure al fitxer resultats.txt.")
