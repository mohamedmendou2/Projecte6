# Autor: Mohamed Mendou       
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe Rellotge amb un atribut privat __hores. Implementa mètodes per canviar l'hora (0-23) i mostrar l'hora en format "HH:MM".
# Especificacions d'entrada:

class rellotge:
    def __init__(self, hores):
        self.__hores = hores
    
    def canviar_hora(self, nova_hora):
        if 0 <= nova_hora <= 23:
            self.__hores = nova_hora

    def mostrar_hora(self):
        return f"{self.__hores:02d}:00"


