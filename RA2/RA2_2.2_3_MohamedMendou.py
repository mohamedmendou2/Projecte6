# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Demana al usuari un numero enter i mostra la seva taula de multiplicar
# Especificacions d'entrada: Introduir un numero enter

# Demana a l'usuari que introdueixi un numero enter i el desa a la variable 'numero'
numero = int(input("Introdueix un numero enter: "))
# Utilitza un bucle 'while' per imprimir la taula de multiplicar del numero des de 1 fins a 10
i = 1
while i <= 10:

# Imprimeix el resultat de la multiplicació del numero per 'i'
    print(f"{numero} x {i} = {numero * i}")
    i += 1

