# Lista con tres elementos
numeros = [10, 20, 30]

# Desempaquetado simple
a, b, c = numeros
print("a:", a)  # 10
print("b:", b)  # 20
print("c:", c)  # 30

# Desempaquetado con *
numeros = [1, 2, 3, 4, 5]

primero, *resto = numeros
print("Primero:", primero)   # 1
print("Resto:", resto)       # [2, 3, 4, 5]

*inicio, ultimo = numeros
print("Inicio:", inicio)     # [1, 2, 3, 4]
print("Último:", ultimo)     # 5

primero, *medio, ultimo = numeros
print("Primero:", primero)   # 1
print("Medio:", medio)       # [2, 3, 4]
print("Último:", ultimo)     # 5

# También se puede usar con strings
letras = ["a", "b", "c"]
x, y, z = letras
print(x, y, z)  # a b c

# Desempaquetado en bucles
pares = [(1, 2), (3, 4), (5, 6)]
for x, y in pares:
    print(f"x: {x}, y: {y}")


# TUPLAS
coordenadas = (100, 200)
x, y = coordenadas
print("Tupla => x:", x, "y:", y)

# TUPLA con * resto
tupla = (1, 2, 3, 4, 5)
a, *b, c = tupla
print("Tupla con * => a:", a, "b:", b, "c:", c)

# STRINGS (los strings son iterables, se desempaquetan como listas de caracteres)
letras = "abc"
x, y, z = letras
print("String => x:", x, "y:", y, "z:", z)

# SETS (desempaquetar es posible, pero el orden no está garantizado)
colores = {"rojo", "verde", "azul"}
a, b, c = colores
print("Set => a:", a, "b:", b, "c:", c)

# DICCIONARIOS
persona = {"nombre": "Ana", "edad": 30}

# Desempaquetar claves
clave1, clave2 = persona
print("Diccionario (claves) =>", clave1, clave2)

# Desempaquetar claves y acceder a valores
for clave in persona:
    print(f"{clave} => {persona[clave]}")

# Desempaquetar items
for clave, valor in persona.items():
    print(f"{clave} = {valor}")

# BUCLES CON TUPLAS
puntos = [(1, 2), (3, 4), (5, 6)]
for x, y in puntos:
    print(f"Tupla en bucle => x: {x}, y: {y}")

# BUCLES CON DICCIONARIOS
for clave, valor in persona.items():
    print(f"Bucle con diccionario => {clave}: {valor}")