# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Llibre amb atributs i mètodes per mostrar informació del llibre.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any
    
    def mostrar_info(self):
        print(f"'{self.titol}' de {self.autor} ({self.any})")

llibre = Llibre("El Quixot", "Miguel de Cervantes", 1605)
llibre.mostrar_info()