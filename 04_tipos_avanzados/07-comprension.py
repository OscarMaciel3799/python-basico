# COMPRENSIÓN DE LISTAS
numeros = [1, 2, 3, 4, 5, 6]

# Cuadrados de los números
cuadrados = [n ** 2 for n in numeros]
print("Cuadrados:", cuadrados)  # [1, 4, 9, 16, 25, 36]

# Números pares
pares = [n for n in numeros if n % 2 == 0]
print("Pares:", pares)  # [2, 4, 6]

# Convertir a string
como_texto = [str(n) for n in numeros]
print("Como texto:", como_texto)  # ['1', '2', '3', '4', '5', '6']

# COMPRENSIÓN DE SETS
letras = "banana"

# Crear un set de letras únicas (sin duplicados)
unicas = {letra for letra in letras}
print("Letras únicas:", unicas)  # {'b', 'a', 'n'}

# COMPRENSIÓN DE DICCIONARIOS
nombres = ["Ana", "Luis", "Carlos"]
edades = [22, 30, 27]

# Combinar listas en un diccionario
personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
print("Diccionario personas:", personas)            # {'Ana': 22, 'Luis': 30, 'Carlos': 27}

# Filtrar solo mayores de 25
mayores = {k: v for k, v in personas.items() if v > 25}
print("Mayores de 25:", mayores)                    # {'Luis': 30, 'Carlos': 27}
