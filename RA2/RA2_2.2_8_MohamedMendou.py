# Autor: Mohamed Mendou
# Data: 8/10/2025
# Versio: 1
#
# Descripció: Demana a l'usuari una frase i compta les vocals que te
# Especificacions d'entrada: Introduir una cadena de text

# Demana a l'usuari que introdueixi una frase i la desa a la variable 'frase'
frase = input("Introdueix una frase: ")

# Inicialitza el comptador de vocals a 0
comptador_vocals = 0   
# Itera sobre cada caràcter de la frase
for car in frase:
    # Comprova si el caràcter és una vocal (tant majúscula com minúscula)
    if car.lower() in 'aeiou':
        comptador_vocals += 1  # Incrementa el comptador de vocals
# Mostra el nombre total de vocals trobades a la frase
print(f"La frase te {comptador_vocals} vocals")