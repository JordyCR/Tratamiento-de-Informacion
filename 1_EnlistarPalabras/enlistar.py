# -*- coding: utf-8 -*-
import string
import math


T = open('ingles.txt').read().lower().translate(string.maketrans(" "," "), string.punctuation)
TN = T.split()
N = len(TN)


# Debemos calcular la frecuencia de cada palabra
palabras_hash = {}
palabras_arr = []


# TablaHash
for p in TN:
	if p not in palabras_hash:
		palabras_hash[p] = 1


# Arreglo
for p in TN:
	if p not in palabras_arr:
		palabras_arr.append(p)

# Mostrar
# for p in palabras_arr:
# 	print p


print "Hast len(", len(palabras_hash), ")"
print "Array len(", len(palabras_arr), ")"