# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Estudiant amb atributs per al nom i la nota.
# Especificacions d'entrada: No hi ha entrada de l'usuari.


class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
    
    def ha_aprovat(self):
        return self.nota >= 5