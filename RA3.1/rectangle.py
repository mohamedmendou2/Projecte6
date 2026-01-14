# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix els atributs de amplada i alçada d'un rectangle.
# Especificacions d'entrada: No hi ha entrada de l'usuari.


# Definició de la classe Rectangle
class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

# Mètode per calcular l'àrea del rectangle
    def area(self):
        return self.amplada * self.alçada
   
# Metode per calcular el perímetre del rectangle
    def perimetre(self):
        return 2 * (self.amplada + self.alçada)