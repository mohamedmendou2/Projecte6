preu = float(input("Introdueix el preu del producte (sense IVA): €"))
iva = preu * 0.21
preu_total = preu + iva
print(f"Preu sense IVA: €{preu:.2f}")
print(f"IVA (21%): €{iva:.2f}")
print(f"Preu total: €{preu_total:.2f}")