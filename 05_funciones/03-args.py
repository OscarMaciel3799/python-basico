# *args: recibe múltiples argumentos en forma de tupla.

# Esta función puede recibir cualquier cantidad de argumentos
def sumar_todos(*numeros):
    resultado = sum(numeros)
    print(f"La suma es: {resultado}")

sumar_todos(1, 2, 3)
sumar_todos(5, 10, 15, 20)


# Ejemplo accediendo a los valores de *args como una tupla
def mostrar_posiciones(*args):
    for i, valor in enumerate(args):
        print(f"Posición {i}: {valor}")

mostrar_posiciones("a", "b", "c")
