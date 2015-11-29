# -*- coding: utf-8 -*-
# letras = 'a\tas30d\nsá20'.decode('utf-8')
# letras = u'a\tas30d\nsá20'




def main():
	letras_ing = open('ingles.txt', 'r').read().lower().decode('utf-8')
	solo_chars_ing = filter(lambda x: x.isalpha(), letras_ing)

	letras_esp = open('espanol.txt', 'r').read().lower().decode('utf-8')
	solo_chars_esp = filter(lambda x: x.isalpha(), letras_esp)

	prob_letra(solo_chars_ing, 'Ingles')
	prob_letra(solo_chars_esp, 'Español')




def prob_letra(solo_chars, idioma):
	print ">>>>>" , idioma , "<<<<<"
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




if __name__ == '__main__':
	main()



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