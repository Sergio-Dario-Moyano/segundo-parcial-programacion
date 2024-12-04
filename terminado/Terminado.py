import pygame 
from constantes.Constantes import *
from funciones.funciones_comunes.Funciones import *
from funciones.maneja_archivos.handler_files import *
from datetime import datetime

pygame.init()
fondo = pygame.image.load("imagenes/voldi.png")
fondo = pygame.transform.scale(fondo,VENTANA)

cuadro_texto = {}
cuadro_texto["superficie"] = pygame.image.load("imagenes/boton_inicio.png")
cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],CUADRO_TEXTO)
cuadro_texto["rectangulo"] = cuadro_texto["superficie"].get_rect()
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif evento.type == pygame.KEYDOWN:
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            print(tecla_presionada)
            
            if tecla_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1]
                cuadro_texto["superficie"] = pygame.image.load("imagenes/boton_inicio.png")
                cuadro_texto["superficie"] = pygame.transform.scale(cuadro_texto["superficie"],CUADRO_TEXTO)
            
            if tecla_presionada == "space" and len(nombre) < 10:
                nombre += " "
            
            if len(tecla_presionada) == 1:
              if len(nombre) < 10:
                if bloc_mayus != 0:
                    nombre += tecla_presionada.upper()
                else:
                    nombre += tecla_presionada
                    
            # Guardar nombre con Enter
            elif tecla_presionada == "return" and len(nombre) >= 3:

                fecha_actual = datetime.now().strftime("%d/%m/%y")
                datos = {"nombre": nombre, "fecha": fecha_actual, "puntos": datos_juego["puntuacion"]}
                cargar_json(datos)
                print("Nombre guardado exitosamente en el ranking.")
                retorno = "menu"
    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo, (0, 0))
    cuadro_texto["rectangulo"] = pantalla.blit(cuadro_texto["superficie"],(80,200))
    mostrar_texto(cuadro_texto["superficie"],nombre,(10,10),FUENTE_32,COLOR_NEGRO)
    mostrar_texto(pantalla,f"USTED OBTUVO {datos_juego["puntuacion"]} PUNTOS",(20,30),FUENTE_27,COLOR_BLANCO)
    mostrar_texto(pantalla,"INGRESE SU NOMBRE:",(50,150),FUENTE_27,COLOR_BLANCO)
    mostrar_texto(pantalla,"GAME OVER",(70,440),FUENTE_H_55,COLOR_MARRON)
    
    return retorno