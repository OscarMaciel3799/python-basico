# bucle WHILE 

# Uso básico de while con contador
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

print("-" * 30)

# Usando break para salir del bucle
contador = 0
while True:  # Bucle infinito
    if contador == 5:
        print("Contador alcanzó 5, saliendo del bucle.")
        break
    print(f"Contador: {contador}")
    contador += 1

print("-" * 30)

# Usando continue para saltarse la iteración
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        print("Salteando el 3.")
        continue
    print(f"Contador: {contador}")

print("-" * 30)

# while con condiciones más complejas
numero = 0
while numero <= 10:
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
    numero += 1

print("-" * 30)

# Simulando una entrada de usuario para continuar el bucle
respuesta = ""
while respuesta.lower() != "salir":
    respuesta = input("Escribe 'salir' para terminar: ")
    print(f"Respuesta: {respuesta}")
    
print("-" * 30)

# Ejemplo de bucle while con listas (aunque no es tan común en Python)
nombres = ["Alice", "Bob", "Charlie"]
indice = 0
while indice < len(nombres):
    print(f"Nombre: {nombres[indice]}")
    indice += 1
