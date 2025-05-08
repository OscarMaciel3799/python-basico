# Bucle for 
# Recorriendo una lista
frutas = ["manzana", "banana", "naranja"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")

print("-" * 30)

# Recorriendo un string
mensaje = "Hola"
for letra in mensaje:
    print(letra)
    
print("-" * 30)

# break: salir del bucle
for fruta in frutas:
    if fruta == "banana":
        print("Encontré la banana, salgo del bucle.")
        break
    print(f"Procesando {fruta}")

print("-" * 30)

# continue: saltarse una iteración
for fruta in frutas:
    if fruta == "banana":
        print("Salteando la banana.")
        continue
    print(f"Comiendo {fruta}")

print("-" * 30)


# Usando range() con for
for numero in range(5):  # 0 a 4
    print(f"Número: {numero}")

print("-" * 30)

# Usando range con inicio y fin
for i in range(2, 5):
    print(f"Índice entre 2 y 4: {i}")

print("-" * 30)

# Usando range con paso
for i in range(0, 10, 2):
    print(f"Número par: {i}")

print("-" * 30)

# Con enumerar: índice y valor
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
    
print("-" * 30)

# Recorriendo una lista con índice
for i in range(len(frutas)):
    print(f"Índice {i} contiene: {frutas[i]}")

print("-" * 30)

# Con zip: recorrer dos listas al mismo tiempo
precios = [100, 200, 300]
for fruta, precio in zip(frutas, precios):
    print(f"La {fruta} cuesta {precio} pesos")