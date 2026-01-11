# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Rectangle amb atributs i mètodes per mostrar informació del rectangle.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada
    
    def area(self):
        return self.amplada * self.alçada
    
    def perimetre(self):
        return 2 * (self.amplada + self.alçada)


rect = Rectangle(5, 10)
print(f"Àrea: {rect.area()}")
print(f"Perímetre: {rect.perimetre()}")

