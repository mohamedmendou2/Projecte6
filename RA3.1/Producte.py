# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Producte amb atributs per al nom i el preu.
# Especificacions d'entrada: No hi ha entrada de l'usuari.


class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu
    
    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte
        return self.preu