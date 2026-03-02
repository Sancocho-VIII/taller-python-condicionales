valid="invalid"
promedio = 0
nota = 0
while True:
        try:
                n1 = float(input("ingresa la nota de tus trabajos individuales "))
                n2 = float(input("ingresa la nota de tus trabajos grupales " ))
                n3 = float(input("ingresa la nota de tus examenes parciales " ))
                if 0<=n1<=100 and 0<=n2<=100 and 0<=n3<=100:
                    valid = 1
                    break
                else:
                    print("Error, ingresa un numero entre 0 y 100")
                    continue
        except ValueError:
                print("Error, ingresa un numero entre 0 y 100")
                continue
if valid == 1:
        promedio=(n1/3+n2/3+n3/3)
if 90<=promedio<=100:
        nota="Excelente"
elif 80<=promedio<90:
        nota = "Muy Bueno"
elif 70<=promedio<80:
        nota = "Bueno"
elif 60<=promedio<70:
        nota = "Supletorio"
else:
        nota="reprobado"
print(f"las notas  ingresadas son:{n1, n2, n3}.")
print(f"el promedio es de {promedio}.")
print(f"La nota final es de {nota}.")



