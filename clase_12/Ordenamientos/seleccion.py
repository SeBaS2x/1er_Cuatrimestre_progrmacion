vector = [4,6,1,9,3,2,8,5,7,10]
largo = len(vector)

for i in range(largo-1):
    minimo_indice = i
    # Encontrar el índice del valor mínimo en el subvector no ordenado
    for j in range(i + 1, largo):
        if vector[j] < vector[minimo_indice]:
            minimo_indice = j
    if minimo_indice != i:
        aux = vector[i]
        vector[i]= vector[minimo_indice]
        vector[minimo_indice] = aux
print(vector)