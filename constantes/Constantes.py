import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_AMARILLO = (239,255,0)
COLOR_VERDE_OSCURO = "#0B9827"
COLOR_MARRON = "#edb22c"
ANCHO = 400
ALTO = 730
VENTANA = (ANCHO,ALTO)
FPS = 60

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (300,60)
TAMAÑO_COMODIN = (90,60)

CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
TAMAÑO_BOTON_COMODIN = (80,80)

FUENTE_H_60 = pygame.font.Font("fuentes/HARRYP.ttf", 80)
FUENTE_H_55 = pygame.font.Font("fuentes/HARRYP.ttf", 55)
FUENTE_H_30 = pygame.font.Font("fuentes/HARRYP.ttf", 30)


FUENTE_18 = pygame.font.SysFont("Arial",18)
FUENTE_20 = pygame.font.SysFont("Arial",20)
FUENTE_22 = pygame.font.SysFont("Arial",22)
FUENTE_25 = pygame.font.SysFont("Arial",25)
FUENTE_27 = pygame.font.SysFont("Arial",27)
FUENTE_30 = pygame.font.SysFont("Times",30)
FUENTE_32 = pygame.font.SysFont("Arial",32)
FUENTE_40 = pygame.font.SysFont("Arial",40)
FUENTE_50 = pygame.font.SysFont("Arial",50)
#------- Areal  Black
FUENTE_22_B = pygame.font.SysFont("Arial Black",22)

CLICK_SONIDO = pygame.mixer.Sound("musica/click.mp3")
ACIERTO_SONIDO = pygame.mixer.Sound("musica/click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("musica/error.mp3")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

BOTON_JUGAR = 0
BOTON_AJUSTES = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3