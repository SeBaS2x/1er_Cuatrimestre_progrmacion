# ###############1##################
# i = 10
# # while i < 10  :#mientras/ while condicional para salir del buclw
# i +=1    #i= i+1
# print (i)

# ##############2##################
# i = 10

# while i > 0:
#     i -= 1
#     # print(i+1)

# ##############3##################
# contador = 0
# i = 0
# while i != 10:
#     i+=1
#     contador += i
# print(f"la suma de los numeros del 1 al 10 es  {contador}")

# ##############4##################
# contador = 1
# suma = 0
# while contador <= 10:
#     if contador % 2 == 0 :
#         suma += contador
#     contador += 1
# print (suma)

# ##############5##################
# numero = 0 #contador, lo que mantiene mi bucle
# suma = 0 #acumulador, va ir sumando los valores ingresados

# while numero < 5:       ###mientras aún no hayamos llegado a 5 números
#     entrada = int(input("ingrese 5 numeros: "))  ###seguí pidiendo números mientras haya ingresado menos de 5”
#     suma += entrada
#     numero += 1
# promedio = suma / numero
# print(f"la suma es {suma} y el promedio de los 5 numeros es: {promedio}")

# ##############6##################
# suma= 0
# ingresos = 0
# respuesta= str(input("quierte ingresar un numero?: si/no"))
# if respuesta == "si":
#     while respuesta == "si":
#         numero = int(input("ingrese el numero: "))
#         suma += numero
#         ingresos += 1
#         respuesta= str(input("quierte ingresar un numero?: si/no"))
#     promedio= suma / ingresos
#     print(f"la cantidad de numeros son{ingresos}")
#     print(f"la suma total {suma}")
#     print(f"promedio final {promedio}")
# else:
#     print("no se ingresaron numeros")

# ##############7##################

# acumulador_positivos = 0
# productos_negativos = 1 #elemento neutro de la multiplicacion 1.
# respuesta = "si"


# while respuesta =="si":
#     numero = int(input("ingresar un numero: "))
#     if numero > 0:
#         acumulador_positivos += numero
#     elif numero < 0:
#         productos_negativos *= numero

#     respuesta = input("quiere ingresar otro numero ?: si/ no")

# print(acumulador_positivos)
# print(productos_negativos)

# ################8###################
# contador = 0
# suma= 0

# while contador < 5 :
#     entradas = int(input("ingrese un numero:"))
#     suma += entradas
#     contador += 1
# respuesta= str(input("¿Querés ingresar otro número? (si/no):"))
# while respuesta == "si" and contador <10:
#     entradas = int(input("ingrese un numero:"))
#     suma += entradas
#     contador += 1
#     respuesta= str(input("¿Querés ingresar otro número? (si/no): "))
# promedio= suma / contador

# print(f"la suma de los numeros es: {suma}")
# print(f"el promedio es: {promedio}")

# ################9###################

# contador = 0
# suma= 0

# while contador < 5 :
#     entradas = int(input("ingrese un numero:"))
#     suma += entradas
#     contador += 1
# respuesta= str(input("¿Querés ingresar otro número? (si/no):"))
# while respuesta == "si" and contador <10: ## para elejercicio 9 solo hayque agregarle una condicion masal seguundo bloque que sea como maximo 10
#     entradas = int(input("ingrese un numero:"))
#     suma += entradas
#     contador += 1
#     respuesta= str(input("¿Querés ingresar otro número? (si/no): "))
# print("ya ingresaste 10 numeos")##1
# promedio= suma / contador

# print(f"la suma de los numeros es: {suma}")
# print(f"el promedio es: {promedio}")


