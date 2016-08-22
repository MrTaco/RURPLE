def cargar_mapa(nombre_mapa):
	mapa = open(nombre_mapa, "r")
	resultado = []
	for i in mapa:
		resultado.append(list(i.strip()))
	mapa.close()
	return resultado

def cargar_instrucciones():
	inst = open(programa1.txt, "r")
	instrucciones = []
	for i in inst:
		instrucciones.append(list(i))
	programa1.close()
	return instrucciones