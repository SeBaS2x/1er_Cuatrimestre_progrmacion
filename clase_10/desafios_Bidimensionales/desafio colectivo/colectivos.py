import random
import sys
from os import system

from funciones_colectivo import *


##############3main################3
LINEAS = 3
COCHES = 5



def main() -> None:
    bandera_menu = True
    legajo = Lista_numeros_alatarios(15)
    matriz_unidades_en_circulacion = crear_matriz(LINEAS, COCHES, 0)
    while bandera_menu:
        print("OPCIONES:\n1. Cargar Plantilla de Recaudacion.\n2. Mostrar la REcaudacion de Cada Coche y linea.\n3. Calcular y Mostrar la recuadacion por linea.\n4. Calcular y Mostrar la recaudacion por coche.\n5. Calcular y Mostrar la Recaudacion Total.\n6. Salir Del Programa")
        opcion = int(input("Ingrese Una Ocion: "))
        match opcion:
            case 1:
                bandera = True
                while bandera:
                    numero_legajo = int(input("Ingrese su numero de legajo: 1-15 "))   
                    if verificar_legajo(legajo, numero_legajo):
                        print("Ingreso correcto..")
                        bandera = False
                    else:
                        print("Error ")
                        bandera= True
                print("--Ingreso De Datos--")
                recaudacion = int(input("Ingrese la recaudacion: "))
                while recaudacion < 0:
                    recaudacion = int(input("Ingrese la recaudacion: "))
                linea = int(input("Ingrese La Linea: "))-1
                while linea<  0 or linea>= LINEAS:
                    linea = int(input("Ingrese La Linea: "))-1
                coche = int(input("ingrese El Coche: "))-1
                while coche< 0 or coche>= COCHES:
                    coche = int(input("ingrese El Coche: "))-1
                
                matriz_unidades_en_circulacion[linea][coche] += recaudacion 
                # print(legajo)
            case 2:
                mostrar_matriz(matriz_unidades_en_circulacion)
            case 3:
                recaduacion_por_linea = sumar_linea_matriz(matriz_unidades_en_circulacion)
                print(f"La recaudacion por linea fueron: {recaduacion_por_linea}")
                
            case 4:
                recaduacion_por_coche = sumar_columnas_matriz(matriz_unidades_en_circulacion)
                print(f"La recaudacion por COCHE fue: {recaduacion_por_coche}")
            case 5:
                recaudacion_total = sumar_total_matriz(matriz_unidades_en_circulacion)
                print(f"La recaudacion Total es: {recaudacion_total}")
            case 6:
                sali = input("Quiere salir? (si/no)")
                if sali == "no":
                    bandera_menu = True
                else:
                    bandera_menu= False









































if __name__ == "__main__":
    sys.exit(main())
