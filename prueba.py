def desifrar_mensaje(mensaje:str)->str:
    """_summary_

    Args:
        mensaje (str): _description_

    Returns:
        str: _description_
    """
    desifrado = ""
    i = 0
    while i < len(mensaje):
        acumulador_de_tres_numeros = 0
        for j in range(3):
            digito = int(mensaje[i + j]) 
            acumulador_de_tres_numeros = acumulador_de_tres_numeros *10 + digito
        desifrado += chr(acumulador_de_tres_numeros)
        i += 3
    return desifrado

mensaje = "097112114117101098101110032101108032112097114099105097108"
desifrado = desifrar_mensaje(mensaje)
print(desifrado)