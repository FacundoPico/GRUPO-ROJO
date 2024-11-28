import pygame
from Constantes import*
from Funciones import *
pygame.init()

fondoadi = pygame.image.load("Imagenes\pantallaadicional .png")
fondoadi = pygame.transform.scale(fondoadi, VENTANA)

boton_mas = pygame.image.load("Imagenes\subida.png")
boton_mas = pygame.transform.scale(boton_mas, TAMAÑO_BOTON_VOLUMEN)

boton_menos = pygame.image.load("Imagenes\Bajada.png")
boton_menos = pygame.transform.scale(boton_menos, TAMAÑO_BOTON_VOLUMEN)

boton_volver = pygame.image.load("Imagenes/boton_volver.png")
boton_volver = pygame.transform.scale(boton_volver, TAMAÑO_BOTON_VOLUMEN)

boton_tiempo_mas =pygame.image.load("Imagenes\subida.png")
boton_tiempo_mas =pygame.transform.scale(boton_mas, TAMAÑO_BOTON_VOLUMEN)

boton_tiempo_menos = pygame.image.load("Imagenes\Bajada.png")
boton_tiempo_menos = pygame.transform.scale(boton_tiempo_menos, TAMAÑO_BOTON_VOLUMEN)

boton_puntuacion_mas = pygame.image.load("Imagenes\subida.png")
boton_puntuacion_mas = pygame.transform.scale(boton_puntuacion_mas, TAMAÑO_BOTON_VOLUMEN)

boton_puntuacion_menos = pygame.image.load("Imagenes\Bajada.png")
boton_puntuacion_menos = pygame.transform.scale(boton_puntuacion_menos, TAMAÑO_BOTON_VOLUMEN)

fuente_boton = pygame.font.SysFont("Arial Narrow", 30)

def mostrar_adicional(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
     '''
     Muestra una pantalla adicional con botones interactivos para modificar las estadísticas del juego.

     Parámetros:
     - pantalla: Superficie de la ventana donde se dibujan los elementos.
     - cola_eventos: Lista de eventos de pygame.
     - datos_juego: Diccionario que contiene los datos actuales del juego.

     Retorna un string que indica la siguiente ventana.
     '''
     retorno = "adicional"
     pantalla.blit(fondoadi, (0, 0))

     boton_volver_rect = pantalla.blit(boton_volver, (10, 10))
     boton_tiempo_mas_rect = pantalla.blit(boton_tiempo_mas, (80, 220))
     boton_tiempo_menos_rect = pantalla.blit(boton_tiempo_menos, (215, 220))
     boton_puntuacion_mas_rect = pantalla.blit(boton_puntuacion_mas, (80, 320))
     boton_puntuacion_menos_rect = pantalla.blit(boton_puntuacion_menos, (215, 320))
     boton_puntuacionNEGATIVA_mas_rect = pantalla.blit(boton_puntuacion_mas, (80, 415))
     boton_puntuacionNEGATIVA_menos_rect = pantalla.blit(boton_puntuacion_menos, (215, 415))
     boton_vida_mas_rect = pantalla.blit(boton_mas, (80, 110))
     boton_vida_menos_rect = pantalla.blit(boton_menos, (215, 110))

     for evento in cola_eventos:
          if evento.type == pygame.QUIT:
               retorno = "salir"
          elif evento.type == pygame.MOUSEBUTTONDOWN:
               if boton_tiempo_mas_rect.collidepoint(evento.pos):
                    datos_juego["tiempo"] += 10
                    CLICK_SONIDO.play()
               elif boton_tiempo_menos_rect.collidepoint(evento.pos):
                    if datos_juego["tiempo"] > 0:
                         datos_juego["tiempo"] -= 10
                         CLICK_SONIDO.play()
               elif boton_vida_mas_rect.collidepoint(evento.pos):
                    datos_juego["vidas"] += 1
                    CLICK_SONIDO.play()
               elif boton_vida_menos_rect.collidepoint(evento.pos):
                    if datos_juego["vidas"] > 0:
                         datos_juego["vidas"] -= 1
                         CLICK_SONIDO.play()
               elif boton_puntuacion_mas_rect.collidepoint(evento.pos):
                    datos_juego["acierto"] += 10
                    CLICK_SONIDO.play()
               elif boton_puntuacion_menos_rect.collidepoint(evento.pos):
                    if datos_juego["acierto"] > 0:
                         datos_juego["acierto"] -= 10
                         CLICK_SONIDO.play()
               elif boton_puntuacionNEGATIVA_mas_rect.collidepoint(evento.pos):
                    datos_juego["fallo"] += 5
                    CLICK_SONIDO.play()
               elif boton_puntuacionNEGATIVA_menos_rect.collidepoint(evento.pos):
                    if datos_juego["fallo"] > 0:
                         datos_juego["fallo"] -= 5
                         CLICK_SONIDO.play()
               elif boton_volver_rect.collidepoint(evento.pos):
                    retorno = "menu"
                    CLICK_SONIDO.play()

     mostrar_texto(pantalla, "VIDAS", (150, 120), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, "TIEMPO", (145, 220), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, "ACIERTO", (140, 320), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, "FALLO", (150, 415), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, str(datos_juego["vidas"]), (175, 140), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, str(datos_juego["acierto"]), (160, 345), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, str(datos_juego["tiempo"]), (170, 245), fuente_boton, COLOR_BLANCO)
     mostrar_texto(pantalla, str(datos_juego["fallo"]), (170, 445), fuente_boton, COLOR_BLANCO)

     return retorno
