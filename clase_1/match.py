# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”.
 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion_año = str(input("indique la estacion del año: "))
destino = str(input("indique su destino: "))
match estacion_año:
    case "invierno"  :
        if destino == "bariloche":
            print("SE VIAJA a bariloche")
        else:
            print("NO SE VIAJA")
    case "verano":
        if destino == "mar del plata":
            print("SE VIAJA a Mar del plata.")
        elif destino == "cataratas":
            print("SE VIAJA a las cataratas")
        else:
            print("NO SE VIAJA")
    case "otoño":
        print("SE VIAJA a todos los lugares.")
    case "primavera":
        if destino == "bariloche":
            print("NO SE VIAJA")
        else:
            print("SE VIAJA a todos los lugares menos Bariloche.")