# #######1###########################
# def cargar_lista( cantidad) ->list:
#     lista =[None]*cantidad
#     for i in range(len(lista)):
#         lista[i] = int(input("ingrese un numero: "))
#     return lista

# lista = cargar_lista(5)
# print(lista)

######2##########

def cargar_lista(cantidad) -> list:
    lista = []
    for _ in range(cantidad):
        numero = int(input("Ingrese un número: "))
        lista.append(numero)
    return lista

# Nueva función que llama a la anterior
def ingresar_numeros(cantidad):
    lista = cargar_lista(cantidad)
    print("Lista ingresada:", lista)
    return lista

# Ejemplo de uso
ingresar_numeros(5)

### array unidimencionales.
#3
# def promedio_lista(lista:list):
#     suma = 0
#     for i in range(len(lista)):
#         suma += lista[i]
#     promedio = suma / len(lista)
#     return promedio

# lista =[3,5,7,9,10,5,7,8]
# promedio = promedio_lista(lista)   
# print(promedio) 

###4###

# def promedio_lista_positivo(lista:list):
#     suma = 0
#     contador_positivo = 0
#     for i in range(len(lista)):
#         if lista[i] >= 0:
#             suma += lista[i]
#             contador_positivo +=1
#     if contador_positivo == 0:
#         return None
#     promedio = suma / contador_positivo
#     return promedio

# lista=[-5,3,2,10,-9]
# positivo_promedio = promedio_lista_positivo(lista)
# print(positivo_promedio)

#5###

# def producto_lista(lista):
#     acumulador = 1
#     for i in range(len(lista)):
#         acumulador *= lista[i]
#     return acumulador

# lista = [2,4,2]
# producto = producto_lista(lista)
# print(producto)

##6###

# def posision_valor_maximo(lista):
#     maximo = lista[0]
#     indice_maximo = 0
#     for i in range(len(lista)):
#         if lista[i] > maximo:
#             maximo =lista[i]
#             indice_maximo = i
#     return indice_maximo


# lista=[3,10,11,4]
# posicion_maximo= posision_valor_maximo(lista)
# print(posicion_maximo)

##7##

# def posision_valor_maximo(lista):
#     maximo = lista[0]
#     indice_maximo = []
#     for i in range(len(lista)):
#         if lista[i] > maximo:
#             maximo =lista[i]
#     for i in range(len(lista)):
#         if lista[i]== maximo:
#             indice_maximo = indice_maximo + [i]
#     return indice_maximo

# lista=[3,10,11,4,11]
# posicion_maximo= posision_valor_maximo(lista)
# print(posicion_maximo)

##8########

# def remplazar_nombre(lista_nombre, nombre_antiguo, nombre_nuevo)-> int:
#     contador = 0
#     for i in range(len(lista_nombre)):
#         if lista_nombre[i] == nombre_antiguo:
#             lista_nombre[i] = nombre_nuevo
#             contador += 1        
#     return contador


# lista_nombres =["sebastian", "antonella", "julieta", "jose", "roberto", "maria"]
# remplazo = remplazar_nombre(lista_nombres, "jose", "San Martin")
# print(remplazo)
# print(lista_nombres)

###9###

# def interseccion_arrays(lista1, lista2,):
#     interseccion = []
#     for i in range(len(lista1)):
#         for j in range(len(lista2)):
#             if lista1[i]== lista2[j]:
#                 interseccion = interseccion + [lista1[i]]
#     return interseccion
    

# lista_1 =[1,4,5,7,8,9,99]
# lista_2 =[2,6,7,99,77]
# interseccion = interseccion_arrays(lista_1, lista_2)
# print (interseccion)

##10####

# def union_arrays_sin_repetir(lista1, lista2):
#     union = []
#     for i in range(len(lista1)):
#         union = union + [lista1[i]]
#     for j in range(len(lista2)):
#         bandera = False
#         for k in range(len(union)):
#             if lista2[j] == union[k]:
#                 bandera= True
#                 break
#         if bandera == False:
#             union = union +[lista2[j]]


    
#     return union

# lista_1 = [1,2,3,4,5]
# lista_2 = [6,7,8,9,10]
# union= union_arrays_sin_repetir(lista_1, lista_2)
# print(union)

##11###############################

def diferencias_array(lista1,lista2):
    no_repetidos =[]
    for i in range(len(lista1)):
        encontrado = False
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                
                encontrado =True
                break
        if encontrado== False:
            no_repetidos += [lista1[i]]    
    return no_repetidos

    pass
lista_1 = [1,3,7,2,3,4,5]
lista_2 = [6,7,8,9,1,5,10]

diferencias = diferencias_array(lista_1, lista_2)
print(diferencias)