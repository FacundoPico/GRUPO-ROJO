import pygame
from Constantes import *
from Funciones import mostrar_texto
from Rankings import guardar_ranking  

pygame.init()


fuente = pygame.font.SysFont("Arial Narrow", 40)
cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
cuadro['superficie'].fill(COLOR_VIOLETA)

game_over = pygame.image.load("Imagenes\gameover.png")
fondo_termino = pygame.image.load("Imagenes\Fondo_terminado.jpg")
fondo_termino = pygame.transform.scale(fondo_termino,(VENTANA))

nombre = ""
bandera_mayuscula = False

def verificar_texto(caracter:str) -> bool:
    '''
    Verifica si un carácter es alfanumérico o tiene un espacio en blanco.
    
    Parámetros:
    - caracter: Carácter a verificar.

    Retorna un booleano, devuelve True si el carácter es alfanumérico o tiene un espacio, devuelve False en caso contrario.
    '''

    nombre = caracter.isalnum() or caracter == " "
    
    return nombre


def mostrar_fin_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    '''
    Muestra la pantalla de fin de juego, permitiendo al jugador ingresar su nombre y guardar el ranking.

    Parámetros:
    - pantalla: Superficie de Pygame donde se dibujan los elementos del fin de juego.
    - cola_eventos: Lista de eventos para detectar las pulsaciones de teclas y otras interacciones.
    - datos_juego: Diccionario que contiene los datos actuales del juego (puntuación y vidas restantes).

    Retorna un string que indica el siguiente estado del juego.
    '''

    global nombre
    global bandera_mayuscula
    retorno = "terminado"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.KEYDOWN:
            letra_presionada = pygame.key.name(evento.key)
            
            if evento.key == pygame.K_CAPSLOCK:
                bandera_mayuscula = True
            
            shift_presionado = pygame.key.get_mods() & pygame.KMOD_SHIFT
            if shift_presionado:
                bandera_mayuscula = True
            else:
                if pygame.key.get_mods() & pygame.KMOD_CAPS == 0:
                    bandera_mayuscula = False
            
            if len(letra_presionada) == 1:  
                if verificar_texto(letra_presionada):
                    if bandera_mayuscula:
                        nombre += letra_presionada.upper()
                    else:
                        nombre += letra_presionada.lower()
            
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1]
                cuadro["superficie"].fill(COLOR_VIOLETA)
            
            if letra_presionada == "space":
                nombre += " "
            
            if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                guardar_ranking(nombre, datos_juego["puntuacion"])
                
                datos_juego["vidas"] = 3
                datos_juego["puntuacion"] = 0
                nombre = ""
                
                retorno = "menu"
    
    pantalla.blit(fondo_termino, (0, 0))
    pantalla.blit(game_over,(140,-25))
    
    cuadro["superficie"].fill(COLOR_VIOLETA)
    
    
    if pygame.time.get_ticks() % 1000 < 500:
        texto_mostrado = nombre + "|"
    else:
        texto_mostrado = nombre
    
    mostrar_texto(cuadro["superficie"], texto_mostrado, (10, 0), fuente, COLOR_BLANCO)
    
    cuadro["rectangulo"] = pantalla.blit(cuadro["superficie"], (270, 260))
    mostrar_texto(pantalla, f"Usted obtuvo: {datos_juego['puntuacion']} puntos", (250, 200), fuente, COLOR_BLANCO)

    return retorno

