from mapeishon import Mapa
from robot import Robot
from Ficha import Monedas
import time
import cargadores

nombre_mapa =  "mapas/" + (input("Ingrese Nombre del Mapa deseado: ")) + ".txt"
lista_mapa = cargadores.cargar_mapa(nombre_mapa)
nombre_instrucciones =  "instrucciones/" + (input("Ingrese Instrucciones del Mapa: ")) + ".txt"
lista_instrucciones = cargadores.cargar_instrucciones(nombre_instrucciones)


objeto_mapa = Mapa((len(lista_mapa[0])) , (len(lista_mapa))) 

for j in range(len(lista_mapa)):
	for i in range(len(lista_mapa[0])):
		if lista_mapa[j][i] == "*":		
			objeto_robot = Robot(i ,j)
			objeto_robot.asignar_mapa(objeto_mapa)
			objeto_mapa.asignar_robot(objeto_robot)		
		elif int(lista_mapa[j][i]) > 0:	
			for lol in range(int(lista_mapa[j][i])):
				objeto_moneda = Monedas(i , j)
				objeto_mapa.asignar_moneda(objeto_moneda)
x=objeto_mapa.monedas_en_mapa()
print(objeto_mapa.dibujar())
for i in lista_instrucciones:
	if i == "ROTATE":
		objeto_robot.ROTATE()
	elif i == "MOVE":
		objeto_robot.MOVE()
	else:
		objeto_robot.PICK()

	print("Fichas del Mapa: " , objeto_mapa.monedas_en_mapa())
	print("Fichas Recogidas: " , objeto_robot.monedas)
		

	
	print (objeto_mapa.dibujar())								
	time.sleep(0.5)
