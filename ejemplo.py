class Robot(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.monedas=0
		self.direccion="UP"
		self.mapa=None

	def MOVE(self):
		pass
	def ROTATE(self):
		pass
	def PICK(self):
		pass
	def obtener_representacion(self):
		if self.direccion=="UP":
			


class Moneda(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.mapa=None