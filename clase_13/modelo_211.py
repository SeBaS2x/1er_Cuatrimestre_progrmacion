
from ordenamiento import*



usuarios = ["juan", "martin", "laura", "antonella", "messi", "maradona","maria","leo","pele","slash", "leandro", "sebastian", "agustin", "tomas", "oscar"]
empresas = ["empresa numero Uno", "la Dos", "tercera empresa"]
precio_accion = [300, 90, 150 ]

acciones = [ #fila = usuarios y columnas = a las compras de acciones de cada empresa, columna 1 empresa 1, columna dos empresa 2
            [10, 20, 15],  # juan
            [5, 12, 8],    # martin
            [7, 5, 10],    # laura
            [20, 10, 5],   # antonella
            [30, 15, 10],  # messi
            [25, 8, 12],   # maradona
            [15, 15, 15],  # maria
            [18, 22, 10],  # leo            
            [5, 5, 5],     # pele
            [40, 10, 20],  # slash
            [12, 18, 9],   # leandro
            [22, 14, 11],  # sebastian
            [8, 6, 4],     # agustin
            [16, 12, 8],   # tomas
            [11, 7, 6]     # oscar
                ]

for i in range(len(acciones)):
    suma = 0
    for j in range(len(acciones[i])):
        suma += acciones[i][j]
    print(f"{usuarios[i]} compró un total de {suma} acciones")

print("###########################################################")

for j in range(len(acciones[0])):
    total_empresa = 0
    for i in range(len(acciones)):
        total_empresa += acciones [i][j]
    promedio = total_empresa / len(acciones)
    print(f"Promedio de acciones para la empresa {empresas[j]}: {promedio}")
    
print("###########################################################")
tota_invertido = 0 
usuarios_con_total = [None] * len(usuarios)  
for i in range(len(acciones)):
    for j in range(len(acciones[i])):
        total = acciones[i][j] * precio_accion[j]
        tota_invertido += total
        usuarios_con_total[i] = usuarios[i], tota_invertido
ordenar = ordenar_array(usuarios_con_total, True)
print(ordenar)
print("###########################################################")


        