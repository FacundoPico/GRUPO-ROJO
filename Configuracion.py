import pygame
from Constantes import *
from Funciones import mostrar_texto

pygame.init()


fondo_config = pygame.image.load("Imagenes\Fondo_config.jpg")
fondo_config = pygame.transform.scale(fondo_config, VENTANA)

boton_subir_vol = pygame.image.load("Imagenes/subir_volumen.png")
boton_subir_vol = pygame.transform.scale(boton_subir_vol, TAMAÑO_BOTON_VOLUMEN)

boton_bajar_vol = pygame.image.load("Imagenes/bajar_volumen.png")
boton_bajar_vol = pygame.transform.scale(boton_bajar_vol, TAMAÑO_BOTON_VOLUMEN)

boton_silenciar = pygame.image.load("Imagenes/sirenciar_musica.png")
boton_silenciar = pygame.transform.scale(boton_silenciar, TAMAÑO_BOTON_VOLUMEN)

boton_volver = pygame.image.load("Imagenes/boton_volver.png")
boton_volver = pygame.transform.scale(boton_volver, TAMAÑO_BOTON_VOLUMEN)

fuente_boton = pygame.font.SysFont("Arial Narrow", 23)
fuente_volumen = pygame.font.SysFont("Arial Narrow", 50)

def mostrar_configuracion(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    '''
    Muestra la pantalla de configuración del juego, donde el jugador pueden subir, bajar o silenciarla música y regresar al menú principal.
    
    Parámetros:
    pantalla: Superficie de Pygame donde se dibujan los botones y texto.
    
    cola_eventos: Lista de eventos que la función utiliza para detectar clics del mouse o pulsaciones de teclas.
    
    datos_juego: Diccionario que contiene los datos del juego (información sobre el volumen de la música)
    
    Retorna un string que indica a cual ventana ir
    '''
    retorno = "configuraciones"
    
    pantalla.blit(fondo_config, (0, 0))
    
    boton_subir_vol_rect = pantalla.blit(boton_subir_vol, (720, 200))
    boton_bajar_vol_rect = pantalla.blit(boton_bajar_vol, (20, 200))
    boton_silenciar_rect = pantalla.blit(boton_silenciar, (720, 20))
    boton_volver_rect = pantalla.blit(boton_volver, (10, 10))
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_subir_vol_rect.collidepoint(evento.pos):
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 2
                CLICK_SONIDO.play()
            elif boton_bajar_vol_rect.collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 2
                CLICK_SONIDO.play()
            elif boton_silenciar_rect.collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica_prev"] = datos_juego["volumen_musica"]  
                    datos_juego["volumen_musica"] = 0
                else:
                    datos_juego["volumen_musica"] = datos_juego.get("volumen_musica_prev", 50)
                CLICK_SONIDO.play()
            elif boton_volver_rect.collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                CLICK_SONIDO.play()
            elif evento.key == pygame.K_DOWN:
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                CLICK_SONIDO.play()
    
    mostrar_texto(pantalla, f"{datos_juego['volumen_musica']} %", (350, 200), fuente_volumen, COLOR_BLANCO)

    return retorno
