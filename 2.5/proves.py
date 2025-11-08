# Autor: Mohamed Mendou
# Data: 8/11/2025
# Versio: 1
#
# Descripció: Utilitza les funcions de validacions.py per validar emails i telèfons
# Instruccions de entrada: 

import validacions as val

# Proves emails
print(val.es_email_valid("prova@gmail.com"))   
print(val.es_email_valid("hola@@gmail..com"))  
print(val.es_email_valid("usuari@web"))        

# Proves telèfon
print(val.es_telefon_valid("654987321"))  
print(val.es_telefon_valid("6549A7321"))  
print(val.es_telefon_valid("12345"))      
