from rurple import cargar_mapa, cargar_instrucciones
print("Mapas Disponibles \n-mapa1 ")
nombre_mapa = "Mapas/" + (input("Ingrese el nombre del mapa: ")) + ".txt"
print(cargar_mapa(nombre_mapa))
nombre_instrucciones = "Instrucciones/" + (input("Ingrese el nombre de las instrucciones: ")) + ".txt"
print(cargar_instrucciones(nombre_instrucciones))

class Mapa(object):
	def __init__(self, ancho, alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
	
	def asignar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, moneda):
		self.monedas.append(moneda)
lista_mapa=[....]
mapa==Mapa(len(lista_mapa[0],lista_mapa))
for y in range(len(lista_mapa)):
	for x in range(len(lista_mapa)):
		if lista_mapa[y][x]=="*":
			robot=Robot[x][y]
		elif lista_mapa[y][x] == "0":
			pass
		else:
			cantidad=int(lista_mapa[y][x])
			for i in range(cantidad):
				moneda=Moneda(x,y)
				mapa_agregar=moneda(moneda)