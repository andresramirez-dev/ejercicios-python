print("--- \tDigitemos un numero ---")
numeros = int(input("\tDigite un numero: "))
if numeros < 0:
    print("\tEl numero es negativo")
elif numeros > 0:
    print("\tEl numero es positivo")
else:
    print("\tEl numero es 0")