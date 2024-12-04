from constantes.Constantes import *
import pygame

# Construye un texto en una superficie.
def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#Ordeno por puntaje
def ordenar_matriz_puntaje(lista_ranking: list) -> list:
   
    # Recorremos la lista de jugadores y comparamos sus puntos
    for fil_i in range(len(lista_ranking) - 1):
        for fil_j in range(fil_i + 1, len(lista_ranking)):
            # Accedemos a las puntuaciones correctas de los jugadores
            puntaje_i = lista_ranking[fil_i]["puntos"]
            puntaje_j = lista_ranking[fil_j]["puntos"]
            
            # Si el jugador en la posición i tiene menos puntos que el jugador en la posición j,
            # intercambiamos las posiciones para ordenar de mayor a menor.
            if puntaje_i < puntaje_j:
                aux = lista_ranking[fil_i]
                lista_ranking[fil_i] = lista_ranking[fil_j]
                lista_ranking[fil_j] = aux
                
    # Mostrar solo los primeros 10 jugadores
    lista_top_10 = lista_ranking[:10] 
    
    return lista_top_10


