# Autor: Mohamed Mendou     
# Data: 23-1-2026
# Versió: 1
# Descripció: Script principal per provar les diferents classes creades.
# Especificaicons de entrada: 

# Compte Bancari Simple
from comptebancari import comptebancari

comptebancari1 = comptebancari (1000)
print(comptebancari1.consultar_saldo())

# Estudiant amb nota protegida
from estudiant import estudiant

estudiant1 = estudiant (6)
print(estudiant1.consultar_nota())
estudiant1.augmentar(2)
print(estudiant1.consultar_nota())
estudiant1.reduir(4)
print(estudiant1.consultar_nota())

# Termòstat
from termostat import termostat

termostat1 = termostat(20)
print(termostat1.get_temperatura())

# Contrasenya segura
from contrasenya import usuari

usuari1 = usuari(8763429868576)

print("Verificació inicial (esperat True):", usuari1.verificar_contrasenya(8763429868576))

nova = "contrasenyaSegura2026"
usuari1.canviar_contrasenya(nova)

print("Després canvi vàlid (esperat True):", usuari1.verificar_contrasenya(nova))

print("Verificació amb antiga (esperat False):", usuari1.verificar_contrasenya(8763429868576))

# Sensor amb valors limitats
from sensor import sensor

sensor1 = sensor(20)
print(sensor1.get_valor())

sensor1.set_valor(80)
print(sensor1.get_valor())

# Producte amb preu controlat
from producte import producte

producte1 = producte ('Llet', 6)
print(producte1.consultar_preu())

producte1.canviar_preu(100)
print(producte1.consultar_preu())

# Temps en hores
from temps import rellotge

rellotge1 = rellotge(6)
print(rellotge1.mostrar_hora())

rellotge1.canviar_hora(10)
print(rellotge1.mostrar_hora())

# Alumne amb edat controlada
from alumne import alumne

alumne1 = alumne(6)
print(alumne1.mostrar_edat())
alumne1.edat(10)
print(alumne1.mostrar_edat())

# Gestor de puntuació
from gestor import joc

joc1 = joc()
joc1.sumar_punts(5)
print(joc1.puntuacio())
joc1.reiniciar_puntuacio()
print(joc1.puntuacio())

# Email d’un usuari
from gmail import compteusuari

usuari1 = compteusuari("mmendou@iesjulioantonio.cat")

print(usuari1.email)
