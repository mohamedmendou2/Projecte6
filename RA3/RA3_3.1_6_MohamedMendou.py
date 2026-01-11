# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe CompteBancari amb atributs i mètodes per mostrar informació del compte.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def ingressar(self, quantitat):
        self.saldo += quantitat
        return f"S'han ingressat {quantitat}€"
    
    def retirar(self, quantitat):
        if quantitat > self.saldo:
            return "Saldo insuficient"
        self.saldo -= quantitat
        return f"S'han retirat {quantitat}€"
    
    def veure_saldo(self):
        return f"Saldo actual: {self.saldo}€"

# Prova la classe
compte = CompteBancari(100)
print(compte.veure_saldo())
print(compte.ingressar(50))
print(compte.retirar(30))
print(compte.veure_saldo())
print(compte.retirar(200))
