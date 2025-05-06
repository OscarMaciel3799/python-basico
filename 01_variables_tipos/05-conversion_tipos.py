# Conversión de tipos

# input siempre devuelve un string
dato = input("Ingresá un número: ")
print("Tipo original:", type(dato))  # <class 'str'>

# ✅ Convertir a entero
numero = int(dato)
print("Como entero:", numero, "| Tipo:", type(numero))  # <class 'int'>

# ✅ Convertir a decimal
decimal = float(dato)
print("Como flotante:", decimal, "| Tipo:", type(decimal))  # <class 'float'>

# ✅ Convertir número a string
texto = str(numero)
print("Número como string:", texto, "| Tipo:", type(texto))  # Tipo: <class 'str'>

# ✅ Convertir a booleano
# Ojo: cualquier string no vacío devuelve True
valor = bool(dato)
print("Como booleano:", valor)      #True

# 🧪 Ejemplo de error
try:
    falla = int("hola")
except ValueError:
    print("❌ Error: no se puede convertir 'hola' a entero.")

# ✅ Convertir un número a string para concatenar
edad = 29
print("Tengo " + str(edad) + " años.")

# ✅ f-strings también ayudan con conversiones implícitas
print(f"Tengo {edad} años.")  # Python convierte edad a str automáticamente
