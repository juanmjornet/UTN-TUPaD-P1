import statistics
import random


#Ejercicio 1
edad = int(input("Ingrese la edad del usuario: "))
if edad > 18:
    print("Usted es mayor de edad")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota > 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor ingresar un numero par.")

#Ejercicio 4
años = int(input("Ingrese la edad del usuario: "))
if años < 12:
    print("Categoria: Niño")
elif años >= 12 and años < 18:
    print("Categoria: Adolescente")
elif años >= 18 and años < 30:
    print("Categoria: Adulto Joven")
else:
    print("Categoria: Adulto Mayor")

#Ejercicio 5
contraseña = int(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6
from statistics import mode, median, mean
aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(aleatorios)
mediana = median(aleatorios)
media = mean(aleatorios)
if media > mediana and mediana > moda:
    print("Sesgo Positivo o A La Derecha")
elif media < mediana and mediana < moda:
    print("Sesgp Negativo o A La Izquierda")
elif media == mediana == moda:
    print("Sin Sesgo")

#Ejercicio 7
frase = input("Ingrese una frase o palabra: ")
ultimo = frase[-1]
vocales = ('A','E','I','O','U','a','e','i','o','u')
if ultimo in vocales:
    print(frase + "!")
else:
    print(frase)

#Ejercicio 8
nombre = input("Ingrese su nombre : ")
print("Seleccione una Opcion")
print("Opcion 1: Nombre en Mayusculas")
print("Opcion 2: Nombre en minusculas")
print("Opcion 3: Nombre con primer letra en Mayusculas")
opcion = int(input("Seleccione una Opcion: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
else:
    print(nombre.title())

#Ejercicio 9
magnitud = int(input("Ingrese la magnitud del terremoto: "))
if magnitud > 3:
    print("Muy Leve")
elif 4 > magnitud >= 3:
    print("Leve")
elif 5 > magnitud >= 4:
    print("Moderado")
elif 6 > magnitud >= 5:
    print("Fuerte")
elif 7 > magnitud >= 6:
    print("Muy Fuerte")
else:
    print("Extremo")

#Ejercicio 10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))
fecha = (mes, dia)
if (fecha >= (12, 21)) or (fecha <= (3, 20)):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (fecha >= (3, 21)) and (fecha <= (6, 20)):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (fecha >= (6, 21)) and (fecha <= (9, 20)):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (fecha >= (9, 21)) and (fecha <= (12, 20)):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = None

if estacion_norte is None:
    print("Fecha no válida.")
elif hemisferio == "N":
    print(f"Te encuentras en {estacion_norte}.")
elif hemisferio == "S":
    print(f"Te encuentras en {estacion_sur}.")
else:
    print("Hemisferio no válido. Usa 'N' para norte o 'S' para sur.")