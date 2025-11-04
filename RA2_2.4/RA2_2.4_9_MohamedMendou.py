# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Divideix una frase en paraules i les mostra una per una 
# Instruccions de entrada: Introduir una frase

# Demana a l'usuari que introdueixi una frase
frase = input("Introdueix una frase: ")

# Divideix la frase en paraules utilitzant l'espai com a separador
paraules = frase.split()
# Mostra cada paraula en una línia separada
for paraula in paraules:
    print(paraula)




