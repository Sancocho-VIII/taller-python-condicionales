tarifa = 1
distancia = float(input("De cuantos km fue el recorrido? "))
hora = int(input("A que hora empezo el recorrido? entero entre (0 y 23) "))
km=0
if 9<=hora<=19:
	km = 0.5
	horario = "diurno"
elif 0<=hora<=5 or 20<=hora<=23:
	km = 0.65
	horario = "nocturno"
if distancia >10:
	tarifa +=2

costo_total=(distancia*km)+tarifa
print(f"el horario del viaje fue en horario {horario}.")
print(f"la distancia recorrida fue de {distancia}km.")
print(f"el costo total a pagar es de ${costo_total}.")
