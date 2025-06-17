import pygame
def crear_boton(dimensiones, posicion, ventana, color_borde, imagen = None, fuente =None, texto = None ): #constuctor 
    boton = {} ### crea un diccionario para el boton
    boton["ventana"] = ventana# ventana donde se dibujara el boton
    boton["dimensiones"] = dimensiones# dimensiones del boton (ancho, alto)
    boton["posicion"] = posicion   # posicion del boton (x, y) 
    boton["color_borde"] = color_borde # color del borde del boton
    boton["presionado"] = False # estado del boton, si esta presionado o no
    if imagen != None:#
        img = pygame.image.load(imagen) ### carga la imagen del boton
        boton["superficie"] = pygame.transform.scale(img, boton["dimensiones"]) # escala la imagen al tamaño del boton
    else:
        fuente, tamaño = fuente #desempacamiento de tupla
        fuente = pygame.font.SysFont(fuente, tamaño)
        boton["superficie"] = fuente.render(texto, False, "red","orange")
        
    boton["rectangulo"] = boton["superficie"].get_rect()
    boton["rectangulo"].topleft = boton["posicion"] # establece la posicion del rectangulo del boton
    return boton

def dibujar_boton(boton): # dibuja el boton en la ventana
    boton["ventana"].blit(boton["superficie"], boton["posicion"])
    pygame.draw.rect(boton["ventana"], boton["color_borde"], boton["rectangulo"], 2)
    
def dibujar_lista_botones(lista_botones):
    for boton in lista_botones:
        dibujar_boton(boton)  # dibuja cada boton en la lista de botones