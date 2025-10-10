# Autor: Mohamed Mendou
# Data: 8/10/2025
# Versio: 1
#
# Descripció: Demna a l'usiari un nuemero enter positiu i determina si es primer o no 
# Especificacions d'entrada: Introduir un numero enter positiu


#Sense el range
# Demana a l'usuari que introdueixi un número enter positiu i el desa a la variable 'numero'
numero = int(input("Introdueix un numero enter positiu: ")) 
es_primer = True
if numero <= 1:
    es_primer = False
else:
    i = 2
    while i <= numero // 2:
        if numero % i == 0:
            es_primer = False
            break
        i += 1
if es_primer:
    print(f"El numero {numero} es primer")
else:
    print(f"El numero {numero} no es primer")

