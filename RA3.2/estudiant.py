# Autor: Mohamed Mendou     
# Data: 23-1-2026
# Versió: 1
# Descripció: Crea una classe Estudiant amb un atribut protegit _nota. Afegeix mètodes per: llegir la nota i modificar la nota només si és entre 0 i 10
# Especificacions d'entrada:

class estudiant:
    def __init__(self, nota):
        self._nota = nota

    def consultar_nota(self):
        return self._nota

    def augmentar(self, quantitat):
        self._nota = self._nota + quantitat

    def reduir(self, quantitat):
        self._nota = self._nota - quantitat


