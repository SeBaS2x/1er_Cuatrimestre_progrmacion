def ordenar_array(lista, opciona =False ):
    for i in range(len(lista)):
        for j in range(i+1,len(lista), +1):
            if opciona == False:
                if lista[i]>lista[j]:
                    opcional = lista[i]
                    lista[i] =lista[j]
                    lista[j]= opcional
            else:
                if lista[i]<lista[j]:
                    opcional = lista[i]
                    lista[i] =lista[j]
                    lista[j]= opcional
    
    return lista
    
    
lista = [1,6,10,4,7,15,99]
ordenado = ordenar_array(lista, True)
print(ordenado)

