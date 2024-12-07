# Operadores

# 📌 OPERADORES ARITMETICOS

print("\n======== OPERADORES ARITMETICOS ========")
print(f"Suma: 2+2 = {2+2}")
print(f"Resta: 4-2 = {4-2}")
print(f"Multiplicacion: 2*2 = {2*2}")
print(f"Division 10/3:  = {10/3}")
print(f"Division Entera 10//3:  = {10//3}")
print(f"Resto : 2%2 = {2%2}")
print(f"Exponente : 2**2 = {2**2}")

# 📌 OPERADORES DE COMPARACIÓN

print("\n======== OPERADORES DE COMPARACIÓN ========")
print(f"Igualdad: 10 == 3 {10 == 3}")
print(f"Desigualdad: 10 != 3 {10 != 3}")
print(f"Mayor que: 10 > 3 {10 > 3}")
print(f"Menor que: 10 < 3 {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 {10 >= 3}")
print(f"Menor o igual que: 10 <= 3 {10 <= 3}")

# 📌 OPERADORES LOGICOS

print("\n======== OPERADORES LOGICOS ========")
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 es: {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR: 10 + 4 == 13 or 5 - 1 == 4 es: {10 + 4 == 13 or 5 - 1 == 4}")
print(f"NOT: not 10 + 3 == 14 es: {not 10 + 3 == 14}")

# 📌 OPERADORES DE ASIGNACION

print("\n======== OPERADORES DE ASIGNACIÓN ========")
my_number = 11 #asignacion
print(my_number)
my_number += 1 #suma y asignacion
print(my_number)
my_number -= 1 #resta y asignacion
print(my_number)
my_number *= 1 #multiplicacion y asignacion
print(my_number)
my_number /= 1 #division y asignacion
print(my_number)
my_number %= 2 #modulo y asignacion
print(my_number)
my_number **= 2 #exponente y asignacion
print(my_number)
my_number //= 2 #division entera y asignacion
print(my_number)

# 📌 OPERADORES DE IDENTIDAD

print("\n======== OPERADORES DE IDENTIDAD ========")
my_new_number = my_number
print(f"OPERADOR DE IDENTIDAD (is) my_number is my_new_number es {my_number is my_new_number}")
my_new_number = 1.0
print(f"OPERADOR DE IDENTIDAD (is) my_number is my_new_number es {my_number is my_new_number}")
print(f"OPERADOR DE NO IDENTIDAD (is not) my_number is my_new_number es {my_number is not my_new_number}")

# 📌 OPERADORES DE PERTENENCIA

print("\n======== OPERADORES DE PERTENENCIA ========")
print(f"OPERADOR (in) 'i' in 'Danilo => {'i' in 'Danilo'}'")
print(f"OPERADOR (not in) 'i' not in 'Danilo => {'i' not in 'Danilo'}'")

# 📌 OPERADORES DE BIT

print("\n======== OPERADORES DE BIT ========")
a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000