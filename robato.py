import time 
map_width=80
map_height=20

def draw_robot(x,y):
	result = (" "*map_width)*y
	result += " " * x + "*"
	result += " " *map_width*(map_height-(y+1))
	return result

steps=20
for i in range(steps):
	time.sleep(.1)
	print(draw_robot(i,i+1))