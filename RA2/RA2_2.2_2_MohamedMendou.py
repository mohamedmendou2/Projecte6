# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Calcula la suma dels 100 primers numeros enters i mostra el resultat per pantalla

NUMERO = 100

# Inicialitza la variable 'suma' a 0
suma = 0

# Utilitza un bucle 'for' per iterar des de 1 fins a NUMERO (inclòs)
for i in range(1, NUMERO + 1):
    # Afegeix el valor de 'i' a 'suma' en cada iteració
    suma += i
# Imprimeix el resultat de la suma
print(f"La suma dels {NUMERO} primers numeros enters es: {suma}")


