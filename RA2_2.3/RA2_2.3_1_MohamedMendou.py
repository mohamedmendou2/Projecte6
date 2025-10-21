# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Program que generi una sequencia de nuemros enters des del 0 fins al numero introduit per l'usuari
# Especificacions d'entrada: Introduir numero enter

# Demana a l'usuari que introdueixi un número enter
numero_usuari = int(input("Introdueix un numero enter: "))

# Inicialitza el comptador a 0
comptador = 0
while comptador <= numero_usuari:
    print(comptador, end=' ')
    comptador += 1
# Mostra una línia buida al final
print()

# Si el usuari introdueix un valor no enter, el programa mostrarà un error.
try:
    numero_usuari = int(input("Introdueix un numero enter: "))
except ValueError:
    print("Error: Si us plau, introdueix un numero enter vàlid.")

    