# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Programa que elimina els duplicats de una llista
# Instruccions de entrada: Introduir una llista amb elements duplicats

# Crearem la llista amb elements duplicats
llista_duplicats = [1, 2, 2, 3, 4, 4, 5, 5, 5]

# Utilitza set per eliminar els duplicats i després converteix-ho de nou a llista
llista_sense_duplicats = list(set(llista_duplicats))
print("Llista sense duplicats:", llista_sense_duplicats)


