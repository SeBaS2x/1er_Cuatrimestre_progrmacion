import random
import os
import time
from datos import *
from funciones import *
from output import *


categoria = seleccionar_categoria(generar_lista_categorias(diccionario_categorias))
palabra = seleccionar_palabra(diccionario_categorias[categoria])
palabra_oculta = ["_"] * len(palabra)
nueva_palabra_oculta = palabra_oculta.copy()
intentos = 7
puntaje = 0

def jugar_ahorcado(categoria,palabra,palabra_oculta,nueva_palabra_oculta,intentos,puntaje)->None:
    inicio = time.time()
    os.system("cls")
    
    while intentos>0:
        os.system("cls")
        print(f"Categoría seleccionada: {categoria}")
        print(f"Intentos restantes: {intentos}")
        print(f"\nPalabra:")
        mostrar_palabra_oculta(nueva_palabra_oculta)

        letra=ingresar_letra()
        actualizar_palabra_oculta(palabra,palabra_oculta,letra,intentos)
        if palabra_oculta == nueva_palabra_oculta:
            intentos -= 1
            puntaje -= 1
        else:
            puntaje += 3
        
        nueva_palabra_oculta=palabra_oculta.copy()
    print(f"Tu puntaje es de: {puntaje}")
    fin = time.time()
    tiempo=fin-inicio
        
    #guardar_puntuacion()



def guardar_puntuacion(diccionario_juego,categoria,puntaje,tiempo,usuario)->bool:
    guardado = False
    if len(categoria) > 0 and len(tiempo)> 0 and len(puntaje)> 0:
        diccionario_juego["Usuario"] = usuario
        diccionario_juego["Categoria"] = categoria
        diccionario_juego["Puntaje"] += puntaje
        diccionario_juego["Tiempo"] = tiempo
        guardado = True
    return guardado

def verificar_estado_juego(diccionario_juego:dict)->bool:
    pass

def calcular_puntuacion_final():
    pass


jugar_ahorcado(categoria,palabra,palabra_oculta,nueva_palabra_oculta,intentos,puntaje)