# LISTAS
frutas = ["manzana", "banana", "naranja"]

# Verificar si un elemento está en la lista
print("banana" in frutas)  # True
print("pera" in frutas)    # False

# Obtener índice (devuelve error si no está, por eso usamos try)
try:
    indice = frutas.index("naranja")
    print("Índice de 'naranja':", indice)
except ValueError:
    print("No se encontró la fruta.")

# TUPLAS
numeros = (1, 2, 3, 4, 5)

# Verificar existencia
print(3 in numeros)    # True
print(10 in numeros)   # False

# Obtener índice
if 4 in numeros:
    print("Índice de 4:", numeros.index(4))

# SETS
colores = {"rojo", "verde", "azul"}

# Verificación de existencia (muy eficiente en sets)
print("verde" in colores)  # True
print("negro" in colores)  # False

# DICCIONARIOS
persona = {
    "nombre": "Lucía",
    "edad": 28,
    "ciudad": "Córdoba"
}

# Verificar si una clave existe
print("edad" in persona)    # True
print("altura" in persona)  # False

# Verificar si un valor existe
print(28 in persona.values())  # True
print("Rosario" in persona.values())  # False

# Buscar con get para evitar errores si no existe
print(persona.get("nombre"))      # Lucía
print(persona.get("altura", "No definida"))  # No definida
