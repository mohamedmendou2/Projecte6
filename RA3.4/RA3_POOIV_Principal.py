# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa demostra l'ús de classes i herència en Python mitjançant diversos exemples d'objectes.
# Especificacions d'entrada:


from animal import Gos, Gat
from vehicle import Cotxe
from persona import Treballador
from figura import Quadrat, Cercle
from llibre import LlibrePaper, LlibreDigital

# Exercici 1: Animals
g = Gos()
g.parlar()

c = Gat()
c.parlar()

# Exercici 2: Vehicles
cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()

# Exercici 3: Persones i treballadors
treballador = Treballador("Joan", 30, "Enginyer")
treballador.saludar()
treballador.mostrar_feina()

# Exercici 4: Figura geomètrica
quadrat = Quadrat(4)
print(f"Àrea del quadrat: {quadrat.area()}")

cercle = Cercle(3)
print(f"Àrea del cercle: {cercle.area()}")

# Exercici 5: Biblioteca
llibre_paper = LlibrePaper("El nom de la rosa", "Umberto Eco", 512)
llibre_paper.mostrar_info()

llibre_digital = LlibreDigital("Sapiens", "Yuval Noah Harari", "PDF")
llibre_digital.mostrar_info()