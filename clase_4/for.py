
# #1###########################
# for i in range(1,11):
#     print(i)

# #2###########################
# for i in range(10,0,-1):
#     print(i)

# #3###########################
# numero = int(input("ingresar numero: "))

# for i in range(0, numero):
#     print(i)

# #4###########################
# numero = int(input("ingresar numero: "))

# for i in range(0, 11):
#     tabla = numero * i
#     print(f"{numero}x {i} = {tabla}")

# #5###########################

# contador = 0
# sumador= 0

# for i in range(1, 11):
#     numero = int(input("ingrese un numero: "))
#     if numero != 0:
#         contador +=1
#         sumador += numero
#     else:
#         break
# promedio = sumador / contador
# print(sumador)
# print(contador)
# print(promedio)

# #6###########################
# for i in range(1,11):
#     mukt = 3 * i
#     print(mukt)

# #7###########################
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)

# #8##########################
# for i in range(1, 11):
#     for j in range (1, i+1):
#         print(j, end="")
#     print()

# #9##########################
# numero = int(input("ingresar numero: "))
# contador = 0
# for i in range(1, numero+1):
#     if numero % i == 0:
#         print(i)  
#         contador +=1
# print(f"cantidad de divisores encontrados fueron {contador}")

# #10##########################
# numero = int(input("ingresar numero: "))
# primo = True
# for i in range(2, numero+1):
#     if numero % 1 == 0:
#         primo = False
#         break
# if primo == False:
#     print(f"{numero} es un número primo.")
# else:
#     print(f"{numero} no es un número primo.")

# # #11##########################
# numero = int(input("Ingrese un número: "))
# contador_primos = 0


# for num in range(2, numero + 1):
#     es_primo = True  

    
#     for i in range(2, num):
#         if num % i == 0:
#             es_primo = False
#             break
    
    
#     if es_primo:
#         print(num)
#         contador_primos += 1

# print(f"Se encontraron {contador_primos} números primos.")