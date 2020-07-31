# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

numero = int(input("Introduzca un número o escriba -1 para detener: "))

#Si el número no es igual a -1, continuaremos#
while numero != -1:
    if numero > numeroMayor:
        # Sí si, actualiza el mayor númeroNúmero
        numeroMayor = numero
        # Ingresa el siguiente número
    numero = int(input("Introduce un numero o escribe -1 para detenerse: "))
print("El numero mas grande es: ", numeroMayor)
