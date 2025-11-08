# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio que multiplica qualsevol quantitat de noombre i retorna el resultat
# Instruccions de entrada: 

def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat

print(multiplica_tot(2, 3, 4))  
print(multiplica_tot(5, 6))     
print(multiplica_tot(7))        
print(multiplica_tot())         