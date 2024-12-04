import os
import json

# Leemos el archivo .json si existe. Si no, lo inicializamos vacío.
def leer_json(nombre_archivo:str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            try:
                ranking = json.load(archivo)
            except json.JSONDecodeError:
                ranking = []
    else:
        ranking = []
    return ranking


#CARGA json--------------------------------
def cargar_json(datos: dict) -> bool:
    archivo_json = "files/partidas.json"
    arr_datos = []

    # Si el archivo existe, cargar los datos actuales
    if os.path.exists(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as archivo:
            try:
                arr_datos = json.load(archivo)
            except json.JSONDecodeError:
                arr_datos = []  # Si el archivo está vacío

    # Agregar los nuevos datos
    arr_datos.append(datos)

    # Sobrescribir el archivo con los datos actualizados
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(arr_datos, archivo, indent=4)

    return True











