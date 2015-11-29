awk '
FILENAME==modelo {
	total++;
}
{
  if($1 == "spam"){
  	totalSpam++;
  	print $0
  }
  else {
  	totalHam++;
  	#print $0
  }
}
END{
	print "---------------------------"
	print "Total de msj = " total;
	print "Total de spam = " totalSpam;
	print "Total de ham = " totalHam;
}
' modelo=$1 $*