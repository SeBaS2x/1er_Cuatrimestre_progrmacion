# cadena = "Algo mas largo"
# contador_o = 0 
# for i in range(len(cadena)):
#     if cadena[i] == "o":
#         contador_o += 1

# print(contador_o)
###########################################################
# cadena = "HOLA"
# # print(ord("a")) #devuelve el codigo ASCI de esa letra
# # print(chr(97)) #devuelve la letra perteneciente al codigo ASCI
# cadena_convertida = ""
# for i in range(len(cadena)):
#     orden_letra_nueva = ord(cadena[i] )+32 # le suma para que el ASCI sea pase a minuscula
#     # print(chr(orden_letra_nueva)) # con chr muestra el AScI sumado 
#     char_letra_nueva = chr(orden_letra_nueva)
#     cadena_convertida += char_letra_nueva

# print(cadena_convertida)
#########################################################3
# cadena = "H9LA@iaq"
# cadena_convertida = ""

# for i in range(len(cadena)):
#     caracter = caracter[i] #obtengo el caracter de la cadena
#     orden_caracter = ord(caracter) #obtengo el codigo ASCI del caracter
#     if orden_caracter >= 65 and orden_caracter<=90: #si el caracter es una letra mayuscula
#         caracter = chr(orden_caracter +32) #lo convierto a minuscula

#     cadena_convertida += caracter #agrego el caracter convertido a la cadena convertida

# print(cadena_convertida)
###############################################3333

def buscar_caracter(un_caracter, caracteres_validos):
    encontro = False
    for i in range(len(caracteres_validos)):
        if caracteres_validos[i] == un_caracter:
            encontro = True
            break
    return encontro


cadena = "HoLa333" 
caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
cadena_minuscula = ""
for i in range(len(cadena)):
    caracter= cadena[i]  # obtengo el caracter de la cadena
    if buscar_caracter(caracter, caracteres_validos):
        conversion = ord(caracter) +32 # convierto a minuscula
        caracter = chr(conversion) # convierto a minuscula    
    
    cadena_minuscula += caracter # agrego el caracter convertido a la cadena minuscula
    
print(cadena_minuscula)  # muestro la cadena convertida a minuscula