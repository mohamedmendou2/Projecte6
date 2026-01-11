# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Cercle amb atributs i mètodes per mostrar informació del cercle.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi
    
    def area(self):
        return math.pi * (self.radi ** 2)
    
    def perimetre(self):
        return 2 * math.pi * self.radi

cercle = Cercle(5)
print(f"Radi: {cercle.radi}")
print(f"Àrea: {cercle.area():.2f}")
print(f"Perímetre: {cercle.perimetre():.2f}")
