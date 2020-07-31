numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numero = int(input("Adivina el numero secreto: "))
while numero != numeroSecreto:
    numero += 1 
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Vuelve a introducir un numero: "))
    if numero == numeroSecreto:    #sin el if puede funcionar
        print("¡Bien hecho, muggle! Eres libre ahora")
    

