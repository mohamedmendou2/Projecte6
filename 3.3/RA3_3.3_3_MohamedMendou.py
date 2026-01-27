# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Implementació del principi de responsabilitat única i principi d'inversió de dependències
# Especificacions d'entrada:

# Interfície/Contracte per a estratègies de descompte
class EstrategiaDescompte:
    def aplicar(self, total):
        pass

# Implementació per a descompte del 20%
class Descompte20(EstrategiaDescompte):
    def aplicar(self, total):
        descompte = total * 0.2
        return total - descompte

# Implementació per a descompte del 10%
class Descompte10(EstrategiaDescompte):
    def aplicar(self, total):
        descompte = total * 0.1
        return total - descompte

# Implementació per a sense descompte
class SenseDescompte(EstrategiaDescompte):
    def aplicar(self, total):
        return total

# Implementació per a descompte fix (ex. 15€)
class DescompteFixe(EstrategiaDescompte):
    def __init__(self, quantitat):
        self.quantitat = quantitat
    
    def aplicar(self, total):
        return max(total - self.quantitat, 0)  # No menys de 0

# Classe CarretCompra ara rep l'estratègia de descompte per injecció
class CarretCompra:
    def __init__(self, total, estrategia_descompte):
        self.total = total
        self.estrategia_descompte = estrategia_descompte  # Acoblament baix

    def calcular_total_amb_descompte(self):
        return self.estrategia_descompte.aplicar(self.total)  # Delegació

# Ús del codi
descompte_20 = Descompte20()
carret = CarretCompra(100, descompte_20)
print(f"Total amb descompte del 20%: {carret.calcular_total_amb_descompte()} €")

# Canviar estratègia de descompte sense modificar CarretCompra
descompte_10 = Descompte10()
carret2 = CarretCompra(100, descompte_10)
print(f"Total amb descompte del 10%: {carret2.calcular_total_amb_descompte()} €")

# Estratègia sense descompte
sense_desc = SenseDescompte()
carret3 = CarretCompra(100, sense_desc)
print(f"Total sense descompte: {carret3.calcular_total_amb_descompte()} €")

# Estratègia de descompte fixe
descompte_fixe = DescompteFixe(15)
carret4 = CarretCompra(100, descompte_fixe)
print(f"Total amb descompte fixe de 15€: {carret4.calcular_total_amb_descompte()} €")

