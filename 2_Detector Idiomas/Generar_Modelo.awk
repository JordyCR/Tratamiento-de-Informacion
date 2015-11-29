#Calculamos la Probabilidad de existencia de una palabra dentro del Corpus de Palabras

awk '{
	#Para cada clase dentro del archivo creamos un vocbulario
	#En este caso las clases que se tienen son 3: Ingles, Italiano,Frances
	for(i=2;i<=NF;i++) {
		frec[$1,$i]++; # { (idioma, palabra) : contpal }
		total_pals[$1]++; # Por idioma
		vocabulario[$i]=1; # Conjunto de todas las palabras encontradas
	}
	#Se Guarda la clase
	clases[$1]=1;
}
END{
	#Recorremos cada clase para calcular su frecuencia de una clase dentro de otra
	for(y in clases) {
		for(x in vocabulario) {
			if((y,x)in frec)
				#Se manda a imprimir la Frecuencia de una clase con respecto de la otra
				print y,x, frec[y,x] "/" total_pals[y], frec[y,x]/total_pals[y];
			else
				#Si la palabra no se encuentra se manda a imprimir un 1 indicando esto 
				#Se le asigna un 1 para que asi no afecte en operaciones a Naive Bayes
				# print y,x,"1/"total_pals[y],"1";
				print y,x,"1/"total_pals[y], 1/total_pals[y];
		}
    }

}' $*
