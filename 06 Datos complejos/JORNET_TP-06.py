

#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())

#Ejercicio 4
agenda = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("\nIngresá el nombre del contacto que querés buscar: ")
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontró un contacto llamado '{consulta}'.")

#Ejercicio 5
frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", contador_palabras)

#Ejercicio 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    print(f"Ingresá 3 notas para {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print("\nPromedios:")
for nombre in alumnos:
    promedio = sum(alumnos[nombre]) / 3
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio 9
eventos = {
    ("Lunes", "10:00"): "Reunion",
    ("Martes", "15:00"): "Clase de ingles"
}

dia = input("Ingresá el día que querés consultar: ")
hora = input("Ingresá la hora que querés consultar: ")

busqueda = (dia, hora)
if busqueda in agenda:
    print(f"Hay una actividad: {agenda[busqueda]}")
else:
    print("No hay actividad registrada en ese día y hora.")

#Ejercicio 10
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Francia': 'París',
    'Italia': 'Roma',
    'Japón': 'Tokio'
}

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario invertido: ", capitales_paises)