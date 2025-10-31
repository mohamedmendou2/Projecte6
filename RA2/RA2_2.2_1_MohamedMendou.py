# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Programa que mostra a la pantalla una compta enrere del 10 al 1 i després escriu "Feliç any nou"

# Importa la funció sleep del mòdul time

from time import sleep
# Inicia la compta enrere des del 10 fins al 1
for i in range(10, 0, -1):
    print(i)
    sleep(1)  # Espera 1 segon entre cada número

# Després de la compta enrere, imprimeix "Feliç any nou"
print("Feliç any nou!")
