awk '{
	gsub(/[!$%&=?¡¿´¨""*{},_;:()+[\]\x2E-]/, " ", $0);
	for (i=1; i<=NF; i++){
		frecuencia[tolower($i)]++;
		total++;
	}
	next;
}
END{
	for (x in frecuencia) {
	    split(x, a, SUBSEP);
	    print a[1], "\t\t"frecuencia[x], "\t\t"frecuencia[x]/total;
  }
	print "---------------------------"
	print "Total de palabras = " total;
}
' $*