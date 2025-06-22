import random

def buscar_elementos_diccionarios(diccionario:dict, opcion:str, valor:str=None) -> list:
    '''
    Busca y devuelve en formato lista, los elementos de un diccion
    key = devuelve una lista con las llaves
    value = devuelve una lista con los valores del diccionario
    '''
    lista_elementos = []
    for elemento in diccionario:
        if opcion == "key":
            lista_elementos.append(elemento)
        elif opcion == "value":
            if valor != None:
                for elemento in diccionario[valor]:
                    lista_elementos.append(elemento)
            else:
                for elemento in diccionario:
                    lista_elementos.append(diccionario[elemento])
    return lista_elementos

def generar_lista_categorias(diccionario_categorias:list):
    lista_categorias = []
    for clave in diccionario_categorias:
        lista_categorias.append(clave)
    return lista_categorias
    
def seleccionar_categoria(lista_categorias:list) -> str:
    categoria = obtener_elemento_aleatorio(lista_categorias)
    return categoria

def seleccionar_palabra(lista_palabras:list)->str:
    palabra =  obtener_elemento_aleatorio(lista_palabras)
    return palabra

def obtener_elemento_aleatorio(lista_elementos:list)->any:
    elemento=random.choice(lista_elementos)
    return elemento

def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo_len:int, maximo_len:int)->str:
    while True:
        nombre = input(mensaje).strip()
        if minimo_len <= len(nombre) <= maximo_len:
            return nombre
        else:
            print(mensaje_error)



def actualizar_palabra_oculta(palabra,palabra_oculta,letra,intentos):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
    return palabra_oculta

def ingresar_letra()->str:
    while True:
        letra=input("Ingrese una letra: ").strip().lower()
        if len(letra) == 1 and letra.isalpha():
            break
    return letra

def obtener_lista_palabras(diccionario_categorias:dict, categoria:str) -> list:
    lista_palabras = diccionario_categorias[categoria]
    return lista_palabras 

