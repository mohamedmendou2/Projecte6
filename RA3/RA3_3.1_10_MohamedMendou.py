# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Punt amb atributs i mètodes per calcular la distància entre dos punts.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def calcular_distancia(self, altre_punt):
        distancia = math.sqrt((altre_punt.x - self.x)**2 + (altre_punt.y - self.y)**2)
        return distancia

# Prova la classe
punt1 = Punt(3, 4)
punt2 = Punt(7, 1)
distancia = punt1.calcular_distancia(punt2)
print(f"Distància entre ({punt1.x},{punt1.y}) i ({punt2.x},{punt2.y}): {distancia:.2f}")
