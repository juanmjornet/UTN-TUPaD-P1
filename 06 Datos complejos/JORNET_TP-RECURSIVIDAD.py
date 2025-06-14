

#Ejercicio 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Ingrese un numero: "))

for i in range(1, num +1):
    print(f"Factorial de {i} = {factorial(i)}")

#Ejercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingresa la posición hasta la cual mostrar la serie Fibonacci: "))

print("Serie Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")
print()

#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = float(input("Ingresa la base: "))
e = int(input("Ingresa el exponente (entero no negativo): "))

print(f"{b} elevado a {e} = {potencia(b, e)}")

#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingresa un número entero positivo en base decimal: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario}")

#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingresa una palabra sin espacios ni tildes: ").lower()
if es_palindromo(texto):
    print(True)
else:
    print(False)

#Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
    
#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        cuenta_actual = 1 if (numero % 10) == digito else 0
        return cuenta_actual + contar_digito(numero // 10, digito)

num = int(input("Ingresa un número entero positivo: "))
dig = int(input("Ingresa el dígito a contar (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en el número {num}.")