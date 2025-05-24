def crea_matriz(cantidad_filas, Cantidad_columnas, Valor_inicial):
    matriz =[]
    for i in range(cantidad_filas):
        fila =[Valor_inicial]*Cantidad_columnas
        matriz+=fila
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz [i][j], end="")
        print("")    



#################################################
#creacion matri< MxN
M = 5
N = 3
# matriz = [[None ]*N for _ in range(M)] #COmprencion de lista,, "magia de python"
matriz=crea_matriz(N,M,None)
mostrar= mostrar_matriz(matriz)
print(matriz)
