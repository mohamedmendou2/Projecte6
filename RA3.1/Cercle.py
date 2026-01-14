# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Cercle amb atributs per al radi i mètodes per calcular l'àrea i el perímetre.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi
    
    def area(self):
        return math.pi * (self.radi ** 2)
    
    def perimetre(self):
        return 2 * math.pi * self.radi