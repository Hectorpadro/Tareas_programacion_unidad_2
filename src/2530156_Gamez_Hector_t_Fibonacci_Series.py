# ------------------------------
# Nombre: Hector Manuel Gamez Padrón
# Matrícula: 2530156
# Grupo: IM 1-3
# ------------------------------

# EXECUTIVE SUMMARY
# The Fibonacci series is a sequence where each term is obtained by adding 
# the previous two numbers, starting from 0 and 1. This program reads an 
# integer n from the user and generates the first n Fibonacci terms. It 
# includes input validation to ensure n is a valid integer and n >= 1. A 
# loop is used to iteratively compute the sequence. The objective is to 
# practice loops, validation, and formatted output in Python


# PROBLEM: FIBONACCI SERIES GENERATOR
# Description:
# Program that reads an integer n and prints the first n terms of the 
# Fibonacci series, starting from 0 and 1.

# Inputs:
# user_input = input("Enter number of terms: ")

# Outputs:
# fibo_text

# Validations:
# - n debe ser un entero (se valida con isdigit())
# - n debe ser >= 1
# - n debe ser <= 50


# Test cases:

# 1. Normal case:
#   n = 7  
#    Expected output: "Fibonacci series: 0 1 1 2 3 5 8"

# 2. Border case:
#    n = 1  
#    Expected output: "Fibonacci series: 0"

# 3. Error case:
#    Enter number of terms: 0
# Error: invalid input (must be between 1 and 50).



user_input = input("Enter number of terms: ").strip()

if not user_input.isdigit():
    print("Error: invalid input (not an integer).")
    exit()

n = int(user_input)

if n < 1 or n > 50:
    print("Error: invalid input (must be between 1 and 50).")
    exit()
elif n == 1:
    print("Fibonacci series: 0")
    exit()
elif n == 2:
    print("Fibonacci series: 0 1")
    exit()

fibo = [0, 1] 

for i in range(2, n):
    next_term = fibo[i-1] + fibo[i-2]
    fibo.append(next_term)

fibo_text = " ".join(str(x) for x in fibo)

print("Fibonacci series:", fibo_text)



# CONCLUSIONS
# Using a loop made it possible to build the Fibonacci sequence step by step 
# without needing complex formulas. Handling special cases such as n = 1 or 
# n = 2 ensures the program behaves correctly for all valid inputs. The logic 
# for generating Fibonacci numbers can be reused in other programs that 
# require iterative sequences or cumulative calculations.


# REFERENCES
# Python Official Documentation – Built-in Types (List, Tuple, Dict)
# https://docs.python.org/3/library/stdtypes.html

# Python Official Tutorial – Input & Output
# https://docs.python.org/3/tutorial/inputoutput.html

# W3Schools – Python Lists
# https://www.w3schools.com/python/python_lists.asp

# Real Python – Handling Errors With Exceptions
# https://realpython.com/python-exceptions/

# GeeksforGeeks – Python Program to Check Valid Strings / isalpha()
# https://www.geeksforgeeks.org/python-string-isalpha-application/


# URL Repositorio en github
# https://github.com/Hectorpadro/Tareas_programacion_unidad_2.git