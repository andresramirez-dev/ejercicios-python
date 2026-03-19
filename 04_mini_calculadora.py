# ================================================
# Ejercicio 4: Mini Calculadora
# Autor: Andrés Ramírez
# Descripción: Programa que combina variables,
#              condicionales y ciclos para hacer
#              operaciones matemáticas básicas
# ================================================

def calculadora():
    print("╔══════════════════════════╗")
    print("║      MINI CALCULADORA    ║")
    print("╚══════════════════════════╝")

    # -- Solicitar números al usuario --
    num1 = float(input("\nIngresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    # -- Mostrar opciones de operación --
    print("\n¿Qué operación deseas realizar?")
    print("  1. Suma")
    print("  2. Resta")
    print("  3. Multiplicación")
    print("  4. División")

    opcion = input("\nElige una opción (1-4): ")

    # -- Ejecutar la operación según la opción --
    if opcion == "1":
        resultado = num1 + num2
        simbolo = "+"
    elif opcion == "2":
        resultado = num1 - num2
        simbolo = "-"
    elif opcion == "3":
        resultado = num1 * num2
        simbolo = "×"
    elif opcion == "4":
        # Validar que no se divida entre cero
        if num2 == 0:
            print("\nError: no se puede dividir entre cero.")
            return
        resultado = num1 / num2
        simbolo = "÷"
    else:
        print("\nOpción no válida.")
        return

    # -- Mostrar resultado --
    print(f"\n{num1} {simbolo} {num2} = {resultado}")

# -- Ejecutar la calculadora --
calculadora()
