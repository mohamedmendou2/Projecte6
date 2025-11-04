# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Funcio que elimina tots els espais d'una cadena 
# Instruccions de entrada: Introduir una cadena de text

def elimina_espais(cadena):
    # Utilitza el mètode replace per eliminar els espais
    return cadena.replace(" ", "")
# Demana a l'usuari que introdueixi una cadena de text
cadena_entrada = input("Introdueix una cadena de text: ")
# Crida la funció i desa el resultat
cadena_sense_espais = elimina_espais(cadena_entrada)
# Mostra la cadena sense espais
print("Cadena sense espais:", cadena_sense_espais)