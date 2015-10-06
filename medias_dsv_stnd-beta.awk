awk '{
	mediaAncha += $3;
	mediaLarga += $4;
	n[$2]++;
	Ancho[n[x],$2] = $3;
	Largo[n[x],$2] = $4;
}
END {
	for(x in mediaAncho){
		print x, n[x];
		mediaAncho[x] /= n[x];
		mediaLarga[x] /= n[x];

		for (i=1; i<=n[x]; i++){
			DesvAncho[x] += (Ancho[i,x] - mediaAncho[x])^2;
			DesvLargo[x] += (Largo[i,x] - mediaLargo[x])^2;
		}

		DesvAncho[x] /= (n[x]-1);
		DesvLargo[x] /= (n[x]-1);

		DesvAncho[x] = sqrt(DesvAcho[x]);
		DesvLargo[x] = sqrt(DesvLargo[x]);

		print mediaAncho[x], DesvAncho[x], mediaLargo[x], DesvLargo[x];
	}
}
