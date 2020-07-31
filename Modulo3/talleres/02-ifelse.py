ingresos = float(input('Ingrese el ingreso anual: '))

if ingresos < 85528:
    impuesto = ingresos * 0.18 - 556.02
else :
    impuesto = (ingresos - 85528) *0.32+14839.02
if ingresos < 0.0:
    impuesto = 0.0
    
impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")