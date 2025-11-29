"""
    Nombre: Hector Manuel Gamez Padrón
    Matrícula: 2530156
    Grupo: IM 1-3
"""

""" Resumen Ejecutivo:

Un string en Python es un tipo de dato que representa texto 
y es inmutable, lo que significa que cualquier modificación 
genera una nueva cadena. Entre las operaciones más comunes 
se encuentran concatenar, medir longitud, extraer subcadenas, 
buscar patrones y reemplazar texto. La validación y normalización 
de texto es esencial para garantizar entradas correctas, 
especialmente en información como correos, nombres o contraseñas. 
Este documento describe seis problemas aplicados al manejo de strings, 
detallando entradas, salidas, validaciones y casos de prueba.
También muestra el uso de los principales métodos de cadenas y 
su aplicación correcta en código.
"""

"""PRINCIPIOS Y BUENAS PRÁCTICAS:

Los strings son inmutables; cualquier cambio crea una nueva cadena.

Es buena práctica normalizar entradas con strip() y lower() antes de compararlas.

Evitar números mágicos en índices; documentar cada slicing.

Usar métodos de string en lugar de reescribir lógica básica.

Diseñar validaciones claras: primero vacío, luego formato.

Mantener código legible, con nombres claros y mensajes entendibles.

"""

# Problema 1: Full name formatter (name + initials)

"""Descripción:
Dado el nombre completo de una persona en una sola cadena (por ejemplo:
 "juan carlos tovar"), el programa debe:
1) Normalizar el texto (strip, espacios extra, mayúsculas/minúsculas).
2) Mostrar el nombre formateado en Title Case y las iniciales 
(por ejemplo: J.C.T.).
"""

"""
Entradas:
first_name, last_name

Salidas:
full_name, initials

Validaciones:


Testing:

"""

first_name = input("Set you firs name: ")
for i in range(5):
    if first_name.strip() == "":
        first_name = input("Invalid first name. Set your first name: ")
    else:
        break

last_name = input("Set you last name: ")
for i in range(5):
    if last_name.strip() == "":
        last_name = input("Invalid last name. Set your last name: ")
    else:
        break


full_name = first_name + " " + last_name
words = full_name.split()
initials = ""
for w in words:
    initials += w[0].upper() + "." 

print("Full Name:", full_name.strip().title())
print("Initials:", initials)    

# Problema 2: Email validator

"""Descripción:
Valida si una dirección de correo tiene un formato básico correcto:
- Contiene exactamente un '@'.
- Después del '@' debe haber al menos un '.'.
- No contiene espacios en blanco.
Si el correo es válido, también muestra el dominio 
(la parte después de '@').
"""

"""
Entradas:

Salidas:

Validaciones:

Testing:

"""

email_text = input("Set your email address: ")
for i in range(5):
email_text = email_text.strip()==""

