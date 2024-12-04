import random
from constantes.Constantes import *

#comodin--------------------
def comodin_elimina_opciones(lista_respuestas: list, pregunta_actual:list):
    # defino Respuesta correcta--------------------
    respuesta_correcta = int(pregunta_actual["respuesta_correcta"]) - 1
    #Cargo Respuestas incorrectas en una lista
    respuestas_incorrectas = cargo_respuestas_icorretas(respuesta_correcta, lista_respuestas)
    #Pinto 2 de las 3 respuestas incorrectas en rojo
    marco_respuestas_incorrectas(lista_respuestas, respuestas_incorrectas)

def cargo_respuestas_icorretas(respuesta_correcta: list, lista_respuestas: list):
    # Crear una lista respuestas incorrectas
    respuestas_incorrectas = []
    for i in range(len(lista_respuestas)):
        if i != respuesta_correcta:
            respuestas_incorrectas.append(i)
    return respuestas_incorrectas

def marco_respuestas_incorrectas(lista_respuestas:list, respuestas_incorrectas: list):
    # Seleccionar aleatoriamente dos respuestas incorrectas para marcar en rojo
    respuestas_a_marcar = random.sample(respuestas_incorrectas, 2)

    for i in range(len(lista_respuestas)):
        if i in respuestas_a_marcar:
            # Marcar las respuestas seleccionadas con rojo
            lista_respuestas[i]["superficie"] = pygame.image.load("imagenes/incorrecta.png")
            lista_respuestas[i]["superficie"] = pygame.transform.scale(lista_respuestas[i]["superficie"], TAMAÑO_RESPUESTA)
            lista_respuestas[i]["rectangulo"] = None

#---COMODIN  doble punto      
def comodin_duplico_puntos(respuesta_seleccionada, pregunta_actual,datos_juego):
     
    if respuesta_seleccionada == int(pregunta_actual["respuesta_correcta"]):
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO * 2
    