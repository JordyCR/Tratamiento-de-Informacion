BEGIN {
	chunk_part = 10; # Este valor va del 1 al 10 para conseguir los chunks
}
{
	if( (25 * (chunk_part-1) <= clase[$2]) && (clase[$2] < 25*chunk_part)){
		print $0;
	}
	clase[$2]++
}