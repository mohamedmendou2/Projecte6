# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Animal amb atributs i mètodes per mostrar informació de l'animal.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie
    
    def fer_soroll(self):
        print("fa un soroll")

# Prova la classe
animal = Animal("Miky", "gat")
print(f"{animal.nom} és un {animal.especie} i...")
animal.fer_soroll()
