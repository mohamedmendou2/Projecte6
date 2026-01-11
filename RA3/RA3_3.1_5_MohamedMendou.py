# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Estudiant amb atributs i mètodes per mostrar informació de l'estudiant.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota
    
    def ha_aprovat(self):
        return self.nota >= 5

estudiant1 = Estudiant("Pere", 7.5)
estudiant2 = Estudiant("Maria", 4.2)
print(f"{estudiant1.nom} ha aprovat? {estudiant1.ha_aprovat()}")
print(f"{estudiant2.nom} ha aprovat? {estudiant2.ha_aprovat()}")
