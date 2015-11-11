# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time, random
import re # Expresiones Regulares

# Tamaño del NGrama
tam_NGram = 5


# Leemos el archivo a analizar
t = open('ingles.txt').read().decode('utf-8')
t = re.sub(r'\([^)]*\)', '', t)
t = t.split()


# Formamos el arreglo de palabras que usaremos en la consulta (NGramas)
# (Creación dimple de NGramas)
grams = [t[i:i+tam_NGram] for i in xrange(len(t)-tam_NGram+1)]


# Ciclo para hacer la consulta de google
for i in xrange(len(grams)):

	# Query
	q = '+'.join(grams[i])

	# Deberiamos hacer que reaccione según el idioma, quitando el '.mx'
	url = "https://www.google.com.mx/search?q=%s&ie=utf-8&oe=utf-8" % ( q )
	# "https://www.google.com.mx/search?q=tigre+negro&ie=utf-8&oe=utf-8"

	# Google te limita a 2500 Querys por día
	# Mas info
	# http://stackoverflow.com/questions/22657548/is-it-ok-to-scrape-data-from-google-results
	# page=urllib2.urlopen(url)


	# Simulamos un navegador
	request = urllib2.Request(url, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
    
	# Efectuamos el Query
	page = urllib2.urlopen(request)

	# Parseamos todo el HTML
	soup = BeautifulSoup(page.read(), "html5lib")


	# Conseguimos los números
	resultStats = soup.find(id="resultStats").getText()
	resultStats = re.sub(r'\([^)]*\)', '', resultStats) # Quitamos el '(0.39 segundos)'
	resultStats = resultStats.replace('Cerca de ', '').replace('resultados', '') # Limpiamos

  
  	# Mostramos
  	g = ' '.join(grams[i]).encode('utf-8').encode('utf-8')
	# print "Iteración: %s\nGramaQuery: %s\nResultados: %s" % ( i, g, resultStats)
	print "Iteración:", i+1
	print "GramaQuery:", g
	print "Resultados:", resultStats

	# Esperamos aleatoriamente para pasar desapercibidos de san google
	wait = random.uniform(2, 5)
	print "Espramos tantito: %s segs\n" % wait
	time.sleep(wait)