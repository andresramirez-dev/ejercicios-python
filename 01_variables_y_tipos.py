# ================================================
# Ejercicio 1: Variables y Tipos de Datos
# Autor: Andrés Ramírez
# Descripción: Uso básico de variables y tipos
#              de datos en Python
# ================================================

# -- Tipos de datos básicos --
nombre = "Andrés"           # str   → texto
edad = 27                   # int   → número entero
altura = 1.75               # float → número decimal
activo = True               # bool  → verdadero o falso

# -- Mostrar información en pantalla --
print("=== Información Personal ===")
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Altura:", altura, "m")
print("Cuenta activa:", activo)

# -- Operaciones básicas con variables --
print("\n=== Operaciones ===")
anio_nacimiento = 2025 - edad
print("Año aproximado de nacimiento:", anio_nacimiento)

saludo = "Hola, me llamo " + nombre + " y tengo " + str(edad) + " años."
print(saludo)

# -- Verificar el tipo de una variable --
print("\n=== Tipos de datos ===")
print(type(nombre))    # <class 'str'>
print(type(edad))      # <class 'int'>
print(type(altura))    # <class 'float'>
print(type(activo))    # <class 'bool'>
