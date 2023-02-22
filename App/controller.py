﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import time
import csv
from DISClib.ADT import list as lt
...
csv.field_size_limit(2147483647)


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(type):
    """
    Crea una instancia del modelo
    """

    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(type)
    return control


# Funciones para la carga de datos

def datos_por_año(datos: list):
    dic_anios ={}  
    for dato in datos:
        if dato['Año'] not in dic_anios:
            dic_anios[dato['Año']]=[dato]

        else:
            dic_anios[dato['Año']].append(dato)

    return dic_anios




def load_data(control, filename):
    """
    Carga los datos del reto
    """
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    catalog = control['model']
    for line in input_file:
        model.add_data(catalog, line)

    
    
    return  catalog

def crear_list_iterable(catalog):
    lista = lt.iterator(catalog)
    return lista
    # TODO: Realizar la carga de datos

def data_size(control):
    return lt.size(control['model']["data"])
# Funciones de ordenamiento

def sort(control, tipo):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    lista = model.sort(control["model"], tipo)
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    tamano = data_size(control)
    return lista, delta_t, tamano

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    req_1 = model.req_1(control["model"])
    return req_1


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    req_2 = model.req_2(control["model"])
    return req_2


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    req_3 = model.req_3(control["model"])
    return req_3


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    req_4 = model.req_4(control["model"])
    return req_4


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    req_5 = model.req_5(control["model"])
    return req_5


def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    req_6 = model.req_6(control["model"])
    return req_6


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    req_7 = model.req_7(control["model"])
    return req_7


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"])
    return req_8


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
