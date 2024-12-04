import pygame
from constantes.Constantes import *
from funciones.funciones_comunes.Funciones import *
from funciones.maneja_archivos.handler_files import *

pygame.init()
fondo = pygame.image.load("imagenes/puntajes.png")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_volver = {}
boton_volver["superficie"] = pygame.image.load("imagenes/volver.png") 
boton_volver["superficie"] = pygame.transform.scale(boton_volver["superficie"],TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "puntuaciones"
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.blit(fondo,(0,0))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    
    lista_ranking = leer_json("files/partidas.json")
    
    #Creo una superficie para mostrar el error (si lo hay)
    cuadro_error = {}
    cuadro_error["superficie"] = pygame.Surface(VENTANA)
    cuadro_error["rectangulo"] = cuadro_error["superficie"].get_rect()

    if len(lista_ranking) == 0:
        texto_error = "¡¡¡ERROR!!! Aún no hay datos cargados."
        cuadro_error["superficie"] = pygame.image.load("imagenes/fondo_harry_error.jpg")
        cuadro_error["superficie"] = pygame.transform.scale(cuadro_error["superficie"], VENTANA)
        mostrar_texto(cuadro_error["superficie"],texto_error,(50,50),FUENTE_40,COLOR_ROJO)
        cuadro_error["rectangulo"] = pantalla.blit(cuadro_error["superficie"],(0,50))
    else:
        #Si el archivo .json tiene algo, lo ordeno por ranking antes de mostrarlo.
        lista = ordenar_matriz_puntaje(lista_ranking)
        
        #mostrar_texto(pantalla,f"ACA DEBEN MOSTRAR EL TOP 10",(20,200),FUENTE_32,COLOR_NEGRO)
        top = 100  # Posición inicial en Y para la lista
        for jugador in lista:
            mostrar_texto(pantalla, str(jugador["fecha"]), (300, top), FUENTE_22, COLOR_AMARILLO)
            mostrar_texto(pantalla, jugador["nombre"], (20, top), FUENTE_22, COLOR_AMARILLO)
            mostrar_texto(pantalla, str(jugador["puntos"]), (220, top), FUENTE_22, COLOR_AMARILLO)
            top += 40  # Incrementar la posición vertical para la siguiente fila

    return retorno

