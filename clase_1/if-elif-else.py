##########################1################

# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:

# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot


altura_jugador = float(input("inidque su altura: "))

if altura_jugador < 160:  
    print("Tu posicion Base")
elif altura_jugador >=160 and altura_jugador <179:
    print("Tu posicion Escolta")
elif altura_jugador >= 180 and altura_jugador < 199:
    print("Tu posicion Alero")
else:
    print("Tu posicion Ala-Pivot o pivot")

########################2##################
# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:

# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

nota= int(input("Indique su nota del 1 al 10: "))

if nota >= 6 :
    print(f"Pomocion directa, la nota es : {nota} ")
elif nota >= 4:
    print(f"Aprobado, su calificacion es: {nota}")
elif nota >= 1:
    print(f"Desaprobado, su calificacion es: {nota}")
else:
    print("vuelva a ingresar su Nota")