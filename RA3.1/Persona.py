# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Persona amb atributs per al nom i l'edat.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

# Definició de la classe Persona
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def mostrar_info(self):
        print(f"Nom: {self.nom}, Edat: {self.edat}")
