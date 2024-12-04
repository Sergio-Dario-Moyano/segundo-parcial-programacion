import pygame
from constantes.Constantes import *
from funciones.funciones_comunes.Funciones import *
from funciones.crear_superficies.Crear_superficies import *

pygame.init()

fondo = pygame.image.load("imagenes/configuracion.jpg")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_suma = crea_cuadros(1, "imagenes/vol_max.png", TAMAÑO_BOTON_VOLUMEN)[0]
boton_resta = crea_cuadros(1, "imagenes/vol_max.png", TAMAÑO_BOTON_VOLUMEN)[0]
boton_mute = crea_cuadros(1, "imagenes/vol_mute.png", TAMAÑO_BOTON_VOLUMEN)[0]
boton_volver = crea_cuadros(1, "imagenes/volver.png", TAMAÑO_BOTON_VOLVER)[0]

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                else:
                    ERROR_SONIDO.play()
                print("SUMA VOLUMEN")
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                else:
                    ERROR_SONIDO.play(maxtime=1000)
                print("RESTA VOLUMEN")
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
            elif boton_mute["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    # Guardar el volumen actual antes de mutear
                    datos_juego["volumen_musica_guardado"] = datos_juego["volumen_musica"]
                    datos_juego["volumen_musica"] = 0  # Mutear
                    print("MUTE ACTIVADO")
                else:
                    # Restaurar el volumen guardado
                    datos_juego["volumen_musica"] = datos_juego["volumen_musica_guardado"]
                    print("MUTE DESACTIVADO")
                
    porcentaje_coma = datos_juego["volumen_musica"] / 100
    pygame.mixer.music.set_volume(porcentaje_coma)

    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo, (0, 0))

    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,280))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(320,280))    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute["superficie"], (20, 130))
    
    mostrar_texto(boton_suma["superficie"],"VOL+",(5,40),FUENTE_20,COLOR_BLANCO)
    mostrar_texto(boton_resta["superficie"],"VOL-",(5,40),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_22,COLOR_BLANCO)
    mostrar_texto(boton_mute["superficie"], "MUTE", (10, 10), FUENTE_20, COLOR_BLANCO)  # Mostrar texto para mute
    mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(150,280),FUENTE_H_55,COLOR_MARRON)
    
    return retorno