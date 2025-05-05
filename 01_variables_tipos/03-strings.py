# METODOS DE STRINGS

texto = "Hola, Mundo!  "

# Convertir a mayúsculas
print(texto.upper())           # "HOLA, MUNDO!  "

# Convertir a minúsculas
print(texto.lower())           # "hola, mundo!  "

# Capitalizar (primera letra en mayúscula)
print(texto.capitalize())      # "Hola, mundo!  " (ojo, solo la primera letra del string)

# Título (primera letra de cada palabra en mayúscula)
print(texto.title())           # "Hola, Mundo!  "

# Reemplazar texto
print(texto.replace("Mundo", "Python"))  # "Hola, Python!  "

# Buscar texto 
# (retorna el índice o -1)
print(texto.find("Mundo"))     # 6
print(texto.find("Adiós"))     # -1
#(retorna True o False)
print("Mundo" in texto)        # True
print("adiós" in texto)        # False

# Contar ocurrencias
print(texto.count("o"))        # 2

# Eliminar espacios al principio y final
print(texto.strip())           # "Hola, Mundo!"

# Unir una lista de palabras con un separador
palabras = ["Hola", "mundo"]
print(" ".join(palabras))      # "Hola mundo"

# Separar una cadena en lista (por defecto por espacio)
print(texto.strip().split())   # ["Hola,", "Mundo!"]

# Verifica si empieza o termina con algo
print(texto.startswith("  Hola"))    # False
print(texto.endswith("!  "))         # True

# Verificar si es alfabético, numérico, etc.
print("Python".isalpha())      # True
print("123".isdigit())         # True
print("abc123".isalnum())      # True

#Devuelve la longitud de una cadena
print(len(texto))  # 14

#Substrings cadena[inicio:fin]
print(texto[0:4])     # "Hola"
print(texto[5:])      # " Mundo!  " (desde el índice 5 hasta el final)
print(texto[:4])      # "Hola"      (desde el inicio hasta antes del índice 4)
print(texto[-5:])     # " do!  "    (últimos 5 caracteres)

#Dar un salto
print(texto[::2])     # "Hl,Mno"    (salta de a 2)
