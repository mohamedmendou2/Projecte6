# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Aquest script crea un fitxer de text anomenat "sortida.txt" i escriu diverses línies de text en ell utilitzant el mètode writelines().
# Instruccions de entrada: 

linies = [
    "Primera linia\n",
    "Segona linia\n",
    "Tercera linia\n"
]

with open("sortida.txt", "w") as f:
    f.writelines(linies)
