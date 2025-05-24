# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.


respuesta = input("Quiere ingresar sus datos? si/no: ").lower()

while respuesta != "si":
    print("Nos vemos!!!")
    respuesta = input("Quiere ingresar sus datos? si/no: ").lower()
    
apellido = input("ingrese su apellido: ")
edad = int(input("ingrese su edad: "))
while edad < 18 or edad > 90:
    print("incorreto")     
    edad = int(input("ingrese su edad: "))    
estado = input("Ingrese su estado Civil: Soltero/a-Casado/a-Vidudo/a ").lower()
while estado != "soltero" and estado!= "soltera" and estado !="casado" and estado !="casada" and estado!="viudo" and estado != "viuda": 
    print("incorreto")
    estado = input("Ingrese su estado Civil: Soltero/a-Casado/a-Vidudo/a ").lower()    
legajo =int(input("Ingrese su numero de legajo: ")) 
while legajo < 1000 or legajo >9999:
    print("Incorrecto")
    legajo =int(input("Ingrese su numero de legajo: ")) 
print(f"Muchas gracias {apellido} por la informacion!!!")
print(f"edad: {edad}")
print(f"estado civil: {estado}")
print(f"numero de legajo: {legajo}")
print("Nos vemos!!!")
