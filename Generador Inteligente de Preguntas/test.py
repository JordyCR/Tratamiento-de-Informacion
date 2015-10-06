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


# Borrar / Esto es Test
for arch in archivos_txt:
	print arch


from pattern.es import parse

print parse(open(archivos_txt[25]).readline()  )