
import string

idiomas = open('./Idiomas.txt', 'r')

	
lista_idiomas = ['Italian', 'French', 'English']
Italian = set()
French = set()
English = set()

for linea in idiomas:
	
	#Si es idioma Italiano
	if linea.split()[0] == lista_idiomas[0]:
		Italian = Italian | set(linea.split()[1:])
	#Si es idioma Frances	
	elif linea.split()[0] == lista_idiomas[1]:
		French = French | set(linea.split()[1:])
	#Entonces es Ingles
	else:
		English = English | set(linea.split()[1:])

#Calculamos la similitud entre Frances e Italiano
print "<<<<<<<Porcentaje de Similitud Frances | Italiano>>>>>>> "
similitud = len(Italian & French)/ float(len(Italian | French))
print similitud*100,"%"
#Calculamos la similitud entre Frances e Ingles
print "<<<<<<<Porcentaje de Similitud Frances | Ingles>>>>>>> "
similitud = len(English & French)/ float(len(English | French))
print similitud * 100, "%"
#Calculamos la similitud entre Ingles e Italiano
print "<<<<<<<Porcentaje de Similitud Ingles | Italiano>>>>>>> "
similitud = len(Italian & English)/ float(len(Italian | English))
print similitud *100, "%"



