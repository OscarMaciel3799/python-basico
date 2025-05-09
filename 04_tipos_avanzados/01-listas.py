# Listas (list) - Colección ordenada y modificable

# Crear una lista
frutas = ["manzana", "banana", "cereza"]
print("Lista original:", frutas)

# Acceder a elementos
print("Primera fruta:", frutas[0])

# Modificar un elemento
frutas[1] = "naranja"
print("Lista modificada:", frutas)

# Agregar elementos
frutas.append("uva")
print("Con uva:", frutas)

# Insertar en una posición específica
frutas.insert(1, "kiwi")
print("Con kiwi en posición 1:", frutas)

# Eliminar por valor
frutas.remove("manzana")
print("Sin manzana:", frutas)

# Eliminar por índice
frutas.pop(0)
print("Después de pop:", frutas)

# Verificar si un elemento existe
if "cereza" in frutas:
    print("¡Hay cereza!")

# Recorrer la lista
for fruta in frutas:
    print("Fruta:", fruta)

# Longitud
print("Cantidad de frutas:", len(frutas))

# Ordenar
frutas.sort()
print("Ordenadas:", frutas)

# Reversa
frutas.reverse()
print("Reverso:", frutas)

# Lista con diferentes tipos de datos
mezcla = [1, "dos", 3.0, True]
print("Lista mixta:", mezcla)

# Lista de frutas
frutas = ["manzana", "banana", "naranja", "pera", "kiwi", "sandía"]

# Acceso simple
print("Primera fruta:", frutas[0])             # manzana
print("Última fruta:", frutas[-1])             # sandía

# Slicing con rango: desde índice 1 hasta antes del 4 (no incluye el 4)
print("Índices del 1 al 3:", frutas[1:4])       # ['banana', 'naranja', 'pera']

# Slicing desde el inicio hasta el índice 3 (no incluye el 3)
print("Inicio hasta el 3:", frutas[:3])         # ['manzana', 'banana', 'naranja']

# Slicing desde el índice 3 hasta el final
print("Desde el 3 al final:", frutas[3:])       # ['pera', 'kiwi', 'sandía']

# Slicing completo (copia de la lista)
print("Copia completa:", frutas[:])             # ['manzana', 'banana', 'naranja', 'pera', 'kiwi', 'sandía']

# Slicing con paso
print("Cada 2 frutas:", frutas[::2])            # ['manzana', 'naranja', 'kiwi']

# Slicing en reversa
print("Frutas al revés:", frutas[::-1])         # ['sandía', 'kiwi', 'pera', 'naranja', 'banana', 'manzana']
