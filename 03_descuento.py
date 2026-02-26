subtotal = float(input("Ingrese el subtotal de la cuenta"))
tipo_cliente = input("Eres vip o regular?")
descuento = 0
total = 0
dinero_descuento=0
if tipo_cliente == "vip" or tipo_cliente =="VIP":
	descuento = 0.15*subtotal	 
elif tipo_cliente == "regular" and subtotal >=100:
	descuento = 0.05*subtotal
else:
	descuento = 0

total = subtotal-descuento
print(f"El subtotal es de ${subtotal}.")
print(f"descuento aplicado de {descuento/10}%")
print(f"El total final es de ${total}")
