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

	def Rotate(self):
		if self.direccion=="^":
			self.direccion=">"
		elif self.direccion==">":
			self.direccion=="v"
		elif self.direccion=="v":
			self.direccion=="<"
		else:
			self.direccion=="^"

	




