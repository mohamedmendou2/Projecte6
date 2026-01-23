# Autor: Mohamed Mendou     
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe Termostat amb un atribut privat __temperatura. Implementa propietat per llegir i modificar la temperatura només si està entre 10 i 30 graus.
# Especificacions d'entrada:

class termostat:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
    
        if 10 <= valor <= 30:
            self.__temperatura = valor




