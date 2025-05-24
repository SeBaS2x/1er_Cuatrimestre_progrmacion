CARGO_FIJO = 7000
COSTO_METRO =200
bonificacion = 0
recargo = 0
IVA = 0.21

#ENTRADA
tipo_cliente= str(input("Indique que tipo de cliente es: residencial - comercial- industrial: "))
cantidad_metros= float(input("ingrese cantidad de metros:"))
#PROCESOS
subtotal_consumo= (cantidad_metros * COSTO_METRO) + CARGO_FIJO

if tipo_cliente== "residencial":
    if cantidad_metros < 30:
        print("bonificacion 10%")
        bonificacion = 0.1
    elif cantidad_metros > 80:
        print("recargo 15%")
        recargo= 0.15
    if subtotal_consumo < 35000:
        bonificacion += 0.5 # el += quiere decir que se suma 0.5 a la bonificacion previamente seteada.
elif tipo_cliente == "comercial":
    if cantidad_metros > 300:
        print("bonificacion 8%")
        bonificacion = 0.8
    elif cantidad_metros >150:
        print("bonificacion 10%")
        bonificacion= 0.1
    else:
        print("recargo 5%")
        recargo = 0.05
elif tipo_cliente == "industrial":
    if cantidad_metros > 1000:
        print("bonificacion 30%")
        bonificacion = 30
    elif cantidad_metros > 500:
        print("bonificacion 20%")
        bonificacion = 0.2
    elif cantidad_metros < 200:
        print("recargo 30")
        recargo = 0.3

total_bonificacion = subtotal_consumo * bonificacion

total_recargo= subtotal_consumo * recargo

subtotal_porcentaje_aplicado = subtotal_consumo + total_recargo - total_bonificacion

importe_iva= subtotal_porcentaje_aplicado * IVA
total_a_pagar =subtotal_porcentaje_aplicado + importe_iva


#SALIDAS
print(f"el subtotal de consumo es: {subtotal_consumo}")
print(f"el total de bonificacion es {total_bonificacion}")
print(f"el total de recargo es {total_recargo}")
print(f"el subtotal con recargo y bonificaciones es: {subtotal_porcentaje_aplicado}")
print(f"el iva es: {importe_iva}")
print(f"el total a pagar es: {total_a_pagar}")
#La letra f de "form"es un interpolado que te permite ahorra en comas y funcional para cuando hay que mostrar varias variables.
