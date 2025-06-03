matriz = [[3,6,1],
          [4,3,9],
          [2,8,1],
          [9,5,9]
]

for j in range(len(matriz[0])): #Cantidad de Columnas
    for i in range(len(matriz)): # Cantidad de filas 
        print(matriz[i][j], end=" ")
    print(" ")