import os

def crear_diccionario(lista_valores:list) -> dict:
    diccionario = {}
    diccionario["pregunta"] = lista_valores[0]
    diccionario["respuesta_1"] = lista_valores[1]
    diccionario["respuesta_2"] = lista_valores[2]
    diccionario["respuesta_3"] = lista_valores[3]
    diccionario["respuesta_4"] = lista_valores[4]
    diccionario["respuesta_correcta"] = lista_valores[5]
    
    return diccionario


def leer_csv(nombre_archivo:str,lista:list) -> bool:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r", encoding='utf-8') as archivo:
            #Leer la primer linea del archivo y no hacer nada.
            archivo.readline()
            for linea in archivo:
                linea = linea.replace("\n","") 
                lista_valores = linea.split(",")
                diccionario = crear_diccionario(lista_valores)
                lista_preguntas.append(diccionario)
            retorno = True
    else:
        retorno = False
        
    return retorno

#1. Leer csv -> Generamos la lista de diccionarios
lista_preguntas = []

leer_csv("files/preguntas_harry_potter.csv", lista_preguntas)