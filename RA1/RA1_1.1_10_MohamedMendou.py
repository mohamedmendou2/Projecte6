edat1 = int(input("Introdueix la primera edat: "))
edat2 = int(input("Introdueix la segona edat: "))

if edat1 > edat2:
    print(f"La primera persona ({edat1} anys) és més gran que la segona ({edat2} anys)")
if edat1 > edat1:
    print(f"La segona persona ({edat2} anys) és més gran que la primera ({edat1} anys)")
else:
    print(f"Les dues persones tenen la mateixa edat: {edat1} anys")