# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Aquest programa llegeix el contingut d'un fitxer de text anomenat "missatge.txt" i el mostra per pantalla.
# Instruccions de entrada: 

with open("missatge.txt", "r") as f:
    contingut = f.read()
    print("Contingut del fitxer:")
    print(contingut)

