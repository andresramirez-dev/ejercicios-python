# ================================================
# Ejercicio 2: Condicionales (if / elif / else)
# Autor: Andrés Ramírez
# Descripción: Toma de decisiones según el valor
#              de una variable
# ================================================

# -- Ejemplo 1: Clasificar edad --
print("=== Clasificador de edad ===")
edad = 20

if edad < 12:
    print("Es un niño")
elif edad < 18:
    print("Es un adolescente")
elif edad < 60:
    print("Es un adulto")
else:
    print("Es un adulto mayor")

# -- Ejemplo 2: Verificar si un número es par o impar --
print("\n=== Par o Impar ===")
numero = 15

if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")

# -- Ejemplo 3: Sistema de calificaciones --
print("\n=== Sistema de Calificaciones ===")
nota = 85

if nota >= 90:
    print("Calificación: Excelente")
elif nota >= 75:
    print("Calificación: Bueno")
elif nota >= 60:
    print("Calificación: Aprobado")
else:
    print("Calificación: Reprobado")

# -- Ejemplo 4: Condiciones combinadas (and / or) --
print("\n=== Acceso al sistema ===")
usuario = "andres"
contrasena = "1234"

if usuario == "andres" and contrasena == "1234":
    print("Acceso concedido")
else:
    print("Usuario o contraseña incorrectos")
