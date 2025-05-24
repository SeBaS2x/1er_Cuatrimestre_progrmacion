###1#######
# def sumar_naturales(numero:int)->int:
#     if numero == 0:
#         return 0
#     else: 
#         return numero + sumar_naturales(numero -1) 
    
    
#     pass

# suma = sumar_naturales(0)
# print(suma)


###2#####
# def calcular_potencia(base: int, exponente: int)->int:
#     if exponente ==0:
#         calculo =1
#     else:
#         calculo = base * calcular_potencia(base, exponente-1)
    
#     return calculo
#     pass

# resultado = calcular_potencia(2,3)
# print(resultado)

#######3###################
# def suma_digitos(numero: int)->int:
    
#     if numero == 0:
#         return 0
#     else:
#         ultimo_digito = numero % 10 
#         resto = numero // 10
#         return ultimo_digito + suma_digitos(resto)
# resultado = suma_digitos(1234)
# print(resultado)

########4##################

# from functools import lru_cache
# @lru_cache(maxsize=None)
# def calcular_fibonacci(numero: int)->int:
#     if numero == 0:
#         return 0
#     elif numero==1:  
#         return 1
#     else:
#         return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero-2)
    
# for i in range(34):

#     fibonacci = calcular_fibonacci(i)
#     print(fibonacci)