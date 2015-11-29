import math
g1 = open("g1.txt", 'r')
g2 = open("g2.txt", 'r')
g3 = open("g3.txt", 'r')

#Leemos todos los archivos y los guardamos en conjuntos
animal = set(g1.read().split())
hidraulico = set(g2.read().split())
juego = set (g3.read().split())

#leemos oracion y la volvemos un conjunto 
oracion = set(raw_input(">>> Proporcione una oracion que tenga que ver con gato (animal/hidraulico/juego)\n>>> ").split())

r1 = len(animal & oracion) / float(len (animal | oracion))
r2 = len(hidraulico & oracion)/ float(len(hidraulico | oracion))
r3 = len(juego & oracion) / float(len(juego | oracion))

print r1
print r2
print r3

if ( r1 > r2):
	if (r1 > r3):
		print "la oracion posee un sentido semantico de animal"
	else:
		print "la oracion posee un sentido semantico de juego"
elif (r2 > r3):
	print "la oracion posee un sentido semantico de herramienta"
else:
	print "la oracion posee un sentido semantico de juego"

