# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Llibre" amb un constructor que inicialitza el títol i l'autor del llibre, així com un mètode "mostrar_info" que imprimeix la informació del llibre. Després, es defineixen dues subclasses, "LlibrePaper" i "LlibreDigital", que hereten de "Llibre" i afegeixen atributs específics per cada tipus de llibre.
# Especificacions d'entrada:

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pagines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")