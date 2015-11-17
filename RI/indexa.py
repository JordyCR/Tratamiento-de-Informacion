# -*- coding: utf-8 -*-
import os
from os.path import isfile, join
from pattern.es import lemma
import string

RAIZ = './'
EXTENSION = ".txt"

archivos_txt = []
for base, dirs, files in os.walk(RAIZ): # Escaneamos el arbol de ficheros
	for file in files:
		fich = join(base, file)
		if fich.endswith(EXTENSION):
			archivos_txt.append(fich)


# {palabra : documento}
diccionario = {}


for arch in archivos_txt:
	# print arch

	t = open(arch).read().lower()
	# TODO: Falta leer el archivo con formato utf-8

	# TODO: Falta quitar todos los signos de puntuación con una RegEx
	t = t.translate(string.maketrans("",""), string.punctuation)

	# Sacar el Lemma de cada palabra
	pals = t.split()

	# No sirve
	# i = 0
	# for x in xrange(len(pals)):
	# 	pals[i] = lemma(str(pals[i]).decode('utf-8'))
	# 	i += 1

	for p in pals:
		if not p in diccionario:
			diccionario[p] = set()
		diccionario[p].add(arch)

# Solo mostramos el diccionario
for k in diccionario.keys()[10:30]:
	print "PALABRA:", k, "\t"
	for e in diccionario[k]:
		print e, ",",
	print "\n"


while True:
	op = raw_input("\nIntroduce tu busqueda:\n>>> ")
	op = op.translate(string.maketrans("",""), string.punctuation)

	busq = op.split()

	# Un solo elemento
	if len(busq) == 1:
		op = lemma(op.decode('utf-8'))

		if op in diccionario:
			for res in diccionario[op]:
				print res
			print
			print ">>> Resultados:" , len(diccionario[op]), "<<<\n"
		else:
			print ">>> No hubo resultados para esta búsqueda <<<\n"

	# Mas de un elemento
	elif len(busq) > 1:
		tipo = raw_input("\nQue tipo de busqueda desea realizar:\n" + 
						"A) AND\n" + 
						"B) OR\n" + 
						"C) RESTA\n" + 
						">>> ").lower()

		conjb = []
		for i in xrange(len(busq)):
			r = set() if busq[i] not in diccionario else diccionario[busq[i]]
			conjb.append(r)

		resultado = conjb[0]

		for i in range(1, len(busq)):
			if tipo == 'a':
				resultado = resultado & conjb[i]
			elif tipo == 'b':
				resultado = resultado | conjb[i]
			elif tipo == 'c':
				resultado = resultado - conjb[i]


		# Mostramos los resultados
		for res in resultado:
			print res
		print
		print ">>> Resultados:" , len(resultado), "<<<\n"
