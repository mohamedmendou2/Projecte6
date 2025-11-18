# Autor: Mohamed Mendou
# Data: 18/11/2025
# Versio: 1
#
# Descripció: Gestió d'errors amb try-except-finally
# Instruccions de entrada: 


f = None
try:
    f = open("missatge.txt", "r")
    contingut = f.read()
    print(contingut)

    # Simulem un error
    a = 10 / 0     

except Exception as e:
    print("S'ha produït un error:", e)

finally:
    if f is not None:
        f.close()
        print("Fitxer tancat correctament.")
