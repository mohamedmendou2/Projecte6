# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Persona" amb un constructor que inicialitza el nom i l'edat de la persona, així com un mètode "saludar" que imprimeix un missatge de salutació. Després, es defineix una subclasse "Treballador" que hereta de "Persona" i afegeix un atribut "feina" i un mètode "mostrar_feina" per mostrar la feina del treballador.
# Especificacions d'entrada:

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}.")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}.")