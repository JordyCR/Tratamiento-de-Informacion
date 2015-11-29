awk '{
  gsub(/[!$%&=?¡¿´¨""*{},_;:()+[\]\x2E-]/, " ", $0);
  #print NF;
  for (i=2; i<=NF; i++){
  	frecuencia[tolower($1),tolower($i)]++;
  	#print tolower($1),tolower($i);
  }
  #Total[tolower($1)] = Total[tolower($1)] + (NF - 1);
  #print Total[tolower($1)];
}
{
	maxFrec = 0;
}
END {
	#Obtiene el total de palabras
	for (x in frecuencia){
		split(x, a, SUBSEP);
		totalPal++;
		if(a[1] == "ham") contHAM++;
		else contSPAM++;
	}
	#Imprime la palabra con su frecuencia	
	for (x in frecuencia) {
	    split(x, a, SUBSEP);
	    #if(frecuencia[x] > 50)
	    print a[1], a[2], frecuencia[x];#/totalPal;#/Total[a[1]];
	    #Para determinar la palabra con mayor frecuencia
	    if (frecuencia[x] > maxFrec){
	    	maxFrec = frecuencia[x];
	    	palMayor = a[2];
	    }
	    #totalPal++;
	    #print totalPal;
  }
  print "-------------------------------------"
  print "Palabra con mayor frecuencia : " palMayor " con " maxFrec " apariciones";
  print "Contador de palabras: " totalPal;
  print "Contador de palaHAM: " contHAM;
  print "Contador de palaSPAM: " contSPAM;
  print "-------------------------------------"
  print "** Probabilidad a priori **"
  print "P(HAM)= " contHAM/totalPal;
  print "P(SPAM)= " contSPAM/totalPal;
} ' $*