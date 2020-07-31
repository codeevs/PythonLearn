#Ejercicio 1#
x = 5
y = 10
z = 8

print(x > y)
print(y > z)

#Ejercicio 2
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

#Ejercicio 3
x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

#Ejercicio 4
x = 10
if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

#Ejercicio 5
x = "1"

if x == 1:
    print("uno")
elif x == "1":
    if int (x) > 1:
        print("dos")
    elif int (x) < 1:
        print("tres")
    else:
        print("cuatro")
if int (x) == 1:
    print("cinco")
else:
    print("seis")

#Ejercicio 6
x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int (z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro")
