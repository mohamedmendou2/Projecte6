# Autor: Mohamed Mendou     
# Data: 10-02-2026
# Versió: 1
# Descripció: Aquest programa defineix una classe base "Missatger" amb un mètode "enviar" que no fa res (pass). Després, es defineixen tres subclasses, "Email", "SMS" i "WhatsApp", que hereten de "Missatger" i implementen el mètode "enviar" per mostrar el tipus de missatge enviat.
# Especificacions d'entrada:

class Missatger:
    def enviar(self, missatge):
        pass

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant Email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")


def enviar_missatges(missatgers, missatge):
    for missatger in missatgers:
        missatger.enviar(missatge)