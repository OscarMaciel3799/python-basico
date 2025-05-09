# Diccionarios (dict) - Colección de pares clave:valor

# Crear un diccionario
persona = {
    "nombre": "Pepito",
    "edad": 28,
    "ciudad": "Chaco"
}

print("Diccionario:", persona)

# Acceder a valores
print("Nombre:", persona["nombre"])
print("Edad (con get):", persona.get("edad"))

# Agregar o modificar valores
persona["edad"] = 29
persona["profesión"] = "Ingeniero"
print("Actualizado:", persona)

# Eliminar claves
persona.pop("ciudad")
print("Sin ciudad:", persona)

# Recorrer claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Claves y valores por separado
print("Claves:", list(persona.keys()))
print("Valores:", list(persona.values()))

# Comprobar existencia
if "nombre" in persona:
    print("La clave 'nombre' existe")

# Longitud
print("Cantidad de claves:", len(persona))
