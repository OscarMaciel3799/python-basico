# Condicionales anidados
edad = 20
tiene_dni = True

if edad >= 18:
    if tiene_dni:
        print("Puede ingresar al club.")
    else:
        print("Necesitás DNI para ingresar.")
else:
    print("Sos menor de edad, no podés ingresar.")

print("-" * 30)

# Bucles anidados (ejemplo: tabla de multiplicar)
print("Tabla de multiplicar del 1 al 3:")

for i in range(1, 4):  # 1, 2, 3
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("--- Fin de tabla del", i)

print("-" * 30)

# Combinación de bucle con condicional anidado
print("Números pares entre 1 y 10:")

for num in range(1, 11):
    if num % 2 == 0:
        if num > 5:
            print(f"{num} es par y mayor que 5")
        else:
            print(f"{num} es par y menor o igual a 5")

