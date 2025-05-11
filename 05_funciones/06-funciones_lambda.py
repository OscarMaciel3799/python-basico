# Funciones_lambda

# Las funciones lambda son funciones anónimas, cortas y de una sola línea

# Ejemplo básico: sumar dos números
sumar = lambda x, y: x + y
print("Suma:", sumar(3, 5))  # 8

# Multiplicar por 10
multiplicar_por_diez = lambda n: n * 10
print("Multiplicar:", multiplicar_por_diez(7))  # 70

# Usando lambda con nombres divertidos
presentar = lambda nombre: f"Hola, soy {nombre}"
print(presentar("Pepito"))  # Hola, soy Pepito

# Con condicional ternario
mayor_de_edad = lambda edad: "Mayor" if edad >= 18 else "Menor"
print("Juanita es:", mayor_de_edad(20))  # Mayor

# Lambda en una lista con map()
nombres = ["Lupita", "Anita", "Carlitos"]
saludos = list(map(lambda nombre: f"¡Hola {nombre}!", nombres))
print("Saludos:", saludos)

# Lambda con filter()
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Pares:", pares)

# Ordenando una lista de tuplas (nombre, edad)
personas = [("Juanita", 20), ("Pepito", 15), ("Carlitos", 30)]
ordenadas = sorted(personas, key=lambda persona: persona[1])
print("Ordenado por edad:", ordenadas)
