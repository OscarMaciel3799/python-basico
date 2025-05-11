# Retorno de valores

# Función que retorna la suma de dos números
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print("Resultado:", resultado)


# Podés guardar el valor y reutilizarlo
def obtener_nombre_completo(nombre, apellido):
    return f"{nombre} {apellido}"

nombre_completo = obtener_nombre_completo("Oscar", "Maciel")
print("Nombre completo:", nombre_completo)


# Retornar múltiples valores como tupla
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones(10, 3)
print("Suma:", s)
print("Resta:", r)


# También se puede retornar listas, diccionarios, etc.
def info_usuario(nombre, edad):
    return {"nombre": nombre, "edad": edad}

usuario = info_usuario("Pepita", 28)
print(usuario)
