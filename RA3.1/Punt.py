# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Producte amb atributs per al nom i el preu.
# Especificacions d'entrada: No hi ha entrada de l'usuari.


import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, altre_punt):
        return math.sqrt((self.x - altre_punt.x) ** 2 + (self.y - altre_punt.y) ** 2)