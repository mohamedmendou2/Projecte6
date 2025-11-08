# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio multiplica una serie de nombres
# Instruccions de entrada: 

def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat

print(multiplica_tot(2, 3, 4))  
print(multiplica_tot(5, 10))   

