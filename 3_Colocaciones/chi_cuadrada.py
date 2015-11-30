# -*- coding: utf-8 -*-

frase = raw_input("Dame dos palabras para buscar\n>>> ")
#tomamos solo las dos primeras palabras
f = frase.split()[:2]
print f
#Abrimos el archivo
arch = open("./ingles.txt", "r")
#Leemos el archivo y lo convertimos en lista
t = arch.read().split()
# Tamaño del NGrama
tam_NGram = 2

# Creación simple de NGramas
grams = [t[i:i+tam_NGram] for i in xrange(len(t)-tam_NGram+1)]
#calculamos los valores observados
observados = [0]*4
for ngram in grams:
	# si la frase dada es igual al bigrama
	if (ngram == f):
		observados[0] += 1
	# si segunda palabra de la frase esta en la segunda posicion
	if (ngram[1] == f[1]):
		observados[1] += 1
	# si la primer palabara de la frase esta en la primera posicion
	if (ngram[0] == f[0]):
		observados[2] += 1
	# si la frase dada no es esta en el bigrama 
	if (ngram[0] != f[0] and ngram[1] != f[1]):
		observados[3] += 1

esperados = [0]*4

esperados[0]= ((observados[0] + observados[1])/ float(len(grams)) * (observados[0] + observados[2])/ float(len(grams))) * len(grams)
esperados[1]= ((observados[1] + observados[0])/ float(len(grams)) * (observados[1] + observados[3])/ float(len(grams))) * len(grams)
esperados[2]= ((observados[2] + observados[0])/ float(len(grams)) * (observados[2] + observados[3])/ float(len(grams))) * len(grams)
esperados[3]= ((observados[3] + observados[1])/ float(len(grams)) * (observados[3] + observados[2])/ float(len(grams))) * len(grams)
x = 0.0	
for i in xrange(0,4):
	print (observados[i] - esperados[i])**2
	print (observados[i] - esperados[i])**2/ float(esperados[i])
	x += (observados[i] - esperados[i])**2 / float(esperados[i])
print observados
print esperados
print x

