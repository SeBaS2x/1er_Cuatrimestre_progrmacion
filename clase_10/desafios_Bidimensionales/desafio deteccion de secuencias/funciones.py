from random import*
def crear_matriz(fila, columnas, valor):
    matriz = []
    for i in range(fila):
        filas = [valor] * columnas
        matriz += [filas]
    return matriz
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end=" ")
        print("")
def carga_alatorea_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]= randint(0,11)
def buscar_secuencia(matriz):
    for i in range(len(matriz)):
        secuencia =[]
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                secuencia = secuencia + [matriz[i][j]]
                if len(secuencia)== 2:
                    return True
                
def contar_ocurrencias(matriz):
    if not buscar_secuencia(matriz):
        return 0
    else:
        contador = 0
        for i in range(len(matriz)):
            secuencia = []
            for j in range(len(matriz[0])):
                if matriz[i][j] % 2 == 0:
                    secuencia = secuencia + [matriz[i][j]]
                    if len(secuencia) == 2:
                        contador += 1
                        secuencia = []
        return contador

def encontrar_secuencia_larga(matriz):
    secuencia_larga = []
    for i in range(len(matriz)):
        secuencia = []
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                secuencia = secuencia + [matriz[i][j]]
            else:
                if len(secuencia) > len(secuencia_larga):
                    secuencia_larga = secuencia
                secuencia = []
        if len(secuencia) > len(secuencia_larga):
            secuencia_larga = secuencia
    return secuencia_larga
def encontrar_secuencia_corta(matriz):
    secuencia_corta =[]
    for i in range(len(matriz)):
        secuencia = []
        for j in range(len(matriz[0])):
            if matriz[i][j] % 2 == 0:
                secuencia = secuencia + [matriz[i][j]]
            else:
                if len(secuencia) < len(secuencia_corta) or not secuencia_corta:
                    secuencia_corta = secuencia
                secuencia = []
        if len(secuencia) < len(secuencia_corta) or not secuencia_corta:
            secuencia_corta = secuencia         
    return secuencia_corta
