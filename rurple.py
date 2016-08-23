def cargar_mapa(nombre_mapa):
	listamapa = open(nombre_mapa, "r")
	mapa = []
	for i in listamapa:
		mapa.append(list(i.strip()))
	listamapa.close()
	return mapa

def cargar_instrucciones():
	listainstrucciones= open(programa1.txt, "r")
	instrucciones = []
	for j in listainstrucciones:
		instrucciones.append(j.strip())
	listainstrucciones.close()
	return instrucciones