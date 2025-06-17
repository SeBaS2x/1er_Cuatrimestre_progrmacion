def crea_matriz(cantidad_filas, Cantidad_columnas, Valor_inicial):
    matriz =[]
    for i in range(cantidad_filas):
        fila =[Valor_inicial]*Cantidad_columnas
        matriz+=[fila]
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz [i][j], end=" ")
        print(" ") 

def cargar_matriz(matriz):# recive la matriz incializada con todo NONE
    for i in range(len(matriz)): #recorro las filas
        for j in range(len(matriz[i])): #recorro las caloumnas 
            matriz[i][j]= int(input(f"ingresar valor para la matriz: {[i,j]}:"))
#################################################

M = 2
N = 3
# matriz = [[None ]*N for _ in range(M)] #COmprencion de lista,, "magia de python"
matriz=crea_matriz(N,M,None)
cargar_matriz(matriz)
mostrar_matriz(matriz)
print(matriz)