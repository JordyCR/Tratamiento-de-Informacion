{
	mediaAncho += $3;
	mediaLargo += $4;
	n++;
	anchos[n] = $3;
	largos[n] = $4;
}
END{
	mediaAncho /= n;
	mediaLargo /= n;

	for (i=1; i<=n; i++){
		DesvAncho += (anchos[i] - mediaAncho)^2;
		DesvLargo += (largos[i] - mediaLargo)^2;
	}
	
	DesvAncho /= n-1;
	DesvLargo /= n-1;

	DesvAncho = sqrt(DesvAncho);
	DesvLargo = sqrt(DesvLargo);

	print mediaAncho, DesvAncho, mediaLargo, DesvLargo;
}
