def crear_vector(valor_inicial, cantidad) -> list:
    vector = [valor_inicial] * cantidad
    return vector

def cargar_vector(vector:list, mensaje):
    for i in range(len(vector)):
        vector[i] = int(input(mensaje)) 
    
def mostrar_vector(vector):
    for i in range(len(vector)):
        print(vector[i])
        
######MAIN#############
def buscar_minimo(vector:list):
    for i in range(len(vector)):
        if i == 0 or vector[i]<minimo:
            minimo = vector[i]
    return minimo

crear =crear_vector(0,5)
cargar_vector(crear, "ingresar numero del vector ")
mostrar_vector(crear)