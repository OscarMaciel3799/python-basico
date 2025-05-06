# Operadores de comparación (comparadores lógicos) 

a = 10
b = 5

# Igualdad
print("¿a es igual a b?:", a == b)  # False

# Desigualdad
print("¿a es distinto de b?:", a != b)  # True

# Mayor que
print("¿a es mayor que b?:", a > b)  # True

# Menor que
print("¿a es menor que b?:", a < b)  # False

# Mayor o igual que
print("¿a es mayor o igual que b?:", a >= b)  # True

# Menor o igual que
print("¿a es menor o igual que b?:", a <= b)  # False

# Comparación de strings
nombre1 = "Ana"
nombre2 = "Carlos"

print("¿nombre1 es igual a nombre2?:", nombre1 == nombre2)  # False
print("¿nombre1 es menor que nombre2?:", nombre1 < nombre2)  # True (orden alfabético)

# Comparación estricta entre distintos tipos
print(2 == "2")        # False (int vs str)
print(2 == int("2"))   # True (ambos int)
print(2 != "2")        # True (int vs no_str)
print(2 != 2)          # False (int vs no_int)

# Pare evaluar un condicion compuesta podemos usar AND, OR, NOT

# and
print("True and True: " , True and True)   # True
print("True and False: ", True and False)  # False

# or
print("True or False: ", True or False)   # True
print("False or False: ", False or False)  # False

# not
print("not True: ", not True)        # False
print("not False: ", not False)       # True

edad = 20
es_estudiante = True

if edad > 18 and es_estudiante:
    print("Es mayor de edad y estudiante.")

if edad < 18 or es_estudiante:
    print("Es menor o estudiante.")

if not es_estudiante:
    print("No es estudiante.")

# Cadena de comparadores

edad = 25

# Verificar si la edad está entre 18 y 30 (inclusive)
if 18 <= edad <= 30:
    print("Edad dentro del rango.")

# Comprobando si un número está fuera de un rango
numero = 50
if not (10 <= numero <= 40):
    print("El número está fuera del rango 10-40.")

# Comparaciones de mayor a menor
x = 5
if 10 > x > 0:
    print("x está entre 0 y 10")
