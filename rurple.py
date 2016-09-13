from mapeishon import Mapa
from robot import Robot
from Ficha import Monedas
import time
import cargadores

nombre_mapa =  "mapas/" + (input("Ingrese Nombre del Mapa deseado: ")) + ".txt"
lista_mapa = cargadores.cargar_mapa(nombre_mapa)
nombre_instrucciones =  "instrucciones/" + (input("Ingrese Instrucciones del Mapa: ")) + ".txt"
lista_instrucciones = cargadores.cargar_instrucciones(nombre_instrucciones)


el_mapa = Mapa((len(lista_mapa[0])) , (len(lista_mapa))) 
#estos ciclos asignan el robot y las fichas al mapa usando las funciones
for j in range(len(lista_mapa)):
	for i in range(len(lista_mapa[0])):
		if lista_mapa[j][i] == "*":		
			el_robot = Robot(i ,j)
			el_robot.asignar_mapa(el_mapa)
			el_mapa.asignar_robot(el_robot)		
		elif int(lista_mapa[j][i]) > 0:	
			for l in range(int(lista_mapa[j][i])):
				la_moneda = Monedas(i , j)
				el_mapa.asignar_moneda(la_moneda)
print(el_mapa.dibujar())
for i in lista_instrucciones:
#este ciclo ejecuta las instrucciones de lista_instrucciones
	if i == "ROTATE":
		objeto_robot.ROTATE()
	elif i == "MOVE":
		objeto_robot.MOVE()
	else:
		objeto_robot.PICK()
#Imprime en pantalla las fichas dek mapa
	print("Fichas del Mapa: " , el_mapa.monedas_en_mapa())
	print("Fichas Recogidas: " , el_robot.monedas)
		

	
	print (el_mapa.dibujar())								
	time.sleep(0.5)
