import random


#Ejercicio 1:
for i in range(101):
    print(i)

#Ejercicio 2:
numero = input("Ingrese un numero entero: ")
cantidad = len(numero)
print("La cantidad de digitos que tiene el numero ingresado es de: ", cantidad)

#Ejercicio 3:
valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor: "))
if valor_1 > valor_2:
    valor_1, valor_2 = valor_2, valor_1
suma = 0
for num in range(valor_1 + 1, valor_2):
    suma += num
print("La suma de los números es:", suma)

#Ejercicio 4:
suma_secuencia = 0
while True:
    entero = int(input("Ingrese un numero entero (con 0 corta): "))
    if entero == 0:
        break
    suma_secuencia += entero
print("La suma total es de: ", suma_secuencia)

#Ejercicio 5:
aleatorio = random.randint(0,9)
contador = 0
intento = int(input("Ingrese un numero: "))
while intento != aleatorio:
    contador += 1
    if intento == aleatorio:
        print("Ha adivinado el numero")
    else:
        print("Siga intentando")
print("Adivinó el numero en un total de: ", contador, "intentos.")

#Ejercicio 6:
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7:
positivo = int(input("Ingrese un numero positivo: "))
while positivo < 0:
    positivo = int(input("Ingrese un numero positivo: "))
sumatoria = 0
for i in range(positivo + 1):
    sumatoria += i
print("La suma es: ", sumatoria)

#Ejercicio 8:
pares, impares, positivos, negativos = 0, 0, 0, 0
for i in range(100):
    ingreso = int(input("Ingrese un numero: "))
    if ingreso % 2 == 0:
        pares += 1
    else:
        impares += 1
    if ingreso > 0:
        positivos += 1
    elif ingreso < 0:
        negativos += 1
print("Pares: ", pares)
print("Impares: ", impares)
print("Positivos: ", positivos)
print("Negativos: ", negativos)

#Ejercicio 9:
contador_suma = 0
total = 100
for i in range(total):
    num_ingresado = int(input("Ingrese un numero: "))
    contador_suma += num_ingresado
media = contador_suma / total
print("La media de los ", total, "numeros ingresados es: ", media)

#Ejercicio 10:
numero_sin_invertir = input("Ingrese un número entero: ")
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)