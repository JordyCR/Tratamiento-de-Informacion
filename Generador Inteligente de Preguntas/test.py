# -*- coding: utf-8 -*-
import os
from os.path import isfile, join

RAIZ = './'
EXTENSION = ".txt"

archivos_txt = []
for base, dirs, files in os.walk(RAIZ): # Escaneamos el arbol de ficheros
	for file in files:
		fich = join(base, file)
		if fich.endswith(EXTENSION):
			archivos_txt.append(fich)


for arch in archivos_txt:
	print arch


from pattern.es import parse, ngrams
import codecs

print "\n\n"
mList = parse(codecs.open(archivos_txt[45], encoding='utf-8').readline().strip().split('.')[0]).split()
for element in mList[0]:
	print element[0] + "\t\t", # .encode('utf-8')
	for token in element[1:]:
		print str(token) + "\t",
	print

print "\n\n"
misGrams = ngrams(codecs.open(archivos_txt[45], encoding='utf-8').readline().strip().split('.')[0], n=5)
print str(misGrams)