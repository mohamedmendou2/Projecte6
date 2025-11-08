# Autor: Mohamed Mendou
# Data: 8/11/2025
# Versio: 1
#
# Descripció: Aquest mòdul proporciona funcions matemàtiques avançades
# Instruccions de entrada:



import math
from calculadora import suma, resta, multiplicacio, divisio

# Funcions combinades amb math
def arrel_quadrada(x):
    return math.sqrt(x)

def potencia(a, b):
    return math.pow(a, b)

def sine(x):
    return math.sin(math.radians(x))  # converteix a radians

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))
