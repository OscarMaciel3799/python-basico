# closures

print("=== CLOSURES en Python ===\n")

# Un closure es una función que recuerda el entorno (variables) en el que fue creada, incluso después de que ese entorno haya finalizado.

def saludar(nombre):
    def mensaje():
        return f"Hola, {nombre}!"  # nombre es recordado
    return mensaje  # devolvemos la función sin ejecutarla

saludo_pepito = saludar("Pepito")
saludo_juanita = saludar("Juanita")

print(saludo_pepito())   # Hola, Pepito!
print(saludo_juanita())  # Hola, Juanita!

# Otro ejemplo: generador de multiplicadores

def multiplicador(factor):
    def multiplica(numero):
        return numero * factor
    return multiplica

por_2 = multiplicador(2)
por_3 = multiplicador(3)

print("\nMultiplicaciones:")
print("5 x 2 =", por_2(5))
print("5 x 3 =", por_3(5))

# ¿Qué pasa si tratamos de acceder al closure?
print("\nVariables retenidas en el closure de por_2:")
print(por_2.__closure__[0].cell_contents)  # Muestra 2, el valor de 'factor' retenido
