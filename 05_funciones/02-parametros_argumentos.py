# Parámetros y Argumentos
# Parametros es el nombre de la variable dentro de la funcion
# Argumento es el valor que se le pasa a la funcion al ser invocada

# Función con un parámetro
def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamado pasando un argumento
saludar("Oscar")


# Función con varios parámetros
def presentar(nombre, edad):
    print(f"Me llamo {nombre} y tengo {edad} años.")

presentar("Ana", 30)


# Función con parametros por defecto
def saludar_con_saludo(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar_con_saludo("Carlos")
saludar_con_saludo("Lucía", "Buenas tardes")


# Parámetros nombrados (keyword arguments)
presentar(edad=25, nombre="Laura")


# Función con cantidad variable de argumentos (tupla)
def mostrar_amigos(*amigos):
    print("Mis amigos son:")
    for amigo in amigos:
        print("-", amigo)

mostrar_amigos("Ana", "Luis", "Pedro")


# Función con argumentos nombrados variables (diccionario)
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Juan", edad=28, ciudad="Rosario")
