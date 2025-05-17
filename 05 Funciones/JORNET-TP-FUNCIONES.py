import math


#Ejercicio 1:
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Ejercicio 2:
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)

#Ejercicio 3:
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 4:
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(num)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

x = float(input("Ingrese el primer número: "))
y = float(input("Ingrese el segundo número: "))

sum, res, mul, div = operaciones_basicas(x, y)
print(f"Suma: {sum}")
print(f"Resta: {res}")
print(f"Multiplicación: {mul}")
print(f"División: {div}")

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Ingrese la temperatura en grados Celsius: "))
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C equivalen a {temp_f:.2f}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {promedio:.2f}")