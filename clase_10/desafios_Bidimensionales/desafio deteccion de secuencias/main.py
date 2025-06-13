
from funciones import *
import sys
from os import system

def main()-> None:
    matriz = crear_matriz(5, 5, 0)
    carga_alatorea_matriz(matriz)
    
    bandera = True
    while bandera:
        print("1. Cargar matriz\n.2 verificar existencia de secuencia de 2 numeros pares consecutivos\n.3 Determinar la cantid\n4  Identificar la secuencia más corta\n5. Identificar la secuencia más larga\n6. Salir")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                print("Cargando matriz...")
                carga_alatorea_matriz(matriz)
                mostrar_matriz(matriz)
            case 2:
                if buscar_secuencia(matriz):
                    print("Se encontraron dos numeros pares consecutivos.")
                else:
                    print("No se encontraron dos numeros pares consecutivos.")
            case 3:
                ocurrencias = contar_ocurrencias(matriz)
                print(f"La cantidad de ocurrencias de secuencias de dos numeros pares consecutivos es: {ocurrencias}")
            case 4:
                secuencia_corta = encontrar_secuencia_corta(matriz)
                print(f"La secuencia más corta es: {secuencia_corta}")  
                
            case 5:
                secuencia_larga = encontrar_secuencia_larga(matriz)
                if secuencia_larga:
                    print(f"La secuencia más larga es: {secuencia_larga}")
                else:
                    print("No se encontraron secuencias.")
            case 6:
                bandera = False
            case _:
                print("Opción no válida, intente nuevamente.")



if __name__ == "__main__":
    sys.exit(main())

