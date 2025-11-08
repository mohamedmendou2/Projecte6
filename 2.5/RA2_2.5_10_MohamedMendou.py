# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio filtra parells, que reb una llista de nombre i retorna una altra de nomes parells 
# Instruccions de entrada: 

def filtra_parells(llista):
    parells = []
    for n in llista:
        if n % 2 == 0:
            parells.append(n)
    return parells

print(filtra_parells([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  

