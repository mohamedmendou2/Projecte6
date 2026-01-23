# Autor: Mohamed Mendou     
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe Sensor amb un atribut privat __valor. Implementa propietat per llegir i modificar el valor només si està entre 0 i 100.
# Especificacions d'entrada:

class sensor:
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor

