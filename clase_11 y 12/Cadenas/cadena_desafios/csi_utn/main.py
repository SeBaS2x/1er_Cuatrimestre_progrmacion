from Sospechosos import *
criminal = "CGTTTAATG"
largo_del_criminal = len(criminal) 
culpable = None

for i in range(len(sospechosos)):
    nombre = sospechosos[i]
    muestra = muestras[i]
    largo_muestra = len(muestra)


    for j in range(largo_muestra - largo_del_criminal + 1):
        subcadena = muestra[j:j + largo_del_criminal]
        if subcadena == criminal:
            culpable = nombre
            break
    if culpable:
        break
if culpable:
    print(f"El culpable es:  {culpable}, adn :{criminal}")
else:
    print("son todos inocentes")



