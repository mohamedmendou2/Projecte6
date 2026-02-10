# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Vehicle" amb un mètode "arrencar" que imprimeix el nom de la marca del vehicle. Després, es defineix una subclasse "Cotxe" que hereta de "Vehicle" i implementa un mètode "tocar_claxon".
# Especificacions d'entrada:

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"{self.marca} està arrencant.")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")
