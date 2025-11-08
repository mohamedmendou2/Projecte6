# Autor: Mohamed Mendou
# Data: 6/11/2025
# Versio: 1
#
# Descripció: Funcio estat i edat de persona que retorni si es menor d'edat, adult o Jubilat 
# Instruccions de entrada: 

def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat"
    elif edat < 65:
        return "Adult"
    else:
        return "Jubilat"


print(estat_persona(15))  
print(estat_persona(35))  
print(estat_persona(70))  
