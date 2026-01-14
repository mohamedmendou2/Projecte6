# Autor: Mohamed Mendou
# Data: 11/1/2026
# Versio: 1
#
# Descripció: Programa que utilitza la classe Persona per gestionar una col·lecció de persones.
# Especificacions d'entrada: No hi ha entrada de l'usuari.

# Importar la classe Persona (que s'ha de trobar al mateix directori)
from Persona import Persona

def mostrar_majors_30(persones):
    """Mostra només les persones que tenen més de 30 anys"""
    for persona in persones:
        if persona.edat > 30:
            print(persona.mostrar_info())  

# Crear una llista de persones
persones = [
    Persona("Anna", 25),
    Persona("Pere", 42),
    Persona("Maria", 31),
    Persona("Jordi", 28),
    Persona("Carme", 55)
]

# Executar l'exercici

print("Persones majors de 30 anys:")
mostrar_majors_30(persones)