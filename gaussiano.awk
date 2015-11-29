awk '
FILENAME==modelo {
	Ancho[$1] = $2;
	DsvAncho[$1] = $3;
	Largo[$1] = $4;
	DsvLargo[$1] = $5;
	clase[$1] = 1;
	next;
}
{
	# print " ----> " $0 " <---- ";
	altura_global = 0;
	
	for (c in clase) {
		altura = (1/(DsvAncho[c] * DsvLargo[c]*2*3.14159)) * exp(-1 * (( ($3-Ancho[c])**2 / (2*DsvAncho[c]**2)) + ($4-Largo[c])**2 / (2*DsvLargo[c]**2)));
			
		if (altura > altura_global) {
			altura_global = altura;
			clase_ganadora = c;
		}
	}	

	print $0 " --- " clase_ganadora, distancia_global;
	if ($2 ==  clase_ganadora) Exactitud++;
	else Errores++;
}
END{
	print "---------------------RESUMEN---------------------";
	print "Exactitud " (Exactitud/(Exactitud+Errores))*100 "%";
}' modelo=$1 $*