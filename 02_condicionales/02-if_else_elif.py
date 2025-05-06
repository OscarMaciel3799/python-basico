# CONDICIONALES EN PYTHON

# 1. if simple
edad = int(input("Ingresá tu edad: "))
if edad >= 18:
    print("Sos mayor de edad.")

# 2. if-else
if edad >= 18:
    print("Podés votar.")
else:
    print("Sos menor de edad.")

# 3. if-elif-else
nota = int(input("Ingresá tu nota: "))
if nota >= 9:
    print("Excelente!")
elif nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

# 4. Operador ternario
edad = int(input("Ingresá tu edad nuevamente: "))
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)