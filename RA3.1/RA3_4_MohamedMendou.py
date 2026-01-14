# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que utilitza la classe CompteBancari per gestionar operacions bancàries.
# Especificacions d'entrada: No hi ha entrada de l'usuari.


from Comptebancari import CompteBancari


compte = CompteBancari(500)
compte.veure_saldo()
compte.ingressar(200)
compte.retirar(150)
compte.retirar(800)  
compte.veure_saldo()
print()