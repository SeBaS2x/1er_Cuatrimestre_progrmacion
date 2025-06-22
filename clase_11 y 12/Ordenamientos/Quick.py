def swap( a: int, b: int) :
    return b, a

def particionar(array, low, high):
    pivote = array[high]#El pivote sera el ultimo elemento de la lista
    i = low - 1  # Índice del elemento más pequeño

    for j in range(low, high):

        if array[j] <= pivote:
            i += 1  # Incrementa el índice del elemento más pequeño
            array[i], array[j] = swap(array[i], array[j])

    array[i + 1], array[high] = swap(array[i + 1], array[high])# Mueve el pivote a su posición correcta
    return i + 1  # Retorna el índice del pivote
def quicksort(array, low, high):
    if low < high:
        pi = particionar(array, low, high)  # Índice del pivote

        quicksort(array, low, pi - 1)  # Ordena los elementos antes del pivote
        quicksort(array, pi + 1, high)  # Ordena los elementos después del pivote