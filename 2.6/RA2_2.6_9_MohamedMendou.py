# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Crear un fitxer si no existeix i llegir-ne el contingut
# Instruccions de entrada: 


try:
    with open("prova.txt", "r") as f:
        print("Fitxer existent:")
        print(f.read())
except FileNotFoundError:
    with open("prova.txt", "w") as f:
        f.write("Fitxer creat automaticament\n")
    print("Fitxer creat perquè no existia.")
