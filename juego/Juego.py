import pygame 
import random
from funciones.funciones_comunes.Funciones import *
from preguntas.Preguntas import *
from funciones.comodines.Comodines import *
from funciones.crear_superficies.Crear_superficies import *
from funciones.funciones_complementarias.Funciones_complementarias import *

pygame.init()

evento_tick = pygame.USEREVENT + 1
pygame.time.set_timer(evento_tick, 1000)  # Dispara cada segundo
tiempo_restante = 50

#Cargo imagen Fondo
fondo = pygame.image.load("imagenes/juego_h.png")
fondo = pygame.transform.scale(fondo,VENTANA)
# Crear cuadro de pregunta
cuadro_pregunta = crea_cuadros(1, "imagenes/marco_pregunta.png", TAMAÑO_PREGUNTA)[0]

# Crear botones con las propiedades necesarias
boton_comodin = crea_cuadros(1, "imagenes/scuiduch.png", TAMAÑO_COMODIN)[0]
boton_comodin["usado"] = False

boton_puntos = crea_cuadros(1, "imagenes/scuiduch.png", TAMAÑO_COMODIN)[0]
boton_puntos["usado"] = False
boton_puntos_activo = False

boton_chance = crea_cuadros(1, "imagenes/scuiduch.png", TAMAÑO_COMODIN)[0]
boton_chance["usado"] = False
doble_chance_activo = False

boton_pasar = crea_cuadros(1, "imagenes/scuiduch.png", TAMAÑO_COMODIN)[0]
boton_pasar["usado"] = False

lista_respuestas = []
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    #-----Agrego imagen fondo respuestas
    cuadro_respuesta["superficie"] = pygame.image.load("imagenes/respuesta.png")  # Carga la imagen del botón
    cuadro_respuesta["superficie"] = pygame.transform.scale(cuadro_respuesta["superficie"], TAMAÑO_RESPUESTA)

    #cuadro_respuesta["superficie"].fill(COLOR_AZUL)
    lista_respuestas.append(cuadro_respuesta)
    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables
puntos_acumulados = 0

random.shuffle(lista_preguntas)
                
def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice
    global bandera_respuesta
    global boton_puntos_activo
    global doble_chance_activo
    global tiempo_restante
    global puntos_acumulados
    
    retorno = "juego"
    
    if bandera_respuesta:
        pygame.time.delay(250)
        #Limpio la superficie
        cuadro_pregunta["superficie"] = pygame.image.load("imagenes/marco_pregunta.png")
        cuadro_pregunta["superficie"] = pygame.transform.scale(cuadro_pregunta["superficie"],TAMAÑO_PREGUNTA)
        for i in range(len(lista_respuestas)):
            #-----Agrego imagen fondo respuestas
            lista_respuestas[i]["superficie"] = pygame.image.load("imagenes/respuesta.png")
            lista_respuestas[i]["superficie"] = pygame.transform.scale(lista_respuestas[i]["superficie"], TAMAÑO_RESPUESTA)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        #controlo si termina el timepo
        elif evento.type == evento_tick:
            if tiempo_restante > 0:
                tiempo_restante -= 1
            else:
                print("¡Tiempo agotado!")
                retorno = "terminado"
        #si termina termina el juego

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            #Funcion comodin
            if boton_comodin["usado"] == False and boton_comodin["rectangulo"].collidepoint(evento.pos): 
                print("Comodín activado")
                boton_comodin["superficie"] = pygame.image.load("imagenes/comodin_usado.png")
                comodin_elimina_opciones(lista_respuestas, pregunta_actual)
                boton_comodin["usado"] = True

            if boton_puntos["usado"] == False and boton_puntos["rectangulo"].collidepoint(evento.pos):
                print("Doble puntos")
                boton_puntos["superficie"] = pygame.image.load("imagenes/comodin_usado.png")
                boton_puntos_activo = True
                boton_puntos["usado"] = True

            if boton_chance["usado"] == False and boton_chance["rectangulo"].collidepoint(evento.pos): 
                print("Doble Chance activado")
                boton_chance["superficie"] = pygame.image.load("imagenes/comodin_usado.png")
                doble_chance_activo = True
                boton_chance["usado"] = True 
                
            if boton_pasar["usado"] == False and boton_pasar["rectangulo"].collidepoint(evento.pos): 
                print("Pasar")
                boton_pasar["superficie"] = pygame.image.load("imagenes/comodin_usado.png")
                indice += 1
                if indice == len(lista_preguntas):
                    random.shuffle(lista_preguntas)
                    indice = 0
                # Desactiva el botón 
                boton_pasar["usado"] = True
                bandera_respuesta = True

                #desactivo comodin
                boton_pasar["usado"] = True 

            for i in range(len(lista_respuestas)):
                
                if lista_respuestas[i]["rectangulo"] and lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    
                    if respuesta_seleccionada == int(pregunta_actual["respuesta_correcta"]):

                        res = respuesta_correcta(datos_juego, lista_respuestas, i, boton_puntos_activo)
                        indice = cambiar_pregunta(indice, lista_preguntas)
                        bandera_respuesta = True
                        print(res)
                        if res:
                            tiempo_restante += 10
                    else:
                        if doble_chance_activo:
                            pintar = False
                            pintar_respuesta(lista_respuestas, pintar, i)
                            doble_chance_activo = False  # Desactiva el comodín tras usarlo
                        else:
                            retorno = respuesta_incorrecta(datos_juego, lista_respuestas, i, retorno)
                            indice = cambiar_pregunta(indice, lista_preguntas)
                            bandera_respuesta = True
                    boton_puntos_activo = False #Una vez usado el comodin, se deshabilita (haya acertado o no).
                           
    # pantalla.fill(COLOR_VIOLETA)
    pantalla.blit(fondo,(0,0))

    # Dibujando las preguntas
    dibujar_preguntas(pantalla, cuadro_pregunta, pregunta_actual)

    # Dibujando las posibles respuestas
    dibujar_respuestas(pantalla, lista_respuestas, pregunta_actual)
    
    #muestro tiempooooo
    mostrar_texto(pantalla, f"Tiempo: {tiempo_restante}", (290, 10), FUENTE_20, COLOR_ROJO)

    mostrar_texto(boton_comodin["superficie"],"COMODIN",(5,10),FUENTE_18,COLOR_BLANCO) # Comodin    
    mostrar_texto(boton_puntos["superficie"],"PUNTOS x2",(5,10),FUENTE_18,COLOR_BLANCO) # doble pts
    mostrar_texto(boton_chance["superficie"],"CHANCE",(5,10),FUENTE_18,COLOR_BLANCO) # doble pts
    mostrar_texto(boton_pasar["superficie"],"PASO",(10,15),FUENTE_18,COLOR_BLANCO) # doble pts

    boton_comodin["rectangulo"] = pantalla.blit(boton_comodin["superficie"],(5,529)) # Comodin
    boton_puntos["rectangulo"] = pantalla.blit(boton_puntos["superficie"],(105,529)) # Comodin Doble ptos
    boton_chance["rectangulo"] = pantalla.blit(boton_chance["superficie"],(205,529)) # Comodin Doble ptos
    boton_pasar["rectangulo"] = pantalla.blit(boton_pasar["superficie"],(305,529)) # Comodin Doble ptos

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_25,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['cantidad_vidas']}",(10,40),FUENTE_25,COLOR_NEGRO)
    
    return retorno