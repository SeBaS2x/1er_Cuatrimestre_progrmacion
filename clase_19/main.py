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

# gatito = pygame.image.load("gatito.jpeg")### carga la imagen del gatito
# VENTANA.fill("GREEN")### rellena la ventana con un colorpy
# VENTANA.blit(gatito, (50,50))### dibuja el gatito en la ventana en la posicion (50,50)
pygame.mixer.init()
pygame.mixer.music.load("ok.mp3")
boton_gatito = crear_boton(dimensiones=(100,100),
                           posicion=(50, 50), 
                           ventana=VENTANA,
                           imagen="gatito.jpeg",
                           color_borde="green")### crea el boton con la imagen del gatito
boton_texto = crear_boton(dimensiones=(100, 250),
                        color_borde="orange",
                        posicion=(50,250),
                        fuente=("consola",20),
                        texto= "pushme",
                        ventana=VENTANA,)
lista_botones=[boton_gatito, boton_texto]

fuente_texto = pygame.font.SysFont("Arial", 20)### establece la fuente del texto del boton


bandera = True### variable para controlar el bucle
while bandera == True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:### si se cierra la ventana
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN: ### si se presiona un boton del mouse
            if boton_gatito["rectangulo"].collidepoint(evento.pos):
                boton_gatito["presionado"] = True### si se presiona el boton, cambia el estado a presionado
            elif boton_texto["rectangulo"].collidepoint(evento.pos):
                
                pygame.mixer.music.play()### reproduce un sonido al presionar el boton de texto
                
    dibujar_lista_botones(lista_botones)### dibuja los botones en la ventana
    
    if boton_gatito["presionado"] == True:
        
        texto = fuente_texto.render("Miauu", False,"blue","pink")
        y = random.randint(50, 500)
        x = random.randint(50, 700)
        VENTANA.blit(texto, (x,y))
        boton_gatito["presionado"] = False### si el boton esta presionado, dibuja el texto en una posicion aleatoria
    
    
    pygame.display.update()### actualiza la ventana


pygame.quit()### finaliza pygame