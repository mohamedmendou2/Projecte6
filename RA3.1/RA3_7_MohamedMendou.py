from animal import Animal

class Gos(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Gos")
    
    def fer_soroll(self):
        return f"{self.nom} diu: Bup bup!"


gos1 = Gos("Rex")

print(gos1.fer_soroll())
print()
