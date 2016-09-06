class Robot():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.monedas = 0
		self.direccion ="^"
		self.mapa = None

	def Move(self):
		if self.direccion=="UP":
			self.y-=1
		elif self.direccion=="RIGHT":
			self.x+=1
		elif self.direccion=="DOWN":
			self.y+=1
		else:
			self.x-=1
        if self.x < 0:
            self.x = 0

        if self.x >= self.mapa.ancho:
            self.x = self.mapa.ancho - 1

        if self.y < 0:
            self.y = 0

        if self.y >= self.mapa.alto:
            self.y = self.mapa.alto - 1

	def dibujar(self):
		if self.direccion=="UP":
			return"^"
		elif self.direccion=="RIGHT":
			return">"
		elif self.direccion=="DOWN":
			return "v"
		else:
			return "<"

	def asignar_mapa(self):
		self.mapa=mapa
	




