def carga_mapa(mapeishon):
	f=open(Mapas/mapa1.txt, "r")
	mapa=list(f)
	return mapa
print(carga_mapa)