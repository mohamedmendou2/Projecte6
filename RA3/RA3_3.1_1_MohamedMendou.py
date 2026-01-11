# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que defineix una classe Cotxe amb atributs i mètodes per mostrar informació del cotxe.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any
    
    def mostrar_info(self):
        return f"Cotxe: {self.marca} {self.model} ({self.any})"


cotxe1 = Cotxe("Toyota", "Corolla", 2022)
cotxe2 = Cotxe("Seat", "Ibiza", 2020)
print(cotxe1.mostrar_info())
print(cotxe2.mostrar_info())