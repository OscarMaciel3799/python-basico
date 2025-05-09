# Conjuntos (set) - Colección desordenada, sin elementos duplicados

# Crear un conjunto
numeros = {1, 2, 3, 4, 5}
print("Conjunto:", numeros)

# Agregar un elemento
numeros.add(6)
print("Con 6:", numeros)

# Eliminar un elemento (sin error si no existe)
numeros.discard(3)
print("Sin 3:", numeros)

# Eliminar un elemento (con error si no existe)
numeros.remove(2)
print("Sin 2:", numeros)

# Limpiar el conjunto
copia = numeros.copy()
copia.clear()
print("Copia vacía:", copia)

# Operaciones de conjuntos
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

# Unión
print("Unión:", pares.union(impares))

# Intersección
print("Intersección (vacía):", numeros.intersection(pares))

# Diferencia
print("Diferencia:", numeros.difference(pares))
