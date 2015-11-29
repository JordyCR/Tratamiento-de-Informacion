awk '
FILENAME==model{
  modelo[$1,$2]=$3;
  clases[$1]=1;
  if($1 == "ham") contHAM++;
  else contSPAM++;
  #print modelo[$1,$2];
  #for (x in classes) print x;
  #print $1, $2;
  next;
}
FILENAME==prueb{ 
  prueba[$1]=tolower($2);
  print "*** FRASE: " $0;
 next;
} 
BEGIN {
  EPSILON = 0.00001;
  TOTALPAL = 10201;
  PSPAM = 0.2972;
  PHAM = 0.7027;
  pSPAM1 = 1;
  pHAM1 = 1;
  pTraining =1;
  print "--------------------BEGIN------------------------------------";
  #print EPSILON+1;
  print "--------------------------------------------------------";
}
END{
  print "---------------- END ----------------------------------------";
  print "WORD  FREQ  P(B/SPAM)  P(B/HAM)  P(B)";
  for (i=1; i<=NF; i++) {
    if (("spam",tolower($i)) in modelo){ #Si la palabra existe en el corpus SPAM
      pSPAM1 *= modelo["spam",tolower($i)] / contSPAM;
      pS = modelo["spam",tolower($i)] / contSPAM;
      #pTraining *= (modelo["spam",$i] + modelo["ham",$i]) / TOTALPAL;
    }
    else{
      pSPAM1 *= EPSILON / contSPAM;
      pS = EPSILON / contSPAM;
    }
    if (("ham",tolower($i)) in modelo){ #Si la palabra existe en el corpus HAM
      pHAM1 *= modelo["ham",tolower($i)]  / contHAM;
      pH = modelo["ham",tolower($i)]  / contHAM;
      #pTraining *= (modelo["spam",$i] + modelo["ham",$i]) / TOTALPAL;
    }
    else{
      pHAM1 *= EPSILON / contHAM;
      pH = EPSILON / contHAM;
    }
    print tolower($i) , modelo["spam",tolower($i)] + modelo["ham",tolower($i)], pS, pH, (modelo["spam",tolower($i)] + modelo["ham",tolower($i)]) / TOTALPAL;
  }
  print "--------------------------------------------------------";
  #print modelo["spam","customer"];
  #print "P(B/SPAM) = (" pSPAM1 " * " PSPAM ") / "pTraining " = "(pSPAM1 * PSPAM);# / pTraining; 
  #print "P(B/HAM) = (" pHAM1 " * " PHAM ") / "pTraining " = "(pHAM1 * PHAM);# / pTraining;
  print "P(B/SPAM) = " pSPAM1 * PSPAM;# / pTraining; 
  print "P(B/HAM) = " pHAM1 * PHAM;# / pTraining;
  if ((pSPAM1 * PSPAM) > (pHAM1 * PHAM)) print "El msj es SPAM";
  else print "El msj es HAM";
  print "--------------------------------------------------------";
  #print contSPAM;
}' model=$1 prueb=$2 $*