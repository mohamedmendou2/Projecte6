# Autor: Mohamed Mendou
# Data: 7/11/2025
# Versio: 1
#
# Descripció: Calcula àrees de formes geomètriques bàsiques del script geometria.py
# Instruccions de entrada: 




import geometria

c = float(input("Introdueix el costat del quadrat: "))
print("Àrea del quadrat:", geometria.area_quadrat(c))

r = float(input("Introdueix el radi del cercle: "))
print("Àrea del cercle:", geometria.area_cercle(r))

b = float(input("Introdueix la base del rectangle: "))
h = float(input("Introdueix l'altura del rectangle: "))
print("Àrea del rectangle:", geometria.area_rectangle(b, h))
