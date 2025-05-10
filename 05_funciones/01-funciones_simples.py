# Funciones simples

# Declaración de una función simple (Usamos def para definir funciones)
def saludar():
    print("¡Hola, bienvenido a Python!")

# Llamado a la función (Las funciones se ejecutan solo cuando las llamás)
saludar()


# Función que imprime un mensaje personalizado
def saludar_usuario():
    nombre = input("¿Cómo te llamás? ")
    print("Hola", nombre, "¡Bienvenido!")

# Llamado a la función que pide entrada
saludar_usuario()


# Función sin cuerpo (placeholder), útil para estructurar el código
def funcion_vacia():
    pass  # No hace nada por ahora

# Llamado a una función vacía (no hace nada)
funcion_vacia()
