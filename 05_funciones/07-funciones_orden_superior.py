from functools import reduce
# funciones_orden_superior

print("=== Funciones de orden superior ===")

# Las funciones de orden superior pueden:
# 1. Recibir funciones como argumento
# 2. Retornar funciones

print("\n--- Función que recibe otra función ---")

def saludar():
    print("Hola desde la función saludar()")

def ejecutar_funcion(funcion):
    print("Ejecutando función pasada como argumento:")
    funcion()

# Pasamos una función como argumento
ejecutar_funcion(saludar)

print("\n--- Función que retorna otra función ---")

def crear_saludo():
    def saludo_personalizado():
        print("Hola, esto es un saludo personalizado.")
    return saludo_personalizado

# Retornamos y guardamos la función
nueva_funcion = crear_saludo()

# Ejecutamos la nueva función
nueva_funcion()

print("\n--- Función que recibe y retorna funciones (composición) ---")

def envoltorio(funcion):
    def modificada():
        print("Antes de ejecutar la función...")
        funcion()
        print("Después de ejecutar la función...")
    return modificada

def despedir():
    print("Chau chau, hasta luego!")

nueva = envoltorio(despedir)
nueva()



# map(): aplica una función a cada elemento de una secuencia
# En este caso, eleva al cuadrado cada número
numeros = [1, 2, 3]
cuadrados = list(map(lambda x: x**2, numeros))
print("map:", cuadrados)  # [1, 4, 9]

# filter(): filtra los elementos según una condición
# Acá, devuelve solo los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("filter:", pares)  # [2]

# reduce(): aplica una función acumulativa a los elementos
# Multiplica todos los números de la lista
producto = reduce(lambda x, y: x * y, numeros)
print("reduce:", producto)  # 6 (1 * 2 * 3)

# any(): devuelve True si al menos un valor es verdadero
# Ideal para verificar si "hay al menos uno válido"
valores = [0, False, 3, None]
hay_verdadero = any(valores)
print("any:", hay_verdadero)  # True (porque 3 es verdadero)

# all(): devuelve True solo si todos los valores son verdaderos
# Útil para validar condiciones múltiples
todo_verdadero = all([1, True, "Hola"])
print("all:", todo_verdadero)  # True

# sorted(): ordena una secuencia, opcionalmente con una función key
# Ordena los nombres por longitud (cantidad de letras)
personas = ["Juan", "Ana", "Zoe"]
ordenadas = sorted(personas, key=lambda x: len(x))
print("sorted con key:", ordenadas)  # ['Ana', 'Juan', 'Zoe']

# zip(): combina elementos de varias listas en tuplas
# Une nombres y edades por posición
nombres = ["Ana", "Luis"]
edades = [28, 32]
emparejados = list(zip(nombres, edades))
print("zip:", emparejados)  # [('Ana', 28), ('Luis', 32)]
