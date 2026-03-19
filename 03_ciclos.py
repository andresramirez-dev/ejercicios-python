# ================================================
# Ejercicio 3: Ciclos (for y while)
# Autor: Andrés Ramírez
# Descripción: Repetición de instrucciones usando
#              ciclos for y while
# ================================================

# -- Ejemplo 1: for con range --
print("=== Conteo del 1 al 5 ===")
for i in range(1, 6):
    print("Número:", i)

# -- Ejemplo 2: for recorriendo una lista --
print("\n=== Lenguajes de programación ===")
lenguajes = ["Python", "JavaScript", "HTML", "CSS"]

for lenguaje in lenguajes:
    print("-", lenguaje)

# -- Ejemplo 3: while con contador --
print("\n=== Cuenta regresiva ===")
contador = 5

while contador > 0:
    print(contador, "...")
    contador -= 1  # equivale a: contador = contador - 1
print("¡Despegue!")

# -- Ejemplo 4: ciclo con acumulador --
print("\n=== Suma de números del 1 al 10 ===")
suma = 0

for numero in range(1, 11):
    suma += numero  # equivale a: suma = suma + numero

print("La suma total es:", suma)

# -- Ejemplo 5: for con condicional dentro --
print("\n=== Solo números pares del 1 al 20 ===")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")  # end=" " evita salto de línea
print()  # salto de línea al final
