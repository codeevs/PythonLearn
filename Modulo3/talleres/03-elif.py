año = int(input("Introdusca la cantidad de dias que tiene el año: "))

if año < 1582:
    print("No dentro del periodo del calendario gregoriano")
else:
    if año % 4 != 0:          #el simbolo ! diferente debe de ir pegado con el simbolo =#
        print("Año comun")
    elif año % 100 != 0:
        print("Año bisiesto")
    elif año % 400 != 0:
        print("Año Comun")
    else:
        print("Año bisiesto")
