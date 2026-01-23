# Autor: Mohamed Mendou     
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe Producte amb atribut privat __preu. Afegeix mètodes per consultar i canviar el preu.
# Especificacions d'entrada:

class producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    def consultar_preu(self):
        return self.__preu
    
    def canviar_preu(self, nou_preu):
        self.__preu = nou_preu
