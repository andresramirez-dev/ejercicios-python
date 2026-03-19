print("\t---Apliquemos a los descuentos---")
descuentos = int(input("\tIngrese el precio del producto: "))
if descuentos > 200000:
    print("\tObtienes 20%  de descuento")
    precio = descuentos * 0.20
elif  descuentos >= 100000 and descuentos < 200000:
    print("\tObtienes 10% de descuento")
    precio = descuentos * 0.10
else:
    print("\tNo obtienes descuento")
    precio = 0
    
total_venta = descuentos - precio
print(f"\tEl total a pagar es: {total_venta} ")