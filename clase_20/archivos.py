# .txt
#Para todo se abre, se usa y se cierra porque si no se puede corromper o no se puede mover, pasan cosas indeseables.
#TRaer los datos del archivo al programa o cargar datos al archivo.

# archivo = open("Archivo.txt" , "w") #Lectura
# archivo.write("augusto")
# archivo.close() #No olvidar de cerrar el archivo

#lectura
# archivo = open("Archivo.txt" , "r")
# contenido = archivo.read()# Esto recorre un string 
# #Puede que si le padsas parametros te lea la acantidad de datos indicado 
# archivo.close()
# print(contenido)

#Listas 
#Escritura 
# lista = ["german" , "ezequiel", "gonza"]
#el with administra un contexto particular, cuando salgo del bucle with se excluye
# with open("Archivo.txt", "w") as archivo:
#     for nombre in lista:
#         archivo.write(f"{nombre}\n")

#Lectura
# archivo = open("Archivo.txt" , "r")
# contenido = archivo.read()
# archivo.close()
# print(contenido)

#Que asa si quiero traer una linea sola?

# archivo = open("Archivo.txt" , "r")
# lista = archivo.readlines()
# archivo.close()#el archivo

# for linea in lista:
#     print(linea, end="")

#CSV : Comma separated values(valores separados por comas)
#Escritura 

# nombre = ["Jose", "Maria", "Luis"]
# apellido = ["Gomez", "Ruiz", "Martinez"]
# edades = [20,21,22]
# #La idea e spoder crear el archivo y que pueda ser leido en cualquier lenguaje
# #Esto es un archivo plano
# #Si se pone ; interpolado en el mensaje si se abre con excel por cada columna. 
# with open("agenda.csv", "w") as archivo:
#     for i in range(3):
#         mensaje= f"{nombre[1]}, {apellido[i]}, {edades[i]}\n"
#         archivo.write(mensaje)

# #Lectura
import re
# with open("agenda.csv", "r", encoding="UTF8") as archivo:
#     for linea in archivo:
#         # valores = linea.split(",")
#         valores = re.split(",|\n", linea) #maaagiaaa
#         print(f"{valores[0]} - {valores[1]} - {valores[2]}")


#JSON : JavaScript Object Notation (Notacion de objetos de Javascript)
#Esto va a ir para configuraciones
import json
# #Escribir
# data = {}
# data["clientes"] = []
# data["clientes"].append({"nombre" : "Juan", "edad": 20})
# data["clientes"].append({"nombre" : "Luis", "edad": 36})

# with open("ar.json", "w") as archivo:
#     json.dump(data, archivo, indent = 1)

#Lectura
# with open("ar.json", "r") as archivo:
#     data = json.load(archivo)

# print(data)

#PARSEAR
def parsear_csv(path:str) -> list:
    lista = []
    archivo = open(path, "r", encoding= "UTF8")
    for line in archivo:
        lectura = re.split(",|\n", line)
        dato = {}
        dato["id"] = lectura[0]
        dato["nombre"] = lectura[1]
        dato["apellido"] = lectura[2]
        dato["edad"] = lectura[3] #Corregir el tema de que la primer linea es "edad"
        lista.append(dato)
    archivo.close()
    return lista

# lista_1 = parsear_csv("MOCK_DATA.csv")
# print(lista_1)

def generar_csv(path:str, lista:list):
    with open(path, "w", encoding = "utf8") as archivo:
        delimitador = ","
        for i in lista:
            mensaje = "{0},{1},{2},{3}"
            mensaje = mensaje.format(i["id"],
                                     i["nombre"],
                                     i["apellido"],
                                     i["edad"])
            archivo.write(mensaje)

lista = parsear_csv("MOCK_DATA.csv")
generar_csv("nuevo.csv", lista)