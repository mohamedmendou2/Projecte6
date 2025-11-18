# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Llegir i escriure en un fitxer 
# Instruccions de entrada: 

with open("sortida.txt", "r+") as f:
    print("Contingut actual:")
    print(f.read())

    f.write("\nNova linia afegida ")
