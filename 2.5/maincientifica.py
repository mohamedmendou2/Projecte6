# Autor: Mohamed Mendou
# Data: 8/11/2025
# Versio: 1
#
# Descripció: Aquest mòdul proporciona funcions matemàtiques avançades del modul cientifica.py
# Instruccions de entrada:




from cientifica import suma, resta, multiplicacio, divisio, arrel_quadrada, potencia, sine, cosine, tangent

def menu():
    print("Calculadora científica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Arrel quadrada")
    print("6. Potència")
    print("7. Sinus")
    print("8. Cosinus")
    print("9. Tangent")
    print("0. Sortir")

while True:
    menu()
    opcio = input("Tria una opció: ")

    if opcio == "0":
        print("Fins aviat!")
        break
    elif opcio in ["1", "2", "3", "4"]:
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        if opcio == "1":
            print("Resultat:", suma(a, b))
        elif opcio == "2":
            print("Resultat:", resta(a, b))
        elif opcio == "3":
            print("Resultat:", multiplicacio(a, b))
        elif opcio == "4":
            print("Resultat:", divisio(a, b))
    elif opcio == "5":
        x = float(input("Introdueix un número: "))
        print("Resultat:", arrel_quadrada(x))
    elif opcio == "6":
        a = float(input("Base: "))
        b = float(input("Exponent: "))
        print("Resultat:", potencia(a, b))
    elif opcio in ["7", "8", "9"]:
        angle = float(input("Introdueix l'angle en graus: "))
        if opcio == "7":
            print("Resultat:", sine(angle))
        elif opcio == "8":
            print("Resultat:", cosine(angle))
        elif opcio == "9":
            print("Resultat:", tangent(angle))
    else:
        print("Opció no vàlida, prova de nou.")
