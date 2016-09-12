class Mapa(object):
    def __init__ (self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.monedas = []
        self.robot = None

    def asignar_robot(self, robot):
        self.robot = robot

    def asignar_moneda(self, monedas):  
        self.monedas.append(monedas)

    def dibujar(self):
        resultado = ""
        resultado += ("\n")
        for j in range(self.alto):
            for i in range(self.ancho):
                if self.contar_monedas(i , j) > 0:
                    resultado += str(self.contar_monedas(i, j)) 
                elif j == self.robot.y and i == self.robot.x:
                    resultado += self.robot.dibujar()
                else:
                    resultado += " "
            resultado +=  "\n"         
        return resultado            

    def contar_monedas(self, x, y):
        contar = 0
        for c in self.monedas:  
            if c.x == x and c.y == y: 
                contar += 1
        return contar   
    def restar_monedas(self , x , y):
        for i in range(len(self.monedas)):
            if self.monedas[i].x == x and self.monedas[i].y == y:
                self.monedas.pop(i)
                break 
    
    def monedas_en_mapa(self):
        contador = 0
        for moneda in self.monedas:
            contador += 1
        return contador 