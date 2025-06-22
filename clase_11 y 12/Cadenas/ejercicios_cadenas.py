##1##################################
# def determinar_vocales(cadena:str)->list:
#     vocales = ["a","e","i","o","u"]
    
#     resultado =[]
#     for i in (vocales):
#         contador =0
#         for j in (cadena):
#             if i== j:
#                 contador += 1

#         resultado = resultado + [[i, contador]]

#     return resultado

# cadena = "murcielagito"
# for f in determinar_vocales(cadena):
#     print(f"{f[0]}:{f[1]}")

#2#######################################
# def encontrar_caracter(string, caracter):
#     for i in range(len(string)):
#         if string[i] == caracter:
#             return i
#     return -1

# cadena = "buenos aires"
# indice = encontrar_caracter(cadena, "s")
# print(indice)
###3######################################

# def determinar_palindromo(string):
#     n = len(string)

#     for i in range(n // 2):## para recrorrer la mitad del sting
#         if string[i] != string[n - 1 - i]:
#             return False  # si algún par no coincide, no es palíndromo

#     return True  # si todos los pares coinciden
       
# cadena = "otto"
# if determinar_palindromo(cadena):
#     print("Es palíndromo ")
# else:
#     print("No es palíndromo")
####4###################################
# def suprimier_caracter_repetido(cadena):
#     nueva_cadena = ""
#     for i in range(len(cadena)):
#             if cadena[i] != cadena[i-1]:
#                 nueva_cadena += cadena[i]
    
#     return nueva_cadena

# cadena="hoolaa"
# sin_repetir = suprimier_caracter_repetido(cadena)
# print(sin_repetir)

# ##5#############################################
# def suprimir_vocales(cadena):
#     nueva_cadena=""
#     vocales =["a","e","i","o","u"]
#     for i in range(len(cadena)):
#         es_vocal = False
#         for j in range(len(vocales)):
#             if cadena[i] == vocales[j]:
#                 es_vocal = True
#                 break
#         if es_vocal ==False:
#             nueva_cadena += cadena[i]
#     return nueva_cadena

# cadena="hoolaa"
# sin_vocal = suprimir_vocales(cadena)
# print(sin_vocal)
###6###############################333
# def contar_subcadena(cadena: str, subcadena: str) -> int:
#     contador = 0
#     largo_sub = len(subcadena)

#     for i in range(len(cadena) - largo_sub + 1):
#         coincidencia = True
#         for j in range(largo_sub):
#             if cadena[i + j] != subcadena[j]:
#                 coincidencia = False
#                 break
#         if coincidencia:
#             contador += 1

#     return contador

# print(contar_subcadena("El pan del panadero", "pan"))