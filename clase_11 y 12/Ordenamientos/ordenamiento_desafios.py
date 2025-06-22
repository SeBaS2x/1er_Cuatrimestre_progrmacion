# ##1########################################
# def ordenar_array(lista, opciona =False ):
#     for i in range(len(lista)):
#         for j in range(i+1,len(lista), +1):
#             if opciona == False:
#                 if lista[i]>lista[j]:
#                     opcional = lista[i]
#                     lista[i] =lista[j]
#                     lista[j]= opcional
#             else:
#                 if lista[i]<lista[j]:
#                     opcional = lista[i]
#                     lista[i] =lista[j]
#                     lista[j]= opcional
    
#     return lista
    
    
# lista = [1,6,10,4,7,15,99]
# ordenado = ordenar_array(lista, )
# print(ordenado)

#2#############################
def ordenar_vector(vector:list, opcional = True)->list:
    
    for i in range(len(vector)-1):
        for j in range(i+1,len(vector),1):
            if opcional:
                if vector[i] >vector[j]:
                    aux = vector[i]
                    vector[i]= vector[j]
                    vector[j]= aux
            else: 
                if vector[i] < vector[j]:
                    aux = vector[i]
                    vector[i]= vector[j]
                    vector[j]= aux
    return vector   
# vector_1= [6,9,3,99,1,0,5,3,]
# vector_2= [4,2,8,7,55,30,151,100]
# vector_1_ordenado = ordenar_vector(vector_1)
# vector_2_ordenado = ordenar_vector(vector_2)

# def intecalar_vectores(vector1, vector2, bool=True)->list:
#     lista_junta = []
#     for i in range(len(vector1)):
#         lista_junta += [vector1[i]]
#     for j in range(len(vector2)):
#         lista_junta += [vector2[j]]
#     ordenar_vector(lista_junta,bool)
    

#     return lista_junta

# vector_intercalado = intecalar_vectores(vector_1_ordenado,vector_2_ordenado,False)
# print(vector_1_ordenado)
# print(vector_2_ordenado)
# print(vector_intercalado)
########3#############################
def ordenar_vector_con_nega(vector:list, )->list:
    lista_nueva_negativos =[]
    lista_nueva_positivos = []
    for i in range(len(vector)):
        if vector[i] < 0:
            lista_nueva_negativos += [vector[i]]
        else:
            lista_nueva_positivos +=[vector[i]]
    orden_negativo= ordenar_vector(lista_nueva_negativos, False)
    orden_positivo= ordenar_vector(lista_nueva_positivos)
    vector = orden_negativo + orden_positivo
            
    return vector

lista=[-1,-4,-5,-6,-8,-2,-9,0,1,2,3,4,5,6,7,8,]
orden= ordenar_vector_con_nega(lista)
print(orden)


