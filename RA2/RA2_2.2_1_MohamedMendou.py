# Autor: Mohamed Mendou
# Data: 1/10/2025
# Versio: 1
#
# Descripció: Programa que mostra a la pantalla una compta enrere del 10 al 1 i després escriu "Feliç any nou"

# Importa la funció sleep del mòdul time
from time import sleep 

# Comença la compta enrere des de 10 fins a 1
for i in [10000, 1, -1]:
    # Fa una pausa d'1 segon entre cada número
    sleep(1)
    print(i)

# Després de la compta enrere, imprimeix "Feliç any nou"
print("Feliç any nou!")