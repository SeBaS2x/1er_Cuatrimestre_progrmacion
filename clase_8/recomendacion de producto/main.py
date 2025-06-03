

def valores_encomun(lista1, lista2):
    lista_encomun = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]== lista2[j]:
                lista_encomun =  lista_encomun + [lista1[i]] 
    return lista_encomun



def productos_exclusivos(lista1, lista2):
    lista_exclusiva1= []
    lista_exclusiva2= []
    for i in range(len(lista1)): #recorro primera lista y hago una bandera para decir que no lo encontre, recorro la segunda lista y si coinciden los objetos pasa a true, sale del bucle y los que no entraron a la comparacion no cambiaron la bandera de valor esos objetos que no lograron cambiar la bandera se acumulan en la lista 
        encontrado = False 
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                encontrado=True
                break
        if encontrado == False:
            lista_exclusiva1 = lista_exclusiva1 + [lista1[i]]        
    for i in range (len(lista2)):
        encontrado = False
        for j in range(len(lista1)):
            if lista2[i]== lista1[j]:
                encontrado = True
        if encontrado == False:
            lista_exclusiva2 = lista_exclusiva2 +[lista2[i]]
    # print(f"Productos exclusivo del primer usuario: {lista_exclusiva1}")
    # print(f"Productos exclusivo del segundo usuario: {lista_exclusiva2}")
    return lista_exclusiva1, lista_exclusiva2
def sumar_listas(lista1,lista2):
    catalogo_total = []
    for i in range(len(lista1)):
        catalogo_total = catalogo_total + [lista1[i]]
    for j in range(len(lista2)):
        encontrado = False
        for k in range(len(catalogo_total)):
            if lista2[j] == catalogo_total[k]:
                encontrado = True
        if encontrado == False:
            catalogo_total = catalogo_total + [lista2[j]]
    return catalogo_total
###############MAIN#############################
usuario_1 = ["manteca", "azucar", "dulce", "chocolate", "yerba"]
usuario_2 = ["azucar", "yerba", "manzanas", "peras", "jugo"]
encomun = valores_encomun(usuario_1, usuario_2)
print(f"Los porductos que compraron en comun los dos usuarios son:\n {encomun}")
exclusivo1, exclusivo2 = productos_exclusivos(usuario_1, usuario_2)
print(f"Productos exclusivo del primer usuario: {exclusivo1}")
print(f"Productos exclusivo del segundo usuario: {exclusivo2}")
catalogo_total = sumar_listas(usuario_1, usuario_2)
print(f"Catalogo total comprados:\n {catalogo_total}")
print("-------------------------------")
print(f"Los productos recomendados para el Primer usuario son {exclusivo2}")
print(f"Los productos recomendados para el segundo usuario son {exclusivo1}")