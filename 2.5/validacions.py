# Autor: Mohamed Mendou
# Data: 8/11/2025
# Versio: 1
#
# Descripció: Defineix funcions per validar emails i números de telèfon
# Instruccions de entrada: 


import re

def es_email_valid(email):
    # regex simple per verificar emails bàsics
    patró = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patró, email) is not None

def es_telefon_valid(telefon):
    # Exemple simple: només números i mínim 9 dígits (format Espanya)
    patró = r'^\d{9}$'
    return re.match(patró, telefon) is not None
