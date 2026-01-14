# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que utilitza la classe Producte per gestionar productes i aplicar descomptes.
# Especificacions d'entrada: No hi ha entrada de l'usuari.


from Producte import Producte

def aplicar_descompte_10(productes):
    for producte in productes:
        producte.aplicar_descompte(10)


productes = [
    Producte("Sabates", 60),
    Producte("Samarreta", 25),
    Producte("Pantalons", 40)
]



aplicar_descompte_10(productes)

print("Preus amb el descompte del 10% de descompte:")
for p in productes:
    print(f"  {p.nom}: {p.preu:.2f}€")
print()