# ------------------------------
# Nombre: Hector Manuel Gamez Padrón
# Matrícula: 2530156
# Grupo: IM 1-3
# ------------------------------


# ------------------------------
# Executive Summary:
# ------------------------------
# This document explains that a **for loop** allows you to repeat actions
# by traversing collections, ranges, or sequences with a known number of iterations.
# A **while loop** repeats instructions as long as a logical condition is true,
# being more natural when you don't know how many times the process will be repeated.
# A **counter** increments its value to keep track of repetitions,
# while an **accumulator** sums values ​​to obtain partial or final totals.
# It is crucial to define the **exit condition** well to avoid infinite loops
# that block the program or consume resources.
# The document will cover the description of each problem, input and output design,
# necessary validations, and proper use of for/while loops in traversals, menus, and repeated reads.


# ------------------------------
# PRINCIPLES AND BEST PRACTICES
# ------------------------------
# - Use a **for** loop when you know in advance how many iterations there will be
# (for example, iterating through a range from 1 to 10).
# - Use a **while** loop when the number of repetitions depends on a
# condition that can change at runtime (for example, reading data
# until the user types "EXIT").
# - Properly initialize **counters** and **accumulators** before entering the loop
# to avoid logical errors and unexpected values.
# - In while loops, remember to **update the control variable** inside the loop
# to avoid infinite loops.
# - Keep the loop body **simple and readable**; if the logic is complex, move it
# to separate functions to improve code clarity and maintainability.


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
# 1) Normal: 
# Enter n: 15
# Sum 1..n: 120
# Even sum 1..n: 56
#
# 2) Border: 
# Enter n: 1
# Sum 1..n: 1
# Even sum 1..n: 0
# 
# 3) Error: 
# Enter n: -5
# Error: invalid input


n_input = input("Enter n: ").strip()


try:
    n = int(n_input)
except ValueError:
    print("Error: invalid input")
else:

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
# 1) Normal:
# Even sum 1..n: 56
# Enter base: 6
# Enter limit: 7
#6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
#
# 2) Border: 
# Enter base: 5
# Enter limit: 1
# 5 x 1 = 5
# 
# 3) Error: 
# Enter base: 7
# Enter limit: 0
# Error: invalid input


try:
    base = int(input("Enter base: ").strip())
    m = int(input("Enter limit: ").strip())
   
    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            resultado = base * i
            print(f"{base} x {i} = {resultado}")

except ValueError:
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
# 1) Normal: 
# Enter number (-1 to finish): 6
# Enter number (-1 to finish): 5
# Enter number (-1 to finish): 4
# Enter number (-1 to finish): 3
# Enter number (-1 to finish): 2
# Enter number (-1 to finish): -1
# Count: 5
# Average: 4.0
#
# 2) Border: 
# Enter number (-1 to finish): 8
# Enter number (-1 to finish): -1
# Count: 1
# Average: 8.0
#
# 3) Error: 
# Enter number (-1 to finish): -1
# Error: no data

sentinel_value = -1
total = 0
count = 0

while True:
    try:
        number = float(input("Enter number (-1 to finish): "))
    except ValueError:
        print("Error: invalid input")


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
# 1) Normal:
# Enter password: admin123
# Login success
# 
# 2) Border: 
# Incorrect password. You have 1 attempt(s) left.
# Enter password: admin123
# Login success
# 
# 3) Error: 
# Account locked

CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

attempts = 0  

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")
    attempts += 1
    
    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    remaining = MAX_ATTEMPTS - attempts
    if remaining > 0:
        print(f"Incorrect password. You have {remaining} attempt(s) left.")
else:
    
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
# 1) Normal: 
#    Input: 1 → 2 → 3 → 0
#    Output: Hello!, Counter:0, Counter incremented, Bye!
#
# 2) Border: 
# Choose an option: 0
# Bye!
#
# 3) Error: 
# Choose an option: 5
# Error: invalid option

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
# 1) Normal: 
# Enter n: 4
# *
# **
# ***
# ****
# ****
# ***
# **
# *
#
# 2) Border: 
# Enter n: 1
# *
# *
#
# 3) Error: 
# Enter n: 0
# Error: invalid input

n_text = input("Enter n: ")

try:
    n = int(n_text)
except ValueError:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()


for i in range(1, n + 1):
    print("*" * i)


for i in range(n, 0, -1):
    print("*" * i)

#--------------------------------------------------
#  CONCLUSIONS 
#--------------------------------------------------
# # The for loop is useful when we know how many times to repeat,
# while the while loop is used to repeat based on a condition.
# Counters and accumulators allow us to keep track of sums,
# attempts, or values ​​within loops.
# A risk of the while loop is falling into infinite loops if the condition is not updated correctly.
# Menus and password systems are typical examples where the while loop works very well.
# Nested loops allow us to create patterns like triangles of asterisks
# and better understand repetition within another repetition.

#--------------------------------------------------
#  REFERENCES
#--------------------------------------------------
# https://docs.python.org/3/tutorial/controlflow.html
# https://www.youtube.com/watch?v=-EZREF7Hp6s
# https://www.youtube.com/watch?v=x-qbx7vXuxA
# https://www.youtube.com/watch?v=w53HiWSZnzU
# https://www.youtube.com/watch?v=YEWxlbffgxE
# https://libros.metabiblioteca.org/server/api/core/bitstreams/a567dd25-1e96-4c0f-9b6a-7a844d0eb577/content


# URL Repositorio en github
# https://github.com/Hectorpadro/Tareas_programacion_unidad_2.git