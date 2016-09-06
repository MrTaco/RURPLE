class Mapa(object):
	def __init__(self, ancho, alto):
		self.ancho=ancho
		self.alto=alto
		self.monedas=[]
		self.robot= None
	def asignar_robot(self, robot):
		self.robot = robot

	def agregar_moneda(self, moneda):
		self.monedas.append(moneda)

	def contar(self, x, y):
    contador = 0
    for moneda in self.monedas:
        if moneda.x == x and moneda.y == y:
           contador += 1


        return contador

	def dibujar_mapa(self):
        resultado = ""

        for y in range(self.altura):
            for x in range(self.ancho):
                if x == self.robot.x and y == self.robot.y:
                    resultado += self.robot.dibujar()

                elif self.contar_monedas_en(x, y) > 0:
                    resultado += self.contar_monedas_en(x, y)
                else:
                    resultado += " "

            resultado += "\n"

        return resultado

        