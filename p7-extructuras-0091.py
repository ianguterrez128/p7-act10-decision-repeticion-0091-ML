# if
# Ejemplo 1
# ian gutierrez NC  0091

edad = 20

if edad >= 18:
    print("Es mayor de edad")

# Ejemplo 2

temperatura = 30

if temperatura > 25:
    print("Hace calor")

# if + elif
# Ejemplo 1

calificacion = 85

if calificacion >= 90:
    print("Excelente")
elif calificacion >= 70:
    print("Aprobado")

# Ejemplo 2

edad = 15

if edad >= 18:
    print("Es adulto")
elif edad >= 13:
    print("Es adolescente")

# if + else
# Ejemplo 1

edad = 16

if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")

# Ejemplo 2

numero = 8

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# for
# Ejemplo 1

for numero in range(1, 6):
    print(numero)

# Ejemplo 2

frutas = ["manzana", "plátano", "naranja"]

for fruta in frutas:
    print(fruta)

# while
# Ejemplo 1

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

# Ejemplo 2

numero = 10

while numero >= 1:
    print(numero)
    numero -= 1

    print("programa realizado por ian gutierrez NC = 0091")
