# Tuplas (tuple) - Colección ordenada e inmutable

# Crear una tupla
coordenadas = (10.5, 20.3)
print("Tupla:", coordenadas)

# Acceder a elementos
print("Primer valor:", coordenadas[0])

# Longitud de la tupla
print("Cantidad de elementos:", len(coordenadas))

# Tupla con un solo elemento (necesita la coma)
una_sola = ("hola",)
print("Tupla de un solo elemento:", una_sola)

# Convertir lista a tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print("Tupla convertida:", tupla_convertida)

# Desempaquetado de tupla
x, y = coordenadas
print("Desempaquetado -> x:", x, ", y:", y)
