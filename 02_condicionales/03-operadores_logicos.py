# Operadores lógicos en Python

# 1. AND: ambas condiciones deben ser verdaderas
edad = 25
tiene_licencia = True
puede_conducir = edad >= 18 and tiene_licencia
print("¿Puede conducir?", puede_conducir)  # True

# 2. OR: al menos una condición debe ser verdadera
tiene_pasaporte = False
tiene_dni = True
puede_viajar = tiene_pasaporte or tiene_dni
print("¿Puede viajar?", puede_viajar)  # True

# 3. NOT: invierte el valor lógico
es_menor = edad < 18
print("¿Es mayor de edad?", not es_menor)  # True

# 4. Combinando todo
usuario_valido = True
clave_correcta = False

puede_ingresar = usuario_valido and clave_correcta
print("¿Puede ingresar al sistema?", puede_ingresar)  # False

# Ejemplo más complejo
tiene_permiso = False
es_admin = True

acceso = (tiene_permiso or es_admin) and not es_menor
print("¿Tiene acceso total?", acceso)  # True

# 5.Cadena de comparadores

# En lugar de escribir esto:
print(edad > 18 and edad < 30)  # True

# Podemos encadenar comparadores así:
print(18 < edad < 30)  # True
