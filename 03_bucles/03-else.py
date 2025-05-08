# uso de else con bucles for y while

# Uso de else con for
print("For con else:")

frutas = ["manzana", "banana", "pera"]
for fruta in frutas:
    print(f"Comiendo {fruta}")
else:
    print("He terminado de comer todas las frutas.")

print("-" * 30)

# Uso de else con for y break
print("For con break y else:")

for fruta in frutas:
    if fruta == "banana":
        print("Encontré la banana, salgo del bucle.")
        break
else:
    # Este else no se ejecuta porque se interrumpió con break
    print("He terminado de comer todas las frutas.")

print("-" * 30)

# Uso de else con while
print("While con else:")

contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
else:
    print("El contador alcanzó el valor 3, salí del bucle.")

print("-" * 30)

# Uso de else con while y break
print("While con break y else:")

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    if contador == 3:
        print("Contador llegó a 3, salgo del bucle.")
        break
    contador += 1
else:
    # Este else no se ejecuta porque se interrumpió con break
    print("El contador ha alcanzado el valor 5.")

