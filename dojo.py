def crear_matriz(cantidad_filas, cantidad_columnas, valor_inicial)-> list:

    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

def multiplicar_matriz(matriz_1, matriz_2, matriz_3):
    acumulador = 0
    for i in range(len(matriz_1)):
        for j in range(len(matriz_2[0])):
            for k in range(len(matriz_2)):
                acumulador += matriz_1[i][k] * matriz_2[k][j]
            matriz_3[i][j] = acumulador
            acumulador = 0
    print(matriz_3)
    
    
#######################main############
matriz_1 = [[3,6],
            [5,2],
            [6,4]]
matriz_2 = [[3,5,7,9],
            [2,7,1,7],]

matriz_3 = crear_matriz(len(matriz_1), len(matriz_2[0]), 0 )

multiplicar_matriz(matriz_1,matriz_2,matriz_3)


# matriz_resultado =[[len(matriz_1)],[len(matriz_2)]]

# print(matriz_resultado)