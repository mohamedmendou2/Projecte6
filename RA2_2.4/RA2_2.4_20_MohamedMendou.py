# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Demana una llista i crea una nova llista nomes amb les paraules que comencen per una vocal
# Instruccions de entrada: Introduir una llista de paraules

paraules = input("Introdueix una llista de paraules separades per comes: ").split(",")

vocals = ["a", "e", "i", "o", "u"]
nova_llista = []

for p in paraules:
    p = p.strip()  # treu espais davant i darrere
    if p[0].lower() in vocals:
        nova_llista.append(p)

print("Llista de paraules que comencen per una vocal:", nova_llista)



