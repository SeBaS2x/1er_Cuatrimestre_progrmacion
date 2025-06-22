def swap(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

nombres = [ "María", "Juan","Sofía", "Carlos", "Lucía", "Elena", "Diego"]
edades = [25, 30, 22, 28, 35, 27, 24]
alturas = [1.65, 1.80, 1.70, 1.75, 1.60, 1.68, 1.72]

for i in range (0, len(nombres)-1,1):
    for j in range(i + 1, len(nombres), 1):
        if nombres[i] > nombres[j]:
            swap(nombres, i, j)
            # aux = nombres[i]
            # nombres[i]= nombres[j]
            # nombres[j] = aux               #Preguntar a IA como tranformar esto a una mejor funcion
            swap(edades, i, j)
            # aux = edades[i]
            # edades[i]= edades[j]
            # edades[j] = aux 
            swap(alturas, i, j)
            # aux = alturas[i]
            # alturas[i]= alturas[j]
            # alturas[j] = aux 
        elif nombres[i]== nombres[j]:
            if edades[i] < edades[j]:
                swap(edades, i, j)
                # aux = edades[i]
                # edades[i]= edades[j]
                # edades[j] = aux 
                swap(alturas, i, j)
                # aux = alturas[i]
                # alturas[i]= alturas[j]
                # alturas[j] = aux

for i in range(len(nombres)):
    print(f"{nombres[i]:<10}{edades[i]:<5}{alturas[i]:<5}")

