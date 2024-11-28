import pygame
from Constantes import *
from Preguntas import *
from Funciones import *
from adicional import *

pygame.init()

fondo = pygame.image.load("Imagenes\Fondo.jpg")
fondo = pygame.transform.scale(fondo, VENTANA)

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.image.load("Imagenes\Fondo_pregunta.png")
cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"], TAMAÑO_IMAGEN_PREG)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()


bandera_comodin_usado_pasar = False
bandera_comodin_visible_pasar = True
imagen_comodin_pasar = pygame.image.load("Imagenes\Pasar.png")
imagen_comodin_pasar = pygame.transform.scale(imagen_comodin_pasar, TAMAÑO_IMAGEN_COMODIN)

imagen_comodin_x2 = pygame.image.load("Imagenes\X2.png")
imagen_comodin_x2 = pygame.transform.scale(imagen_comodin_x2, TAMAÑO_IMAGEN_COMODIN)


cartas_respuestas = []
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

fuente_prgunta = pygame.font.SysFont("Arial Narrow", 30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow", 30)
fuente_texto = pygame.font.SysFont("Arial Narrow", 25)

mezclar_lista(lista_preguntas)
indice = 0
respuestas_correctas_consecutivas = 0
bandera_respuesta = False

clock = pygame.time.Clock()
evento_tiempo_1s = pygame.USEREVENT
pygame.time.set_timer(evento_tiempo_1s, 1000)


bandera_comodin_x2__usado = False
bandera_comodin_x2_visible = True

def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    '''
    Muestra la pantalla de juego, maneja las interacciones del usuario con las respuestas, el uso de comodines, el temporizador y la puntuación.
    Parámetros:
    - pantalla: Superficie de Pygame donde se dibujan los elementos del juego (preguntas, respuestas, comodines, etc.).
    - cola_eventos: Lista de eventos para manejar interacciones del usuario.
    - datos_juego: Diccionario que almacena el estado del juego.

    Retorna un string que indica la siguiente ventana a mostrar.
    '''

    global indice
    global bandera_respuesta
    global respuestas_correctas_consecutivas
    global bandera_comodin_x2__usado
    global bandera_comodin_x2_visible
    global bandera_comodin_usado_pasar
    global bandera_comodin_visible_pasar
    
    retorno = "juego"
    
    
    
    for carta in cartas_respuestas:
        carta["superficie"].fill(COLOR_AZUL)
        
    if bandera_respuesta:
        cuadro_pregunta["superficie"] = pygame.image.load("Imagenes\Fondo_pregunta.png")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"], TAMAÑO_IMAGEN_PREG)
        pygame.time.delay(500)
        bandera_respuesta = False
        
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == evento_tiempo_1s:
            if datos_juego["tiempo"] > 0:
                datos_juego["tiempo"] -= 1
            else:
                datos_juego["tiempo"] = 60
                retorno = "terminado"
        
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            rect_comodin_x2 = imagen_comodin_x2.get_rect()
            rect_comodin_x2.x = 10
            rect_comodin_x2.y = 25
            
            rect_comodin_pasar = imagen_comodin_pasar.get_rect()
            rect_comodin_pasar.x = 50
            rect_comodin_pasar.y = 25 
            
            if bandera_comodin_x2__usado == False and rect_comodin_x2.collidepoint(evento.pos):
                bandera_comodin_x2__usado = True
                bandera_comodin_x2_visible = False
        

            if bandera_comodin_usado_pasar ==False and rect_comodin_pasar.collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    bandera_respuesta = True
                    bandera_comodin_usado_pasar = True
                    bandera_comodin_visible_pasar = False
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    if verificar_respuesta(datos_juego, pregunta_actual, respuesta_usuario):
                        respuestas_correctas_consecutivas += 1
                        if respuestas_correctas_consecutivas == 5:
                            if datos_juego["vidas"] < 3:
                                datos_juego["vidas"] += 1
                            datos_juego["tiempo"] += 10
                            respuestas_correctas_consecutivas = 0
                        
                        if bandera_comodin_x2__usado == True:
                            datos_juego["puntuacion"] += (datos_juego["acierto"] * 2)
                            bandera_comodin_x2__usado = False
                        else:
                            datos_juego["puntuacion"] += datos_juego["acierto"]


                        
                        ACIERTO_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_VERDE)
                    else:
                        ERROR_SONIDO.play()
                        if datos_juego["puntuacion"] > 0 :                   
                            datos_juego["puntuacion"] -= datos_juego["fallo"]
                        cartas_respuestas[i]['superficie'].fill(COLOR_ROJO)

                    
                    bandera_respuesta = True
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1


    if datos_juego["vidas"] == 0:
        datos_juego["tiempo"] 
        retorno = "terminado"
    
    if retorno == "terminado":
        bandera_comodin_x2__usado = False
        bandera_comodin_x2_visible = True
        bandera_comodin_usado_pasar = False
        bandera_comodin_visible_pasar = True
    
    mostrar_texto(cuadro_pregunta["superficie"], f'{pregunta_actual["pregunta"]}', TAMAÑO_PREGUNTA, fuente_prgunta, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), fuente_respuesta, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), fuente_respuesta, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), fuente_respuesta, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_4']}", (20, 20), fuente_respuesta, COLOR_BLANCO)
    
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(cuadro_pregunta["superficie"], (58, 74))
    
    if bandera_comodin_x2_visible == True:
        pantalla.blit(imagen_comodin_x2, (10, 25))
    
    if bandera_comodin_visible_pasar == True:
        pantalla.blit(imagen_comodin_pasar, (70,25)) 
    
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'], (170, 325))
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'], (170, 450))
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'], (465, 325))
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'], (465, 450))
    
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego["puntuacion"]}", (10, 10), fuente_texto, COLOR_BLANCO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['vidas']}", (620, 45), fuente_texto, COLOR_BLANCO) 
    mostrar_texto(pantalla, f"TIEMPO RESTANTE: {datos_juego['tiempo']}", (560, 20), fuente_texto, COLOR_ROJO)
    
    return retorno
