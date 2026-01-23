# Autor: Mohamed Mendou       
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe CompteBancari amb un atribut privat __saldo. Implementa mètodes per consultar el saldo, ingressar i retirar diners.
# Especificacions d'entrada:

class comptebancari:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def ingressar(self, quantitat):
        self.__saldo = self.__saldo + quantitat

    def retirar(self, quantitat):
        self.__saldo = self.__saldo - quantitat
