# Autor:Mohamed Mendou    
# Data: 23-1-2026
# Versió: 1
# Descripció: Classe Usuari amb atribut privat __contrasenya. Implementa: mètode canviar_contrasenya() (amb validació: mínim 8 caràcters) i mètode verificar_contrasenya(clau)
# Especificacions d'entrada:



class usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova_contrasenya):
        if len(nova_contrasenya) >= 8:
            self.__contrasenya = nova_contrasenya

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau



