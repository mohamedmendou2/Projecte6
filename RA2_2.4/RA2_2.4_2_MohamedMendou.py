# Autor: Mohamed Mendou
# Data: 31/10/2025
# Versio: 1
#
# Descripció: Compta quantes vocals te una frase
# Instruccions de entrada: Introduir una frase

# Demana a l'usuari que introdueixi una frase
frase = input("Introdueix un frase")

# Inici el comptador de vocals
comptador_vocals = 0

# Recorre cada caràcter de la frase
for caracter in frase:
    # Comprova si el caràcter és una vocal (majúscula o minúscula)
    if caracter.lower() in 'aeiou':
        comptador_vocals += 1
# Mostra el nombre de vocals trobades
print(f"La frase conté {comptador_vocals} vocals.")

