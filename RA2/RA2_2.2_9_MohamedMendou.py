# Autor: Mohamed Mendou
# Data: 8/10/2025
# Versio: 1
#
# Descripció: Troba el numero maxim d'una llista de numeros


# Demana a l'usuari que introdueixi una llista de números separats per espais i els desa a la variable 'numeros'
numeros = list(map(int, input("Introdueix una llista de numeros separats per espais: ").split()))
# Inicialitza la variable 'maxim' amb el primer element de la llista
maxim = numeros[0]
# Itera sobre cada número a la llista
for num in numeros:
    # Comprova si el número actual és més gran que 'maxim'
    if num > maxim:
        maxim = num  # Actualitza 'maxim' si es troba un número més gran
# Mostra el número màxim trobat a la llista
print(f"El numero maxim es: {maxim}")
