# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero
numImpares = 0
numPares = 0

numero = int (input("Ingrese un numero o escriba 0 para cancelar: "))

while numero != 0:

    if numero % 2 == 1:
        # aumentar el contador de números impares
        numImpares += 1

    else:
         # aumentar el contador de números pares
        numPares += 1
    # lee el siguiente número
    numero = int (input("Ingrese un numero o escriba 0 para cancelar: "))

print("Numeros impares: ", numImpares)
print("Numeros pares: ", numPares)
