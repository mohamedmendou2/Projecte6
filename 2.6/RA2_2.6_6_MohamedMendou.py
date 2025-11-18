# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Comprovar si un fitxer existeix i llegir-ne el contingut
# Instruccions de entrada: 

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as f:
        print(f.read())
else:
    print("ERROR: El fitxer dades.txt no existeix.")
