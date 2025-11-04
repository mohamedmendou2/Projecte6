# Autor: Mohamed Mendou
# Data: 4/11/2025
# Versio: 1
#
# Descripció: Funcio que retorna la llista al reves sense utilitzar la funcio reverse()

llista_numeros = [1, 2, 3, 4, 5]

def invertir_llista(llista):
    nova_llista = []
    for i in range(len(llista)-1, -1, -1):
        nova_llista.append(llista[i])
    return nova_llista

llista_invertida = invertir_llista(llista_numeros)
print("Llista invertida:", llista_invertida)


