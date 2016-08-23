from rurple import cargar_mapa, cargar_instrucciones
print("Mapas Disponibles \n-mapa1 ")
nombre_mapa = "Mapas/" + (input("Ingrese el nombre del mapa: ")) + ".txt"
print(cargar_mapa(nombre_mapa))
nombre_instrucciones = "Instrucciones/" + (input("Ingrese el nombre de las instrucciones: ")) + ".txt"
print(cargar_instrucciones(nombre_instrucciones))