# contexto alcance
"""
Explicación de los conceptos:
Alcance local: Las variables definidas dentro de una función o bloque de código 
               solo son accesibles dentro de ese bloque o función.

Alcance global: Las variables definidas fuera de cualquier función 
                son accesibles desde cualquier parte del código, 
                pero dentro de las funciones solo si no se definen 
                otras variables con el mismo nombre.

Palabra clave global: Usada dentro de una función para indicar que la variable a modificar es global, 
                      lo que permite cambiar su valor fuera de la función.
                      ** SE CONSIDERA MALA PRACTICA, SIMPRE TRABAJAR CON LAS VARIABLES LOCALES DE LA FUNCION**

Funciones anidadas: Las funciones dentro de otras funciones pueden acceder a las variables definidas 
                    en la función externa, pero no al revés (a menos que se usen palabras clave como nonlocal).
"""

# Alcance de las variables en Python

# Variable global
x = 10  # x es una variable global

def funcion_local():
    # Variable local dentro de la función
    y = 5  # y es local
    print("Dentro de la función, x:", x)  # x es global, pero accesible dentro
    print("Dentro de la función, y:", y)  # y es local, accesible solo dentro

# Llamamos la función
funcion_local()

# Fuera de la función, solo podemos acceder a x (la global), pero no a y
print("Fuera de la función, x:", x)
# print("Fuera de la función, y:", y)  # Esto daría error porque y es local y no existe fuera de la función

# Modificando la variable global dentro de una función
def modificar_global():
    global x  # Usamos la palabra clave global para modificar la variable global
    x = 20  # Cambia el valor de x a 20
    print("Dentro de la función, x (modificada):", x)

# Llamamos a la función que modifica la variable global
modificar_global()

# Fuera de la función, la variable global x ha cambiado
print("Fuera de la función, x (modificada):", x)

# Ejemplo de función anidada
def funcion_externa():
    a = 2  # Variable local a funcion_externa

    def funcion_interna():
        b = 3  # Variable local a funcion_interna
        print("Dentro de la función interna, a:", a)  # Accede a 'a' de la función externa
        print("Dentro de la función interna, b:", b)  # Accede a 'b' de la función interna
    
    funcion_interna()  # Llamamos a la función interna desde la externa

# Llamamos a la función externa que contiene a la interna
funcion_externa()

# Variables en bucles
contador = 0  # Variable global
for i in range(3):
    contador += i  # La variable contador se modifica en cada iteración
print("Valor final de contador después del bucle:", contador)  # Accesible fuera del bucle
