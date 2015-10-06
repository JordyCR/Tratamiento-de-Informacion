#!/usr/bin/awk -f
{
	mediaAncho[$2] += $3;
	mediaLargo[$2] += $4;
	n[$2]++;
	anchos[$2,n[$2]] = $3;
	largos[$2,n[$2]] = $4;
	#print n[$2];
	#print anchos[$2,n[$2]]
}
END{
	for(x in mediaAncho){
		#print x, n[x];
		mediaAncho[x] /= n[x];
		mediaLargo[x] /= n[x];

		for (i=1; i<=n[x]; i++){
			DesvAncho[x] += (anchos[x,i] - mediaAncho[x])^2;
			DesvLargo[x] += (largos[x,i] - mediaLargo[x])^2;
		}

		DesvAncho[x] /= n[x]-1;
		DesvLargo[x] /= n[x]-1;

		DesvAncho[x] = sqrt(DesvAncho[x]);
		DesvLargo[x] = sqrt(DesvLargo[x]);
		#print anchos[x,1];
		print x, mediaAncho[x], DesvAncho[x], mediaLargo[x], DesvLargo[x];
	}
}