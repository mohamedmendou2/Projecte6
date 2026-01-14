# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que utilitza la classe Cercle per crear diversos cercles i calcular les seves àrees.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

from Cercle  import Cercle

print("=== Exercici 9 ===")
cercles = [
    Cercle(3),
    Cercle(5),
    Cercle(2),
    Cercle(6),
    Cercle(4)
]

print("Cercles amb àrea superior a 50:")
for cercle in cercles:
    area = cercle.area()
    if area > 50:
        print(f"  - Radi: {cercle.radi}, Àrea: {area:.2f}")
print()