class Robot():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.monedas = 0
		self.direccion ="^"
		self.mapa = None

	def Move(self):
		if self.direccion=="^":
			self.y-=1
		elif self.direccion==">":
			self.x+=1
		elif self.direccion=="v":
			self.y+=1
		else:
			self.x-=1

	def dibujar(self):
		if self.direccion=="UP":
			return"^"
		elif self.direccion=="RIGHT":
			return">"
		elif self.direccion=="DOWN":
			return "v"
		else:
			self.direccion=="<"

	




