# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Figura" amb un mètode "area" que imprimeix un missatge d'àrea no definida. Després, es defineixen dues subclasses, "Quadrat" i "Cercle", que hereten de "Figura" i implementen el mètode "area" per calcular l'àrea del quadrat i del cercle respectivament.
# Especificacions d'entrada:

import math

class Figura:
    def area(self):
        print("Àrea no definida.")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * (self.radi ** 2)