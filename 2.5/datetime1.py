# Autor: Mohamed Mendou
# Data: 8/11/2025
# Versio: 1
#
# Descripció: Utilitza les funcions de datetime per a saber la data i hora actual i calcular dies fins Nadal
# Instruccions de entrada: 


from datetime import datetime, date

# data i hora actual
ara = datetime.now()
print("Data i hora actual:", ara.strftime("%d/%m/%Y %H:%M"))

# dies fins Nadal
avui = date.today()
nadal = date(avui.year, 12, 25)

# si ja ha passat nadal aquest any → comptem l’any següent
if nadal < avui:
    nadal = date(avui.year + 1, 12, 25)

dies_fins_nadal = (nadal - avui).days

print("Dies fins Nadal:", dies_fins_nadal)
