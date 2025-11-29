"""
    Nombre: Hector Manuel Gamez Padrón
    Matrícula: 2530156
    Grupo: IM 1-3
"""

# ------------------------------
# Resumen Ejecutivo:
# ------------------------------
# En este documento se explica que un **bucle for** permite repetir acciones 
# recorriendo colecciones, rangos o secuencias con un número conocido de iteraciones. 
# Un **bucle while** repite instrucciones mientras una condición lógica sea verdadera, 
# siendo más natural cuando no se sabe cuántas veces se repetirá el proceso. 
# Un **contador** aumenta su valor para llevar registro de repeticiones, 
# mientras que un **acumulador** suma valores para obtener totales parciales o finales. 
# Es crucial definir bien la **condición de salida** para evitar ciclos infinitos 
# que bloqueen el programa o consuman recursos. 
# El documento cubrirá la descripción de cada problema, diseño de entradas y salidas, 
# validaciones necesarias y uso adecuado de for/while en recorridos, menús y lecturas repetidas.

# PRINCIPIOS Y BUENAS PRÁCTICAS
# ------------------------------
# - Utiliza un bucle **for** cuando conoces de antemano cuántas iteraciones habrá 
#   (por ejemplo, recorrer un rango del 1 al 10).
# - Utiliza un bucle **while** cuando el número de repeticiones depende de una 
#   condición que puede cambiar en tiempo de ejecución (por ejemplo, leer datos 
#   hasta que el usuario escriba "EXIT").
# - Inicializa correctamente **contadores** y **acumuladores** antes de entrar al bucle
#   para evitar errores lógicos y valores inesperados.
# - En bucles while, recuerda **actualizar la variable de control** dentro del bucle
#   para evitar ciclos infinitos.
# - Mantén el cuerpo del bucle **simple y legible**; si la lógica es compleja, muévela
#   a funciones separadas para mejorar claridad y mantenimiento del código.

#--------------------------------------------------
# Problem 1: Sum of range with for
#--------------------------------------------------
# Description:
# Calculate the sum of all integers from 1 to n (inclusive). 
# Additionally, calculate the sum of only the even numbers 
# within that same range using a for loop.

# Inputs:
# n_input = input("Enter n: ")
#
# Outputs:
# "Sum 1..n:", total_sum
# "Even sum 1..n:", even_sum
#
# Validations:
# n < 1:("Error: invalid input")
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...


n_input = input("Enter n: ").strip()

# Try converting to int
try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:
    # Validate that n >= 1
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for value in range(1, n + 1):
            total_sum += value
            if value % 2 == 0:
                even_sum += value

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

#--------------------------------------------------
# Problem 2: Multiplication table with for
#--------------------------------------------------
# Description:
# Generates and displays the multiplication table of a base number, 
# from 1 up to a limit m. For example, if base = 5 and m = 4, it displays:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
#
# Inputs:
# base = int
# m = int
#
# Outputs:
# resultado = base * i
#
# Validations:
# - Verificar que base y m se puedan convertir a int.
# - m >= 1 ("Error: invalid input")
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...


try:
    base = int(input("Enter base: ").strip())
    m = int(input("Enter limit: ").strip())

    # Validation that m is >= 1
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            resultado = base * i
            print(f"{base} x {i} = {resultado}")

except ValueError:
    # Capture only integer conversion errors
    print("Error: invalid input")


#--------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
#--------------------------------------------------
# Description:
# Read numbers one by one until the user enters a sentinel value (for example, -1). 
# Calculate the average of the valid numbers entered and the total number of numbers read. 
# If the user only enters the sentinel without any valid numbers, display an error message.
#
# Inputs:
# sentinel_value = -1
# number = float
#
# Outputs:
# except ValueError: "Error: invalid input"
# "Count:", count
# "Average:", average
# count == 0: "Error: no data"
#
# Validations:
# Each number must be converted into a float.
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...

sentinel_value = -1
total = 0
count = 0

while True:
    try:
        number = float(input("Enter number (-1 to finish): "))
    except ValueError:
        print("Error: invalid input")
        continue
    except KeyboardInterrupt:
            print("\nSalida manual")
            break

    if number == sentinel_value:
        break

    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)


#--------------------------------------------------
# Problem 4: Password attempts with while
#--------------------------------------------------
# Description:
# Implement a simple password attempt system. Define a valid password in the code (for example, "admin123"). 
# The user has a maximum of MAX_ATTEMPTS attempts to enter it. If they enter it correctly within the limit, display a success message. 
# If they run out of attempts, display a lock message.
#
# Inputs:
# user_password = input
#
# Outputs:
# "Login success"
# "Account locked"
#
# Validations:
# MAX_ATTEMPTS > 0
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

attempts = 0  

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")
    attempts += 1
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect password. You have {remaining} attempt(s) left.")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
else:
    # This else statement is executed if the while loop ends without a break statement.
    print("Account locked")

#--------------------------------------------------
# Problem 5: Simple menu with while
#--------------------------------------------------
# Description:
# Complement a text menu that repeats until the user selects the exit option. Example menu:
# 1) Show greeting
# 2) Show current counter value
# 3) Increment counter
# 0) Exit
# The program should execute the action corresponding to each option and redisplay 
# the menu until 0 is selected.
#
# Inputs:
# option_text = input
#
# Outputs:
# "Bye!"
# "Hello!"
# "Counter:", counter
# "Counter incremented"
# "Error: invalid option"
#
# Validations:
# option must be 0, 1, 2, or 3
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...

counter = 0

while True:
    print("\nMenu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_text = input("Choose an option: ")

    try:
        option = int(option_text)
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")

#--------------------------------------------------
# Problem 6: Pattern printing with nested loops
#--------------------------------------------------
# Description:
# Use nested for loops to print a pattern of asterisks in the shape of a right triangle. 
# For example, for n = 4:
# *
# **
# ***
# **** Additionally, print a second, reversed pattern 
# (optional if you wish to extend this, but please document your decision).
#
# Inputs:
# n_text = input
#
# Outputs:
# "*" * i
#
# Validations:
# 
# Verify that n >= 1
# "Error: invalid input" 
#
# Test cases:
# 1) Normal: ...
# 2) Border: ...
# 3) Error: ...

n_text = input("Enter n: ")

try:
    n = int(n_text)
except ValueError:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

# First triangle
for i in range(1, n + 1):
    print("*" * i)

# Optional inverted triangle (simple)
for i in range(n, 0, -1):
    print("*" * i)

#--------------------------------------------------
# 8. CONCLUSIONES (COMENTARIOS AL FINAL)
#--------------------------------------------------

#--------------------------------------------------
# 9. REFERENCIAS (MÍNIMO 5) – EN COMENTARIOS
#--------------------------------------------------