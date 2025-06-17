import sys
from arrays_generales import *
from os import system
from colorama import *

def main() -> None:
    bandera_manu = True
    vector = crear_vector(None, 5)
    bandera_carga = False
    while bandera_manu:
        print(Back.RED + Fore.BLACK+"1. Ingresar numeros:\n2. Cantidad de numeros positivos y negativos \n3. Suma de numeros pares\n4. Mayor numero impar\n5. Listar numeros ingresados\n6. Listar numeros pares\n7. Listar numeros en posiciones impares\n8. Salir del programa")
        opcion = int(input("Ingrese una opcion: "))
        match opcion:
            case 1:
                cargar_vector(vector, "Ingrese un numero: ")
                    
                
                bandera_carga= True
            case 2: 
                if bandera_carga == True:
                    contador = contar_positivos_negativos(vector)
                    print(contador)
                else:
                    print("Vuelva a la primera opcion")
            case 3: 
                if bandera_carga == True:
                    sumar_pares = sumar_pares_lista(vector)
                    if sumar_pares:
                        print(f"La suma de los numeros pares ingresados es :{sumar_pares}")
                    else:
                        print("No se ingreso ningun numero par")
                else:
                    print("Vuelva a la primera opcion")        
            case 4:
                if bandera_carga == True:
                    mayor_impar = mayor_numero_impar_lista(vector)
                    print(f"El mayor Numero Impar ingresado fue: {mayor_impar}")
            case 5:
                if bandera_carga == True:
                    mostrar_vector(vector)
                else:
                    print("Vuelva a la primera opcion")  
            case 6:
                if bandera_carga == True:
                    if mostrar_pares_lista(vector):
                        pass
                    else:
                        print("no hay numeros pares en la lista")
                else:
                    print("Vuelva a la primera opcion")  
            case 7:
                if bandera_carga == True:
                    posiciones_impares = posicion_impar_lista(vector)
                    print(posiciones_impares)
                else:
                    print("Vuelva a la primera opcion")      
            case 8:
                bandera_manu = False
        system("pause")
        system("cls")














if __name__ == "__main__":
    sys.exit(main())