# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Animal" amb un mètode "parlar" que no fa res (pass). Després, es defineixen dues subclasses, "Gos" i "Gat", que hereten de "Animal" i implementen el mètode "parlar" per imprimir els sons característics dels gossos i gats, respectivament.
# Especificacions d'entrada:

class Animal:
    def parlar(self):
        pass

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")