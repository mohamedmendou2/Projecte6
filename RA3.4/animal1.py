# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Animal" amb un mètode "fer_soroll" que no fa res (pass). Després, es defineixen dues subclasses, "Gos" i "Gat", que hereten de "Animal" i implementen el mètode "fer_soroll" per retornar els sons característics dels gossos i gats, respectivament.
# Especificacions d'entrada:

class Animal:
    def fer_soroll(self):
        pass

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    print(animal.fer_soroll())