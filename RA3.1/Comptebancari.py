# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe CompteBancari amb atributs per al saldo i mètodes per ingressar, retirar i veure el saldo.
# Especificacions d'entrada: No hi ha entrada de l'usuari


class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def ingressar(self, quantitat):
        self.saldo += quantitat
    
    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Saldo insuficient")
    
    def veure_saldo(self):
        return self.saldo