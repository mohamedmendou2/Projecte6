# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Figura" amb un mètode "dibuixar" que imprimeix un missatge de dibuix no definit. Després, es defineixen dues subclasses, "Quadrat" i "Cercle", que hereten de "Figura" i implementen el mètode "dibuixar" per dibuixar les figures respectivament.
# Especificacions d'entrada:

class Figura:
    def dibuixar(self):
        pass

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle.")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat.")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle.")
