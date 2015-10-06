awk '
FILENAME==modelo {
	Ancho[$1] = $2; 
	Largo[$1] = $4;
	clase[$1] = 1;
	next;
}
{
	#print " ----> " $0 " <---- "
	distancia_global = 999999;
	for (c in clase) {
		distancia = sqrt(($3-Ancho[c])**2 + ($4-Largo[c])**2);
		# if (distancia == -1) { 
		# 	distancia_global = distancia; 
		# 	clase_ganadora = c;
		# }
		if (distancia < distancia_global) {
			distancia_global = distancia;
			clase_ganadora = c;
		}
		# print c, distancia;
	}	
	# print $0 " --- " clase_ganadora, distancia_global;
	if ($2 ==  clase_ganadora) Exactitud++;
	else Errores++;

}
END{
	print "---------------------RESUMEN---------------------";
	print "Exactitud " (Exactitud/(Exactitud+Errores))*100 "%";
}' modelo=$1 $*