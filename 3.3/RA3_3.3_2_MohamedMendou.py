# Autor: Mohamed Mendou     
# Data: 27-1-2026
# Versió: 1
# Descripció: Implementació del principi de responsabilitat única i principi d'inversió de dependències
# Especificacions d'entrada:


# Interfície/Contracte per a notificadors
class Notificador:
    def enviar(self, missatge):
        pass

# Implementació per a Email
class EmailNotificador(Notificador):
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

# Nova implementació per a SMS (exemple d'extensibilitat)
class SMSNotificador(Notificador):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

# Nova implementació per a Push (exemple d'extensibilitat)
class PushNotificador(Notificador):
    def enviar(self, missatge):
        print(f"Notificació push: {missatge}")

# Classe Comanda ara no crea el notificador, el rep per injecció
class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador  # Acoblament baix: depèn d'una abstracció

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        missatge = f"Hola {self.client}, la teva comanda ha estat confirmada."
        self.notificador.enviar(missatge)  # Delegació de responsabilitats

# Ús del codi
notificador_email = EmailNotificador()
comanda = Comanda("Client A", notificador_email)
comanda.confirmar()

# Canviar tipus de notificador sense modificar Comanda
notificador_sms = SMSNotificador()
comanda2 = Comanda("Client B", notificador_sms)
comanda2.confirmar()

notificador_push = PushNotificador()
comanda3 = Comanda("Client C", notificador_push)
comanda3.confirmar()