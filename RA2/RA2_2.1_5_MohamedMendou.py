# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Un programa que donat el any et digui si es o no major de edat
# Especificacions d'entrada: Itroduir el any de naixement

# Demana a l'usuari que introdueixi el seu any de naixement i el desa a la variable 'any_naixement'
any_naixement = int(input("Introdueix el teu any de naixement: "))

if any_naixement <= 2007:
    print("Ets majorde edat")

if any_naixement > 2007:
    print("No ets major de edat")
