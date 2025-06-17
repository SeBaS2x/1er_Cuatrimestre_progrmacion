from datos_personas_con_puntos import datos
# {'nombre': 'Carlos', 
#  'edad': 30,
#  'soltero': False,
#  'hobbies': ['fotografía', 'ciclismo', 'ajedrez'],
#  'email': 'carlos0@mail.org',
#  'puntos': 979},

#listado de los datos (nombre, edad y hobbies)



def mostrar_persona(persona):
    print(f"{persona["nombre"]:<15}{persona["edad"]:<5}", end= " ") #diccionario nombre 
    for hobbies in persona["hobbies"]: #recorremos la lista del diccionario hobbies
        print(hobbies, end=" - ")
    print("")  #la mostramos igual que en la matriz 

def mostrar_datos(lista_personas: list):
    for persona in lista_personas: #recorre diccionarios 
        mostrar_persona(persona)

def mostrar_luis(lista_depersonas: list):
    for persona in lista_depersonas:
        if persona["nombre"] == "Luis": #funciona como filtro para la funcion de abajo 
            mostrar_persona(persona)
        

def mostrar_por_nombre(lista_depersonas: list, nombre):
    for persona in lista_depersonas:
        if persona["nombre"] == nombre: #cambio a Luis por un parametro
            mostrar_persona(persona)

def mostrar_por_edad(lista_depersonas: list, edad):
    for persona in lista_depersonas:
        if persona["edad"] == edad: #cambio nombre por edad
            mostrar_persona(persona)

def mostrar_por_clave(lista_depersonas: list, valor, clave):
    for persona in lista_depersonas:
        if persona[clave] == valor: #Se cambia la condicion de busqueda por clave"clave del diccionario" y valor que se busca
            mostrar_persona(persona)

def mostrar_mayor_claves(lista_persona:list, clave, mensaje):
    maximo= calcular_maximo(lista_persona, clave)
    print(f"{mensaje}{maximo}")
    # for persona in lista_persona:
    #     if persona["edad"]== maximo: ## para agregarle el nombre y se cambia por una funsion ya hecha 
    #         print(persona["nombre"])
    mostrar_por_clave(lista_persona, maximo, "edad")

def calcular_maximo(lista_persona, clave ):
    maximo = 0 
    for persona in lista_persona:
        if persona[clave]> maximo :
            maximo= persona[clave]
    return maximo

def mostrar_sin_hobbies(lista_persona:list, valor, clave):
    

                
# mostrar_sin_hobbies(datos,[],"hobbies")


# mostrar_datos(datos)

# mostrar_luis(datos)

# nombre ="Luis"
# mostrar_por_nombre(datos, nombre)

# mostrar_por_edad(datos, 20)

# mostrar_por_clave(datos, True, "soltero")

# mostrar_mayor_claves(datos, "edad", "la mayo edad es: ")
# print(" ")
# mostrar_mayor_claves(datos, "puntos", "El mayor puntaje es: ")
