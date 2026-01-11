# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Persona amb atributs i mètodes per mostrar informació de la persona.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat
    
    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")

# Prova la classe
persona = Persona("Mohamed", 18)
persona.presentar_se()

