# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Llibre amb atributs per al títol, autor i any.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any
    
    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}")
