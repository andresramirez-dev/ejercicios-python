print("\t---Estudiemos las tablas de multiplicar---")
numero = int(input("\tIngrese un numero: "))
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

print("\t---Vamos a sumar 5 numeros---")
suma = 0
for i in range(1,6):
    numero = int(input(f"\t({i}) Ingrese un numero: "))
    suma = suma + numero
print(f"\n\tLa suma de todos los numeros es: {suma}")

for i in range(2, 51, 2):
     print(i)
     
