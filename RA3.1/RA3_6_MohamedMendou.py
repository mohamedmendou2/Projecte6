# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que utilitza la classe Punt per crear punts i calcular la distància entre ells.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

from Punt import Punt


punt_a = Punt(2, 3)
punt_b = Punt(5, 7)

distancia = punt_a.distancia(punt_b)
print(f"Distància entre ({punt_a.x},{punt_a.y}) i ({punt_b.x},{punt_b.y}): {distancia:.2f}")
print()