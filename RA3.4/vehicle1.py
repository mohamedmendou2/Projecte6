# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Vehicle" amb un mètode "moure" que imprimeix un missatge de moviment no definit. Després, es defineixen tres subclasses, "Cotxe", "Bicicleta" i "Barca", que hereten de "Vehicle" i implementen el mètode "moure" per mostrar el moviment de cada vehicle respectivament.
# Especificacions d'entrada:

class Vehicle:
    def moure(self):
        pass

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe està movent-se.")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta està movent-se.")

class Barca(Vehicle):
    def moure(self):
        print("La barca està navegant.")

def simular_moviment(vehicles):
    for vehicle in vehicles:
        vehicle.moure()