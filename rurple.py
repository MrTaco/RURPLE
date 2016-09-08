from mapeishon import Mapa
from robot import Robot
from monedas import Monedas
import time
from cargadores import cargar_mapa, cargar_instrucciones

nombre_mapa =  "mapas/" + (input("Ingrese Nombre del Mapa deseado: ")) + ".txt"
lista_mapa = cargadores.cargar_mapa(nombre_mapa)
nombre_instrucciones =  "instrucciones/" + (input("Ingrese Instrucciones del Mapa: ")) + ".txt"
lista_instrucciones = cargadores.cargar_instrucciones(nombre_instrucciones)


objeto_mapa = Mapa((len(lista_mapa[0])) , (len(lista_mapa))) 

for i in range(len(lista_mapa)):
	for j in range(len(lista_mapa[0])):
		if lista_mapa[i][j] == "*":		
			objeto_robot = Robot(j ,i)
			objeto_robot.asignar_mapa(objeto_mapa)
			objeto_mapa.asignar_robot(objeto_robot)		
		elif int(lista_mapa[i][j]) > 0:	
			for k in range(int(lista_mapa[i][j])):
				objeto_moneda = Monedas(j , i)
				objeto_mapa.asignar_moneda(objeto_moneda)

print("\n")
print("Fichas del Mapa: " + objeto_mapa.monedas_en_mapa())
print("Tus monedas: " + objeto_robot.monedas)
print(objeto_mapa.dibujar())
print("\n")

for i in lista_instrucciones:
	if i == "ROTATE":
		objeto_robot.ROTATE()
	elif i == "MOVE":
		objeto_robot.MOVE()
	else:
		objeto_robot.PICK()

	print("Monedas en el mapa: " , objeto_mapa.monedas_en_mapa())
	print("Tus monedas: " , objeto_robot.monedas)
	print("")		

	
	print (objeto_mapa.dibujar())								
	time.sleep(0.5)