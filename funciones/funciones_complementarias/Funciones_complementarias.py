from constantes.Constantes import *
import random

# Modifica el indice de preguntas para cambiarla si es necesario
def cambiar_pregunta(indice, lista_preguntas):
  indice += 1                      
  if indice == len(lista_preguntas):
    indice = 0
    random.shuffle(lista_preguntas)
  return indice


# Si la respuesta es correcta, pinta de color verde la respuesta y suma puntos
acumula_puntos = 0 #Variable que suma las respuestas correctas
def respuesta_correcta(datos_juego, lista_respuestas, i, boton_puntos_activo):
  global acumula_puntos
  
  ACIERTO_SONIDO.play()
  print("RESPUESTA CORRECTA")
  acumula_puntos += 1
  pintar = True
  pintar_respuesta(lista_respuestas, pintar, i)
  sumar_puntos(datos_juego, boton_puntos_activo)

  if acumula_puntos == 5:
    sumar_vida(datos_juego)
    acumula_puntos = 0
    return True
  else:
    return False

# Si la respuesta fue incorrecta, pinta de color rojo la respuesta y verifica si hay vidas para restar si no, finalia el juego.
def respuesta_incorrecta(datos_juego, lista_respuestas, i, retorno):
  ERROR_SONIDO.play(maxtime=1000)
  pintar = False
  pintar_respuesta(lista_respuestas, pintar, i)
  retorno = verificar_vidas(datos_juego, retorno)
  return retorno

# Pinta una respuesta
def pintar_respuesta(lista_respuestas, pintar, i):
  if pintar:
    lista_respuestas[i]["superficie"].fill(COLOR_VERDE_OSCURO)
  else:
    lista_respuestas[i]["superficie"].fill(COLOR_ROJO)

# Suma puntos (Si el comodin sumar dobre está activado, duplica los puntos a sumar)
def sumar_puntos(datos_juego:dict, boton_puntos_activo):
  if boton_puntos_activo:  
    datos_juego["puntuacion"] += PUNTUACION_ACIERTO * 2
  else:  # Si no está activo, suma puntos normales
    datos_juego["puntuacion"] += PUNTUACION_ACIERTO

# Resta puntos
def restar_puntos(datos_juego:dict):
  datos_juego["puntuacion"] -= PUNTUACION_ERROR

# Suma una vida (se invoca solo si hay 5 respuestas correctas consecutivas)
def sumar_vida(datos_juego):
  datos_juego["cantidad_vidas"] += 1

# Resta una vida si la respuesta fue incorrecta
def restar_vida(datos_juego):
  datos_juego["cantidad_vidas"] -= 1
  print(datos_juego["cantidad_vidas"])

# Verifica si hay vidas disponibles para restar en caso de una respuesta erronea. 
# Si no hay mas vidas para restar, se finaliza el juego.
def verificar_vidas( datos_juego, retorno ) -> bool:
 
  if datos_juego["cantidad_vidas"] > 0:
    restar_vida(datos_juego)
    restar_puntos(datos_juego)
    retorno = "juego"

  if datos_juego["cantidad_vidas"] == 0:
    retorno = "terminado"
      
  return retorno
