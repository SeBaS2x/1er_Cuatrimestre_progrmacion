contador = 0
masculinos =0
iot =0
ia = 0
rv_ra= 0
masculinos_iot_ia = 0
contador_total = 0
contador_no_ia = 0
porcentaje_no_ia = 0
masculino_mayor = 0
nombre_mayor_masculino = ""
tecnologia_masculino_mayor = ""


while contador < 3: #cantidad de veces que se ejecuta
    nombre = input("Ingrese su nombre: ")
    
    edad = int(input("Ingrese su edad: "))
    while edad < 18 or edad > 99:
        edad = int(input("vuelva a ingresar su edad: "))
    
    genero = input("Ingrese su genero: Masculino/ Femenino/ Otros:  ").lower()
    while genero != "masculino" and genero != "femenino" and genero != "otros":
        genero = input("Vuelva a ingresar su genero: ").lower()
    if genero =="masculino":
        masculinos += 1
    
    tecnologia =input("Eliga una tecnologia.. IA, RV/RA, IOT : ").lower()
    while tecnologia != "ia" and tecnologia != "rv/ra" and tecnologia != "iot":
        tecnologia =input("Vuelva a ingresar una tecnologia.. IA, RV/RA, IOT : ").lower()
    
    if tecnologia == "ia":
        ia += 1
    elif tecnologia == "rv/ra":
        rv_ra += 1
    else:
        iot += 1  
##### finalizacion de pedido de informacion y validacion 

##### cantidad de masculino que votaron IOT o IA, cuya edad entra 25 y 50(inclusive)
    if genero == "masculino" and (tecnologia =="iot" or tecnologia == "ia") and edad >= 25 and edad <=50 :
        masculinos_iot_ia += 1 
    ### contador empleados NO votaron por Ia 
    if genero != "femenino" and edad > 33 and edad < 40:
        contador_total += 1
        if tecnologia != "ia":
            contador_no_ia += 1
    ####empleado masculino mayor edad##
    if genero == "masculino":
        if edad > masculino_mayor:
            masculino_mayor = edad
            nombre_mayor_masculino = nombre
            tecnologia_masculino_mayor = tecnologia
    
    contador += 1
    
### porcentaje empleados NO votaron por Ia           
if contador_total > 0:
    porcentaje_no_ia = (contador_no_ia / contador_total)* 100

print(f"Cantidad de empleados masculinos que votaron por IOT o IA entre 25 y 50 fueron {masculinos_iot_ia}")
print(f"Porcentaje de empleados que no votaron por IA, NO femenino, entre 33 y 40 años : {porcentaje_no_ia:.2f}%")
print(f"El empleado masculino de mayor edad... ")
print(f"Nombre : {nombre_mayor_masculino}, edad: {masculino_mayor}, tecnologia elegida: {tecnologia_masculino_mayor}")
