# Autor: Mohamed Mendou      
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe Alumne amb un atribut privat __edat. Implementa mètode per modificar l'edat només si és un valor positiu i un mètode per mostrar l'edat.
# Especificacions d'entrada:

class alumne:
    def __init__(self, edat):
        self.__edat = edat
    
    def edat (self, valor):
        if 0 <= self.__edat:
            self.__edat = valor

    def mostrar_edat(self):
        print(self.__edat)


