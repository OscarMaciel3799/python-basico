# **kwargs: recibe múltiples argumentos nombrados en forma de diccionario.

# Esta función acepta cualquier cantidad de argumentos con nombre
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Oscar", edad=29, ciudad="Corrientes")


# Podés combinarlos con otros argumentos normales
def saludar_usuario(saludo, **kwargs):
    print(saludo)
    for clave, valor in kwargs.items():
        print(f"{clave} -> {valor}")

saludar_usuario("¡Hola!", nombre="Laura", ocupacion="Dev", idioma="Python")
