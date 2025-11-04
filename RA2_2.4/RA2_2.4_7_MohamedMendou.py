# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Demana una cadena i compta quantes vegades apareix una lletra concreta.
# Instruccions de entrada: Introduir una cadena de text

# Demana a l'usuari que introdueixi una cadena de text
cadena = input("Introdueix una cadena de text: ")

# Demana a l'usuari que introdueixi la lletra a comptar
lletra_a_comptar = input("Introdueix la lletra que vols comptar: ")
# Inicialitza el comptador
comptador = 0
# Itera sobre cada caràcter de la cadena
for caracter in cadena:
    # Comprova si el caràcter actual és igual a la lletra a comptar
    if caracter == lletra_a_comptar:
        comptador += 1  # Incrementa el comptador si hi ha una coincidència
# Mostra el resultat
print(f"La lletra '{lletra_a_comptar}' apareix {comptador} vegades a la cadena.")
