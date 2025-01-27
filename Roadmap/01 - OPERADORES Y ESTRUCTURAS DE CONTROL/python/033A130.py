# 01 OPERADORES Y ESTRUCTURAS DE CONTROL
# ¡Operadores en Python!

# Operadores Aritméticos

# Suma de strings:
"""
Al sumar dos strings, estos se concatenan. 
Ten cuidado con los espacios que puedan estar presentes en las cadenas.
"""
print("Hello" + " " + "world")
print("Hello " + "world")
print("Hello" + " world")

# Uso de variables para concatenar strings
variable_string_1 = "Hello"
variable_string_2 = "world"
variable_espacio = " "

# Sin incluir un espacio, el resultado será "Helloworld".
print(f"La suma de variable_string_1 + variable_string_2 = {variable_string_1 + variable_string_2}")

# Agregar un espacio usando una variable o directamente sumándolo como string.
print(f"La suma de variable_string_1 + variable_espacio + variable_string_2 = {variable_string_1 + variable_espacio + variable_string_2}")

# Operador aritmético de suma:
"""
La interpolación permite ejecutar operaciones dentro de una cadena.
La `f` indica que es una cadena formateada, y las `{}` evalúan expresiones o variables.
"""
print(f"Suma: 10 + 3 = {10 + 3}")

# Suma con variables (int)
numero_1 = 9
numero_2 = 4
print(f"Suma: numero_1 + numero_2 = {numero_1 + numero_2}")

# Valor de una variable que contiene el resultado de una suma
suma = 2 + 21
print(f"La variable suma = 2 + 21 = {suma}")

# Suma de un número entero y un número flotante
"""
Cuando se suma un entero y un flotante, el resultado se convierte automáticamente en flotante.
"""
numero_entero = 10
numero_flotante = 3.33333333
print(f"La suma de numero_entero {numero_entero} + numero_flotante {numero_flotante} = {numero_entero + numero_flotante}")

suma_numero_int_flot = numero_entero + numero_flotante
print(f"El tipo de dato del resultado es {type(suma_numero_int_flot)}")

# Suma acumulativa (uso de +=)
"""
Este operador incrementa el valor de una variable acumulando su valor con otro.
"""
acumulador = 5
acumulador += 3  # Equivalente a: acumulador = acumulador + 3
print(f"Suma acumulativa: acumulador += 3 → {acumulador}")

# Suma de valores negativos
"""
Python maneja correctamente números negativos en las operaciones.
"""
negativo_1 = -7
negativo_2 = -3
print(f"Suma de negativos: {negativo_1} + {negativo_2} = {negativo_1 + negativo_2}")

# Suma de booleanos
"""
En Python, True equivale a 1 y False a 0, por lo que se pueden sumar como enteros.
"""
print(f"Suma de booleanos: True + False = {True + False}")
print(f"Suma de booleanos: True + True = {True + True}")
print(f"Suma de booleanos: False + False = {False + False}")

# Suma en listas con sum()
"""
La función sum() permite sumar todos los elementos de una lista de números.
"""
lista_numeros = [1, 2, 3, 4, 5]
print(f"Suma de elementos en una lista: {lista_numeros} = {sum(lista_numeros)}")

# Operador aritmético de resta

# Resta directa
print(f"Resta: 10 - 3 = {10 - 3}")

# Resta con variables (int)
print(f"Resta: numero_1 - numero_2 = {numero_1 - numero_2}")

# Resultado en una variable
resta = 21 - 2
print(f"La variable resta = 21 - 2 = {resta}")

# Resta de un número entero y un número flotante
print(f"La resta de numero_entero {numero_entero} - numero_flotante {numero_flotante} = {numero_entero - numero_flotante}")

resta_numero_int_flot = numero_entero - numero_flotante
print(f"El tipo de dato del resultado es {type(resta_numero_int_flot)}")

# Resta acumulativa (uso de -=)
acumulador = 5
acumulador -= 3  # Equivalente a: acumulador = acumulador - 3
print(f"Resta acumulativa: acumulador -= 3 → {acumulador}")

# Resta de valores negativos
"""
Restar un número negativo equivale a sumar su valor absoluto.
"""
print(f"Resta de negativos: {negativo_1} - {negativo_2} = {negativo_1 - negativo_2}")

# Resta de booleanos
print(f"Resta de booleanos: True - False = {True - False}")
print(f"Resta de booleanos: True - True = {True - True}")
print(f"Resta de booleanos: False - True = {False - True}")
print(f"Resta de booleanos: False - False = {False - False}")

# Resta en listas (diferencia acumulativa)
"""
Aunque no existe una función directa para restar todos los elementos de una lista,
podemos usar un enfoque iterativo.
"""
lista_numeros = [10, 2, 3, 4]
resta_total = lista_numeros[0]
for num in lista_numeros[1:]:
    resta_total -= num
print(f"Resta acumulativa de elementos en una lista: {lista_numeros} → {resta_total}")


# Operador Aritmético de Multiplicación:
"""
La multiplicación de números en Python se realiza usando el operador `*`.
"""
print(f"Multiplicación: 10 * 3 = {10 * 3}")

# Multiplicación con variables (int):
numero_1 = 7
numero_2 = 4
print(f"Multiplicación: numero_1 * numero_2 = {numero_1 * numero_2}")

# Multiplicación de un número entero y un número flotante:
numero_entero = 10
numero_flotante = 2.5
print(f"Multiplicación: numero_entero {numero_entero} * numero_flotante {numero_flotante} = {numero_entero * numero_flotante}")

# Multiplicación acumulativa (uso de *=):
acumulador = 5
acumulador *= 2  # Equivalente a: acumulador = acumulador * 2
print(f"Multiplicación acumulativa: acumulador *= 2 → {acumulador}")

# Operador Aritmético de División:
"""
La división devuelve siempre un número flotante, incluso si los operandos son enteros.
"""
print(f"División: 10 / 3 = {10 / 3}")

# División con variables:
numero_1 = 10
numero_2 = 4
print(f"División: numero_1 / numero_2 = {numero_1 / numero_2}")

# División acumulativa (uso de /=):
acumulador = 20
acumulador /= 5  # Equivalente a: acumulador = acumulador / 5
print(f"División acumulativa: acumulador /= 5 → {acumulador}")

# Operador Aritmético de División Entera:
"""
La división entera se realiza con `//` y descarta cualquier parte decimal del resultado.
"""
print(f"División entera: 10 // 3 = {10 // 3}")

# División entera con variables:
numero_1 = 17
numero_2 = 4
print(f"División entera: numero_1 // numero_2 = {numero_1 // numero_2}")

# División entera acumulativa (uso de //=):
acumulador = 50
acumulador //= 8  # Equivalente a: acumulador = acumulador // 8
print(f"División entera acumulativa: acumulador //= 8 → {acumulador}")

# Operador Aritmético de Módulo (residuo):
"""
El operador de módulo `%` devuelve el residuo de la división.
"""
print(f"Módulo: 10 % 3 = {10 % 3}")

# Módulo con variables:
numero_1 = 17
numero_2 = 5
print(f"Módulo: numero_1 % numero_2 = {numero_1 % numero_2}")

# Módulo acumulativo (uso de %=):
acumulador = 29
acumulador %= 6  # Equivalente a: acumulador = acumulador % 6
print(f"Módulo acumulativo: acumulador %= 6 → {acumulador}")

# Operador Aritmético de Potenciación:
"""
El operador `**` calcula la potencia de un número.
"""
print(f"Potencia: 2 ** 3 = {2 ** 3}")

# Potencia con variables:
base = 5
exponente = 3
print(f"Potencia: base ** exponente = {base ** exponente}")

# Potencia acumulativa (uso de **=):
acumulador = 2
acumulador **= 4  # Equivalente a: acumulador = acumulador ** 4
print(f"Potencia acumulativa: acumulador **= 4 → {acumulador}")

# Operador Aritmético Unario:
"""
El operador unario `-` se usa para cambiar el signo de un número.
"""
numero_positivo = 8
numero_negativo = -numero_positivo
print(f"Operador unario: -{numero_positivo} = {numero_negativo}")

# Operadores de Identidad:
"""
Los operadores de identidad no verifican el valor numérico o absoluto de una variable,
sino si dos variables apuntan a la misma posición en memoria (es decir, si son el mismo objeto).
"""

my_number = 1.0
my_new_number = 1.0
my_second_number = my_number

# Comparaciones con operadores de identidad:
print(f"my_number is my_new_number es {my_number is my_new_number}")  # False, no apuntan a la misma posición
print(f"my_number is my_second_number es {my_number is my_second_number}")  # True, apuntan a la misma posición

#Comparacion con operadores de identidad con NOT:
"""
El NOT va a invertir la verificacion.
"""
print(f"my_number is not my_new_number es {my_number is not my_new_number}")  # True, no apuntan a la misma posición
print(f"my_number is not my_second_number es {my_number is  not my_second_number}")  # False, apuntan a la misma posición


# Operadores de Igualdad:
"""
El operador de igualdad (==) se usa para verificar si dos o más números o variables tienen el mismo valor.
"""
print(f"Igualdad: 10 == 3 es {10 == 3}")  # False

variable_igualdad1 = 20
variable_igualdad2 = 30
variable_igualdad3 = 25
variable_igualdad4 = 25
variable_igualdad5 = variable_igualdad4

# Variables que son iguales:
print(f"Igualdad: variable_igualdad3 == variable_igualdad4 es {variable_igualdad3 == variable_igualdad4}")  # True
print(f"Igualdad: variable_igualdad3 == variable_igualdad4 == variable_igualdad5 es {variable_igualdad3 == variable_igualdad4 == variable_igualdad5}")  # True

# Variables que son diferentes:
print(f"Igualdad: variable_igualdad1 == variable_igualdad4 es {variable_igualdad1 == variable_igualdad4}")  # False
print(f"Igualdad: variable_igualdad1 == variable_igualdad2 == variable_igualdad3 es {variable_igualdad1 == variable_igualdad2 == variable_igualdad3}")  # False

# Operadores de Desigualdad
"""
El operador != se utiliza para verificar si dos o más números o variables son diferentes.
"""
print(f"Desigualdad: 10 != 3 es {10 != 3}")  # True
print(f"Desigualdad: variable_igualdad1 != variable_igualdad4 es {variable_igualdad1 != variable_igualdad4}")  # True
print(f"Desigualdad: variable_igualdad2 != variable_igualdad3 es {variable_igualdad2 != variable_igualdad3}")  # True

# Comparaciones encadenadas con desigualdad:
print(f"Desigualdad: variable_igualdad1 != variable_igualdad2 != variable_igualdad4 es {variable_igualdad1 != variable_igualdad2 != variable_igualdad4}")  # True
print(f"Desigualdad: variable_igualdad3 != variable_igualdad4 != variable_igualdad1 es {variable_igualdad3 != variable_igualdad4 != variable_igualdad1}")  # False

# Comparaciones Mayor y Menor:
"""
Los operadores > y < verifican si un número es mayor o menor que otro.
"""
print(f"Mayor que: 10 > 3 es {10 > 3}")  # True
print(f"Menor que: 10 < 3 es {10 < 3}")  # False

# Comparaciones Mayor o Igual y Menor o Igual:
"""
Los operadores >= y <= verifican si un número es mayor/igual o menor/igual que otro.
"""
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")  # True
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}")  # False

# Operadores Lógicos:
"""
El operador lógico AND verifica si todas las condiciones son True.
"""
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")  # True
print(f"AND: 10 + 3 == 13 and 5 - 1 == 3 es {10 + 3 == 13 and 5 - 1 == 3}")  # False

"""
El operador lógico OR verifica si al menos una condición es True.
"""
print(f"OR: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")  # True
print(f"OR: 10 + 3 == 13 or 5 - 1 == 3 es {10 + 3 == 13 or 5 - 1 == 3}")  # True
print(f"OR: 10 + 3 == 1 or 5 - 1 == 2 es {10 + 3 == 1 or 5 - 1 == 2}")  # False

# Operadores de pertenencia
print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'m' not in 'mouredev' = {'m' not in 'mouredev'}")
print(f"'b' in 'mouredev' = {'b' in 'mouredev'}")
print(f"'z' not in 'mouredev' = {'z' not in 'mouredev'}")

# Operadores Bit a Bit
"""
Los operadores bit a bit (o bitwise) trabajan directamente sobre los bits que componen un dato. Estos operadores son fundamentales en tareas de bajo nivel, como programación de sistemas, criptografía y optimización.
"""

# Operador AND (&)
"""
Compara cada bit de dos números y devuelve 1 si ambos bits son 1; de lo contrario, devuelve 0.
Se utiliza para enmascarar bits específicos.
"""
a = 5  # En binario: 0101
b = 3  # En binario: 0011
resultado_and = a & b  # Resultado: 0101 & 0011 = 0001 (Decimal: 1)
print(f"AND: {a} & {b} = {resultado_and}")

# Operador OR (|)
"""
Compara cada bit de dos números y devuelve 1 si al menos uno de los bits es 1; de lo contrario, devuelve 0.
Se utiliza para establecer bits específicos.
"""
resultado_or = a | b  # Resultado: 0101 | 0011 = 0111 (Decimal: 7)
print(f"OR: {a} | {b} = {resultado_or}")

# Operador XOR (^)
"""
Compara cada bit de dos números y devuelve 1 si los bits son diferentes; de lo contrario, devuelve 0.
Se utiliza para alternar bits específicos.
"""
resultado_xor = a ^ b  # Resultado: 0101 ^ 0011 = 0110 (Decimal: 6)
print(f"XOR: {a} ^ {b} = {resultado_xor}")

# Operador NOT (~)
"""
Invierte todos los bits de un número (complemento a uno).
Se utiliza para operaciones de inversión.
"""
resultado_not = ~a  # Resultado: ~0101 = 1010 (en complemento a dos: -6)
print(f"NOT: ~{a} = {resultado_not}")

# Operador de desplazamiento a la izquierda (<<)
"""
Desplaza los bits de un número hacia la izquierda un número especificado de posiciones. Cada desplazamiento equivale a multiplicar por 2.
Se utiliza para operaciones de multiplicación rápida.
"""
resultado_shift_left = a << 1  # Resultado: 0101 << 1 = 1010 (Decimal: 10)
print(f"Desplazamiento a la izquierda: {a} << 1 = {resultado_shift_left}")

# Operador de desplazamiento a la derecha (>>)
"""
Desplaza los bits de un número hacia la derecha un número especificado de posiciones. Cada desplazamiento equivale a dividir por 2 (sin decimales).
Se utiliza para operaciones de división rápida.
"""
resultado_shift_right = a >> 1  # Resultado: 0101 >> 1 = 0010 (Decimal: 2)
print(f"Desplazamiento a la derecha: {a} >> 1 = {resultado_shift_right}")

# Ejemplo combinado
"""
Combina varios operadores para manipular los bits de un número.
"""
numero = 12  # En binario: 1100
mascara = 6  # En binario: 0110
resultado_combinado = (numero & mascara) | (~mascara)
print(f"Ejemplo combinado: ({numero} & {mascara}) | (~{mascara}) = {resultado_combinado}")

# Estructuras de Control:


# Condicionales:
my_string_2 == "MoureDev"

if my_string2 == " MoureDev":
    print("my_string es 'MoureDev'")
else:
    print("my_string no es 'MoureDev'")



my_string_2 = "033A130"

if my_string_2 == "MoureDev":
    print("my_string_2 es 'MoureDev'")
elif my_string_2 == "033A130":
    print("my_string_2 es 'Brais'")
else:
    print("my_string_2 no es ninguna de las anteriores!")


# Iterativas:
for i in range(11):
    print(i)

i = 0 

while  i <= 10:
    print(i)
    i += 1

# Manejo de excepxiones
try:
    print(10 / 0)
except:
    print("Se ha producido un error!")
finally:
    print("Ha finalizado el manejo de exceptiones!")


# Dificultad Extra:

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
