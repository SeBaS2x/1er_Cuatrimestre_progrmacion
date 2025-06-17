from especificas import *
def crear_vector(valor_inicial, cantidad) -> list:
    vector = [valor_inicial] * cantidad
    return vector

def cargar_vector(vector:list, mensaje):
    for i in range(len(vector)):
        vector[i] = int(input(mensaje)) 
    
def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])

def contar_positivos_negativos(vector)->str:
    contador_positivos = 0
    contador_negativo = 0
    for i in range(len(vector)):
        if es_positivo(vector[i]):
            contador_positivos += 1
        if es_negativo(vector[i]):
            contador_negativo += 1
    return f"Los numeros positivos son: {contador_positivos} y los Negativos: {contador_negativo}"

def sumar_pares_lista(vector):
    sumador = 0
    for i in range(len(vector)):
        if es_par(vector[i]):
            sumador += vector[i]
    return sumador

def mayor_numero_impar_lista(vector):
    mayor_impar = None
    for i in range(len(vector)):
        if es_impar(vector[i]):
            if mayor_impar== None or vector[i] > mayor_impar:
                mayor_impar = vector[i]
    return mayor_impar


def mostrar_pares_lista(vector):
    for i in range(len(vector)):
        if es_par(vector[i]):
            print(vector[i])

def posicion_impar_lista(vector):
    for i in range(1, len(vector), 2):
        print(f"Posicion {i}: {vector[i]}")