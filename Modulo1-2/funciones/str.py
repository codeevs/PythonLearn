#Este tipo de conversión no es en un solo sentido. También se puede convertir un numero a una cadena, lo cual es más fácil y rápido, esta operación es posible hacerla siempre.#
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))
