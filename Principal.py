import pygame
from Constantes import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *
from adicional import *


pygame.init()
pygame.mixer.init()
pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("Imagenes\icono.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion": 0,
                "vidas": CANTIDAD_VIDAS,
                "nombre": "",
                "volumen_musica": 100,
                "tiempo": 60,
                "acierto": 100,
                "fallo": 25
                }
ventana_actual = "menu"
bandera_musica_juego = False
bandera_musica_menu = False


while corriendo:
    reloj.tick(FPS)
    
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        if bandera_musica_menu == False:
            pygame.mixer.music.load("musicamenu.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
            bandera_musica_menu = True
        ventana_actual = mostrar_menu(pantalla, cola_eventos)
        
    elif ventana_actual == "juego":
        if datos_juego["vidas"] <= 0:
            ventana_actual = "terminado"
        else:
            if bandera_musica_juego == False:
                porcentaje_volumen = datos_juego["volumen_musica"] / 100
                pygame.mixer.music.load("musica.mp3")
                pygame.mixer.music.set_volume(porcentaje_volumen)
                pygame.mixer.music.play(-1)
                bandera_musica_juego = True
            ventana_actual = mostrar_juego(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "configuraciones":
        ventana_actual = mostrar_configuracion(pantalla, cola_eventos, datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla, cola_eventos)
    elif ventana_actual == "terminado":
        if bandera_musica_juego == True:
            pygame.mixer.music.stop()
            bandera_musica_juego = False
        if bandera_musica_menu == True:
            pygame.mixer.music.stop()
            bandera_musica_menu = False
        ventana_actual = mostrar_fin_juego(pantalla, cola_eventos, datos_juego)

    elif ventana_actual == "adicional":
        ventana_actual = mostrar_adicional(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "salir":
        corriendo = False
    
    pygame.display.flip()

pygame.quit()
