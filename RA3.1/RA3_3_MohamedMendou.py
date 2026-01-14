# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Rectangle amb atributs per a la llargada i l'amplada, i un mètode per calcular l'àrea.RA3_2_MohamedMendou.py
# Especificacions d'entrada: No hi ha entrada de l'usuari.


from estudiant import Estudiant


estudiants = [
    Estudiant("Anna", 7.5),
    Estudiant("Pau", 4.2),
    Estudiant("Maria", 8.0),
]

print("Estudiants aprovats:")
for estudiant in estudiants:
    if estudiant.ha_aprovat():
        print(f"  - {estudiant.nom}: {estudiant.nota}")
print()