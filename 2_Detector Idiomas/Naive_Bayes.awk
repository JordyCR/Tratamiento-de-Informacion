#Calculo de Naive Bayes
awk '
FILENAME==modelo{
	#Se inicializa prob de acuerdo Modelo creado por el anterior codigo
	#Donde $2 es la Palabra $1 Clase $4 es porcentaje en decimales
	prob[$2,$1]=$4; # { (palabra, clase) : probabilidad }
	clases[$1]=1; # { idioma : dummyVal }
	vocabulario[$2]=1; # { palabra : dummyVal }
	next;
}

{
	#Variables donde se guardan los porcentajes finales
	I=0;
	F=0;
	T=0;

	for(x in clases){
		probPal[x]=0;
	
		for(i=1;i<=NF;i++){
			#Recorremos el Archivo sin clasificar y verificamos si existen palabras que se encuentre
			#Dentro de las clases
			if(($i,x) in prob ) {
				#probPal es la variable que va guardando el porcentaje de acuerdo a cada palabra
				#Se le aplica un suavizado para que los valores no sean tan grandes
			    aux = log(prob[$i,x] + 1);
			    # if(aux < 0) {
			    # 	aux=-aux;
			    # }
		        probPal[x]=probPal[x]+aux;
			}

			# if(probPal[x] < 0) {
			# 	probPal[x]=-probPal[x];
			# }
		}

		#Se van guardando los valores para que al final se determine cual es el mayor
		if(x=="French"){
			F=probPal[x];
		}
		if(x=="English"){
			I=probPal[x];
		}
		if(x=="Italian"){
			T=probPal[x];
		}
	} #Fin del For


	#Se manda a Imprimir el que tenga mayor Porcentaje junto con el Porcentaje y la Oracion
	if(F>I && F>T) {
		print "FRANCES: ",probPal[x]*100,$0;
	}
	if(T>F && T>I) {
		print "ITALIANO: ",probPal[x]*100,$0;
	}
	if(I>F && I>T) {
		print "INGLES: ",probPal[x]*100,$0;
	}

}' modelo=$1 $*
