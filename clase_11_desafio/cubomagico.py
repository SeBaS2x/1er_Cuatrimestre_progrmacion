
#############FUNCIONES################
def suma_fila(matriz):
    suma_fila= []
    
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[0])):
            
            suma += matriz[i][j]  
            
            
            
        suma_fila = suma_fila +[suma]    
    return suma_fila

def verificar_suma_fila(resultado):
    for i in range(len(resultado)):
        if resultado[i] != resultado[0]:
            return False   
        
    return True

def suma_columna(matriz):
    suma_columna = []
    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j] 
        suma_columna = suma_columna + [suma]
    return suma_columna
def verificar_suma_columna(resultado):
    for i in range(len(resultado)):
        if resultado[i] != resultado[0]:
            return False   
        
    return True

def suma_diagonal(matriz):
    suma_diagonal = []
    suma = 0
    for  i in range(len(matriz)):
        
        
        suma +=matriz[i][i]
    return suma
def verificar_suma_diagonal(resultado, matriz):
    suma_filas = suma_fila(matriz)
    if resultado != suma_filas[0]:
        return False
    else:
        return True
###################MAIN###############

matriz = [[2, 7, 6 ],
          [9, 5, 1],
          [4, 3, 8]]
resultado_fila_matriz =suma_fila(matriz)
verificacion_suma_fila = verificar_suma_fila(resultado_fila_matriz)
print(resultado_fila_matriz)
print(verificacion_suma_fila)

resultado_columana_matriz = suma_columna(matriz)
verificacion_suma_columna = verificar_suma_columna(resultado_columana_matriz)
print(resultado_columana_matriz)
print(verificacion_suma_columna)

resultado_diagonal_matriz = suma_diagonal(matriz)
verificacion_suma_diagonal = verificar_suma_diagonal(resultado_diagonal_matriz, matriz)
print(resultado_diagonal_matriz)
print(verificacion_suma_diagonal)

if verificacion_suma_columna == True and  verificacion_suma_diagonal == True:
    print("La matriz es un cuadrado Magico")
else:
    print("La matriz No es un cuadrado Magico")