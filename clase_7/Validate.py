

def validar_numero(numero: int| float, minimo:int, maximo:int)-> bool:
    """Valida un numero, con un rango minimo y maximo, devuelve un booleano 

    Args:
        numero (int | float): _description_
        minimo (int): _description_
        maximo (int): _description_

    Returns:
        bool: _description_
    """
    if numero < minimo or numero > maximo:
        return True
    else:
        return False
    
# resultado = validar_numero(22,1, 10)
# print(resultado)

def validar_cadena(string: str, longitud: int):
    """funcion toma la longitud del string y si conicide devuelve true, sino false

    Args:
        string (str): _description_
        longitud (int): _description_

    Returns:
        _type_: _description_
    """
    if len(string) == longitud:
        return True
    else:
        return False
# cadena=validar_cadena("gol",4)
# print(cadena)

