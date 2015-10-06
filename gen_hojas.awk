awk '
BEGIN {
	chunk_part = 1; # Este valor va del 1 al 10 para conseguir los chunks
	cont = 0
}
{
	if( (250 * (chunk_part-1) <= cont) && (cont < 250*chunk_part)){
		print $0;
	}
	cont++
}'