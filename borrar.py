
ancho = []
largo = []
clase = []
f = open('Hojas_mias.txt')
for line in f:
    fields = line.strip().split()
    # Array indices start at 0 unlike AWK
    #print(fields[1])
    ancho.append(fields[2])
    largo.append(fields[3])
    clase.append(fields[1])
print clase
#leertxt()