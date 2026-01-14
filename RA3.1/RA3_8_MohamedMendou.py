


from llibre import Llibre

class Biblioteca:
    def __init__(self):
        self.llibres = []
    
    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)
    
    def mostrar_llibres(self):
        for llibre in self.llibres:
            print(llibre.mostrar_info())

print("=== Exercici 8 ===")
biblioteca = Biblioteca()
biblioteca.afegir_llibre(Llibre("El Quijote", "Miguel de Cervantes", 1605))
biblioteca.afegir_llibre(Llibre("1984", "George Orwell", 1949))

print("Llibres a la biblioteca:")
biblioteca.mostrar_llibres()
print()