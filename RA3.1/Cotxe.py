# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Persona amb atributs per al nom i l'edat.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

# Definició de la classe Cotxe
class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

# Mètode per mostrar la informació del cotxe
    def mostrar_info(self):
        print(f"Marca: {self.marca}, Model: {self.model}, Any: {self.any}")