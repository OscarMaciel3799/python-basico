import math
numero_entero = 42             # int
numero_decimal = 3.14159       # float
numero_complejo = 2 + 3j       # complex

# OPERACIONES MATEMATICAS

#Suma
print(1+1)      #2
#Resta
print(5-1)      #4
#Multiplicacion
print(6*3)      #18
#Division Real
print(7/3)      #2.33333333
#Division Entera
print(7//3)     #2
#Modulo
print(9 % 4)    #1
#Potencia
print(2**3)     #8

# OPERACIONES SOBRE SI MISMO
print(numero_entero)        #42
numero_entero +=2           #Incrementamos en 2
print(numero_entero)        #44
numero_entero -=2           #Decrementamos en 2
print(numero_entero)        #42
numero_entero /=2           #Dividimos por 2
print(numero_entero)        #21.0
numero_entero *=2           #Multiplicamos por 2
print(numero_entero)        #42.0

# METODOS MATEMATICOS


# Valor absoluto
numero_negativo = -15
print("abs():", abs(numero_negativo))  # 15

# Redondeo
pi = 3.14159
print("round(pi):", round(pi))         # 3
print("round(pi, 2):", round(pi, 2))   # 3.14

# Potencias
base = 2
exponente = 4
print("pow(2, 4):", pow(base, exponente))  # 16
print("2 ** 4:", base ** exponente)        # 16

# División con cociente y resto
dividendo = 17
divisor = 5
resultado = divmod(dividendo, divisor)
print("divmod(17, 5):", resultado)     # (3, 2)

# Máximo y mínimo
valores = [5, 9, 1, 7, 3]
print("max(valores):", max(valores))  # 9
print("min(valores):", min(valores))  # 1

# Suma de elementos
numeros = [10, 20, 30]
print("sum(numeros):", sum(numeros))  # 60

# Conversión de tipos
texto = "100"
print("int('100'):", int(texto))      # 100
print("float('100'):", float(texto))  # 100.0

# Tipo de dato
valor = 3.14
print("type(3.14):", type(valor))     # <class 'float'>



#MODULO MATH

# Raíz cuadrada
numero = 25
print("math.sqrt(25):", math.sqrt(numero))  # 5.0

# Potencias
print("math.pow(2, 3):", math.pow(2, 3))    # 8.0

# Valor absoluto
print("math.fabs(-7):", math.fabs(-7))      # 7.0

# Redondeos hacia arriba y abajo
decimal = 3.7
print("math.ceil(3.7):", math.ceil(decimal))  # 4
print("math.floor(3.7):", math.floor(decimal))  # 3

# Constantes
print("math.pi:", math.pi)  # 3.141592653589793
print("math.e:", math.e)    # 2.718281828459045

# Logaritmo natural y en base 10
print("math.log(100):", math.log(100))         # Logaritmo natural
print("math.log10(100):", math.log10(100))     # Logaritmo base 10

# Factorial
print("math.factorial(5):", math.factorial(5))  # 120

# Funciones trigonométricas
angulo = math.radians(90)  # convertir a radianes
print("math.sin(90):", math.sin(angulo))       # 1.0
print("math.cos(90):", math.cos(angulo))       # cercano a 0
print("math.tan(90):", math.tan(angulo))       # muy grande (no definido en 90°, pero cercano)

# Hipotenusa
print("math.hypot(3, 4):", math.hypot(3, 4))     # 5.0 (por teorema de Pitágoras)

#Los demás metodos los podemos encontrar en: https://docs.python.org/3/library/math.html