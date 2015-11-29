# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time, random
import re

frase = raw_input("Dame una frase para analizar con google mediante NGramas\n>>> ")
t = frase.split()

# Tamaño del NGrama
tam_NGram = 2

# Creación simple de NGramas
grams = [t[i:i+tam_NGram] for i in xrange(len(t)-tam_NGram+1)]

def pag_to_soup(url):
	request = urllib2.Request(url, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	page = urllib2.urlopen(request)
	return BeautifulSoup(page.read(), "html5lib")

def result_stats_from_url(url):
	soup = pag_to_soup(url)

	resultStats = soup.find(id="resultStats").getText()
	resultStats = re.sub(r'\([^)]*\)', '', resultStats) # Quitamos el '(0.39 segundos)'
	resultStats = resultStats.replace('Cerca de ', '').replace('resultados', '') # Limpiamos
	return resultStats.replace(',', '')


for i in xrange(len(grams)):

	url = "https://www.google.com.mx/search?q=\"%s\"" % ( '+'.join(grams[i]) )
	nn = result_stats_from_url(url)

	wait = random.uniform(1, 2)
	time.sleep(wait)


	url = "https://www.google.com.mx/search?q=%s&ie=utf-8&oe=utf-8" % ( t[i] )
	mm = result_stats_from_url(url)

	print "Probabilidad de que '" + t[i+1] + "' aparezca despues de '" + t[i] + "' =", (float(nn)/float(mm))
	wait = random.uniform(2, 4)
	time.sleep(wait)