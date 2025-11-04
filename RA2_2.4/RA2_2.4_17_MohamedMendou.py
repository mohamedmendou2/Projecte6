# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Demana una paraula i guarda cada lletra en una llista
# Instruccions de entrada: Introduir una paraula

paraula = input("Introdueix una paraula: ")

llista_lletres = []
for lletra in paraula:
    llista_lletres.append(lletra)
print("Llista de lletres:", llista_lletres)


