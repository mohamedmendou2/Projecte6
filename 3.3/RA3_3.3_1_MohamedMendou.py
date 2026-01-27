# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Implementació del principi de responsabilitat única i principi d'inversió de dependències
# Especificacions d'entrada:



# Interfície/Contracte per a impressores
class Impressora:
    def imprimir(self, contingut):
        pass

# Implementació per a PDF
class ImpressoraPDF(Impressora):
    def imprimir(self, contingut):
        print(f"Imprimit PDF: {contingut}")

# Nova implementació per a HTML (exemple d'extensibilitat)
class ImpressoraHTML(Impressora):
    def imprimir(self, contingut):
        print(f"{contingut}")

# Classe Factura ara no crea la impressora, la rep per injecció
class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Acoblament baix: depèn d'una abstracció

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)  # Delegació de responsabilitats

# Ús del codi
impressora_pdf = ImpressoraPDF()
factura = Factura("Client A", 100, impressora_pdf)
factura.imprimir_factura()

# Canviar tipus d'impressora sense modificar Factura
impressora_html = ImpressoraHTML()
factura2 = Factura("Client B", 200, impressora_html)
factura2.imprimir_factura()