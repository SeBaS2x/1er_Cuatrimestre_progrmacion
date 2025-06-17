import pygame 
from boton import *
import random ### importa la libreria random para generar numeros aleatorios
ANCHO_VENTANA = 800
ALTO_VENTANA = 500
pygame.init()### inicia pygame 

VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))### crea la ventana
pygame.display.set_caption("Mi Primer Juego")### establece el titulo de la ventana
icono = pygame.image.load("utn_icono.jpg")### carga el icono
pygame.display.set_icon(icono)### establece el icono de la ventana




bandera = True### variable para controlar el bucle
while bandera == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:### si se cierra la ventana
            bandera = False
    
    
    pygame.display.update()### actualiza la ventana


pygame.quit()### finaliza pygame