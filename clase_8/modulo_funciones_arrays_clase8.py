def crear_vector(valor_inicial, cantidad) -> list:
    vector = [valor_inicial] * cantidad
    return vector

def cargar_vector(vector:list, mensaje):
    for i in range(len(vector)):
        vector[i] = int(input(mensaje)) 
    
def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])
        
def buscar_minimo(vector:list):
    for i in range(len(vector)):
        if i == 0 or vector[i]<minimo:
            minimo = vector[i]
    return minimo

def mostrar_posiciones_valor(vector, valor):
    bandera = False
    for i in range(len(vector)):
        if vector[i] == valor:
            print(i)
            bandera = True
    return bandera


def verificar_paridad(numero):
    es_par = True
    if numero % 2 != 0:
        es_par = False
    return es_par

def indicar_si_hay_impar(vector):
    encontro = False
    for i in range(len(vector)):
        if verificar_paridad(vector[i]) == False:
            encontro = True
    return encontro
def mostrar_postivos_negativos(vector: list)->list:
    for i in range(len(vector))
# crear =crear_vector(0,5)
# cargar_vector(crear, "ingresar numero del vector ")
# mostrar_vector(crear)