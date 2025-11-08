# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio determina l'estat de diferents edats 
# Instruccions de entrada: 


def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat"
    elif edat < 65:
        return "Adult"
    else:
        return "Jubilat"

edats = [12, 25, 70]

for e in edats:
    print(e, "→", estat_persona(e))
