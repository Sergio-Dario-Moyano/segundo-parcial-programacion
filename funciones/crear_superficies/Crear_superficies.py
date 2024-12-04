import pygame
from constantes.Constantes import *
from funciones.funciones_comunes.Funciones import *

def crea_botones(cantidad_botones: int, tamaño: tuple, color: tuple) -> list:
    lista_botones = []
    for i in range(cantidad_botones):
        boton = {}
        boton["superficie"] = pygame.Surface(tamaño)
        boton["rectangulo"] = boton["superficie"].get_rect()
        boton["superficie"].fill(color)
        lista_botones.append(boton)
    return lista_botones

def crea_cuadros(cantidad_cuadros: int, imagen: str, tamaño: tuple) -> list:
    lista_cuadros = []
    for i in range(cantidad_cuadros):
        cuadro = {}
        cuadro["superficie"] = pygame.image.load(imagen)
        cuadro["superficie"] = pygame.transform.scale(cuadro["superficie"], tamaño)
        cuadro["rectangulo"] = cuadro["superficie"].get_rect()
        lista_cuadros.append(cuadro)
    return lista_cuadros

#Dibujar preguntas
def dibujar_preguntas(pantalla:pygame.Surface, cuadro_pregunta:dict, pregunta_actual:dict) -> None:
   
   mostrar_texto(cuadro_pregunta["superficie"],f"{pregunta_actual["pregunta"]}", (20,20),FUENTE_22,COLOR_BLANCO)
   cuadro_pregunta["rectangulo"] = pantalla.blit(cuadro_pregunta["superficie"],(20,80))
   pygame.draw.rect(pantalla,COLOR_NEGRO,cuadro_pregunta["rectangulo"],2)

#Dibujar respuestas
def dibujar_respuestas(pantalla:pygame.Surface, lista_respuestas:dict, pregunta_actual:dict) -> dict:
    
    posiciones_respuestas = [(62, 245), (62, 315), (62, 385), (62, 455)]

    for i in range(len(lista_respuestas)):
        mostrar_texto(lista_respuestas[i]["superficie"],f"{pregunta_actual[f"respuesta_{i+1}"]}",(20,20),FUENTE_22,COLOR_BLANCO)
        lista_respuestas[i]["rectangulo"] = pantalla.blit(lista_respuestas[i]["superficie"],posiciones_respuestas[i])
        pygame.draw.rect(pantalla,COLOR_BLANCO,lista_respuestas[i]["rectangulo"],2)