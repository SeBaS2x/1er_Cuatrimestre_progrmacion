import random

def crear_matriz(filas, columnas, valor):
    matriz = []
    for i in range(filas):
        valor_fila = [valor] * columnas
        matriz += [valor_fila]
    return matriz

def mostrar_matriz(matriz):
    print("         ", end="")
    for j in range(5):
        print(f"coche {j+1:>2}", end="  ")
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz [i][j], end= " ")
        print(" ")


def Lista_numeros_alatarios(cantidad):
    if cantidad > 100:
        return "Error: no se pueden generar más de 100 números únicos entre 1 y 100."
    
    lista = []
    cantidad_actual = 0

    while cantidad_actual < cantidad:
        numero = random.randint(1, 16)

        # Verificar si el número ya está en la lista (sin usar 'in')
        repetido = False
        for i in range(cantidad_actual):
            if lista[i] == numero:
                repetido = True
                break

        if not repetido:
            lista += [numero]
            cantidad_actual += 1

    return lista

def verificar_legajo(lista:list, numero_a_validar:int)->bool:
    for i in range(len(lista)):
        bandera = False
        if lista[i] == numero_a_validar:
            bandera = True
            return True
    if bandera == False:
        return False 



matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]


def sumar_linea_matriz(matriz:list)->list:
    lista_suma = []
    for i in range(len(matriz)):
        suma =0 
        for j in range(len(matriz[0])):
            suma += matriz[i][j]
        lista_suma = lista_suma + [suma]
    return lista_suma

def sumar_columnas_matriz(matriz:list)->list:
    lista_suma_columnas =[]
    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma+= matriz[i][j]
        lista_suma_columnas = lista_suma_columnas +[suma]
    return lista_suma_columnas
# suma = sumar_columnas_matriz(matriz)
# print(suma)
# sumaf= sumar_linea_matriz(matriz)
# print(sumaf)
def sumar_total_matriz(mariz):
    suma_total= []
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            suma  +=  matriz[i][j]
    suma_total = suma_total + [suma]
    return suma_total
    

# st= sumar_total_matriz(matriz)
# print(st)