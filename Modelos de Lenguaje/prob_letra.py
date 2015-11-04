# -*- coding: utf-8 -*-

# letras = 'a\tas30d\nsá20'.decode('utf-8')
# letras = u'a\tas30d\nsá20'

letras = open('ingles.txt', 'r').read().lower().decode('utf-8')

# def acentos2letras(letra):
# 	if letra == u'á':
# 		return u'a'
# 	elif letra == u'é':
# 		return u'e'
# 	elif letra == u'í':
# 		return u'i'
# 	elif letra == u'ó':
# 		return u'o'
# 	elif letra == u'ú':
# 		return u'u'
# 	else:
# 		return letra

# letras = filter(lambda x: acentos2letras(x), letras)
solo_chars = filter(lambda x: x.isalpha(), letras)

# print solo_chars
cont = {}
for l in solo_chars:
	if not l in cont:
		cont[l] = 1
	else:
		cont[l] += 1

# Mostrar resultados
t = len(solo_chars)
for l in cont.keys():
	porc = float(cont[l]) / t * 100
	print '%s %s %5s %s %s %s ' % (l, '->', cont[l], '\t', str(porc)[:9], '%')

# print '\n', t
