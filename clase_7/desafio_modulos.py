from Validate import*
##########1#################


def tomar_entero(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) ->int|None:
    """Solicita un número entero dentro de un rango con intentos limitados

    Args:
        mensaje (str): Pedir numero.
        mensaje_error (str): en caso de que no reciva un entero, dara mensaje de error.
        minimo (int): seleccion de rango minimo que acepta la funcion.
        maximo (int): seleccion de rango maximo que acepta la funcion.
        reintentos (int): cantidad de veces que podes ingresar numeros.

    Returns:
        int|None: devuelve un entero o None.
    """
    entero =int(input(mensaje))
    # while entero < minimo or entero > maximo:  ##PREVIO A REALIZAR LA VARIABLE DEL MODULO VALIDATE.PY
    #     reintentos -= 1
    #     if reintentos > 0:
    #         entero =int(input(mensaje_error))    
    #     else:
    #         return None    
        
    # return entero
    while validar_numero(entero, minimo, maximo): ###UTILIZANDO LA VARIABLE DEL MODULO VALIDATE.PY
        reintentos -= 1
        if reintentos > 0:
            entero =int(input(mensaje_error))
        else:
            return None
    return entero    

numero = tomar_entero("Ingrese un numero dentro del rango 1-10: ", "Error, vuelva a ingresar el numero: ", 1,10,3)
print(numero)

##############2##################

def tomar_flotante(mensaje: str, mensaje_error: str, minimo: int, maximo:int, reintentos: int) ->float|None:
    """Solicita un número flotante dentro de un rango con intentos limitados

    Args:
        mensaje (str): Pedir numero.
        mensaje_error (str): en caso de que no reciva un flotante, dara mensaje de error.
        minimo (int): seleccion de rango minimo que acepta la funcion.
        maximo (int): seleccion de rango maximo que acepta la funcion.
        reintentos (int): cantidad de veces que podes ingresar numeros.

    Returns:
        float|None: devuelve un flotante o None.
    """
    flotante = float(input(mensaje))
    while validar_numero(flotante, minimo, maximo):  ## uUTILIZANDO LA VARIABLE DEL MODULO VALIDATE.PYt
        reintentos -= 1
        if reintentos > 0:
            flotante = float(input(mensaje_error))    
        else:
            return None    
        
    return flotante

numero = tomar_flotante("Ingrese un numero dentro del rango 1.0-10.0: ", "Error, vuelva a ingresar el numero: ", 1,10,3)
print(numero)
    ########3#######################
    ##En el punto numero 3 no puedo hacer que me devuelva un None en caso de que no coincidan la cantidad de caracteres 

def tomar_string(longitud: int) -> str|None:
    """funcion toma la longitud del string y si conicide devuelve string, sino None

    Args:
        longitud (int): cantidad de digitos del string

    Returns:
        str|None: devuelve el string ingresado o None
    """
    string = input("Ingrese un String: ")
    longitud = len(string)
    # if cantidad == longitud:
    #     return string
    # else:
    #     return None
    validacion= validar_cadena(string,longitud)
    if validacion == True:
        return string
    else:
        return None
    
    

cadena = tomar_string(9)
print(cadena)




