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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos




def new_data_structs(type):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=type,
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"], data["Código actividad económica"], data["Nombre actividad económica"],
                data["Código sector económico"],data["Nombre sector económico"],data["Código subsector económico"],
                data["Nombre subsector económico"],data["Total ingresos netos"],data["Total costos y gastos"], data["Total saldo a pagar"],
                data['Total saldo a favor'])
    lt.addLast(data_structs["data"], d)

    return data_structs


# Funciones para creacion de datos

def new_data(anio, cod_acti, nom_acti, cod_sector, nom_sector, cod_subsec, nom_subsec, total_netos, total_c_g, total_s_pagar, total_favor):
    
    data = {'Año': 0, "Código actividad económica": "","Nombre actividad económica": "","Código sector económico": "","Nombre sector económico": "",
    "Código subsector económico": "","Nombre subsector económico": "","Total ingresos netos": "","Total costos y gastos": "","Total saldo a pagar": "",
    "Total saldo a favor": ''}
    data["Año"] = anio
    data["Código actividad económica"] = cod_acti
    data["Nombre actividad económica"] = nom_acti
    data["Código sector económico"] = cod_sector
    data["Nombre sector económico"] = nom_sector
    data["Código subsector económico"] = cod_subsec
    data["Nombre subsector económico"] = nom_subsec
    data["Total ingresos netos"] = total_netos
    data["Total costos y gastos"] = total_c_g
    data["Total saldo a pagar"] = total_s_pagar
    data["Total saldo a favor"] = total_favor

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(impuesto_1, impuesto_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    if impuesto_1['Año']!= impuesto_2['Año']:
        return(float(impuesto_1['Año'])> float(impuesto_2['Año']))
    
    else:
        return(float(impuesto_1['Código actividad económica'])>float(impuesto_2['Código actividad económica']))
    


def sort(data_structs, tipo):
    if tipo == 1:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =ins.sort(sub_list, sort_criteria)

    elif tipo == 2:

        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =se.sort(sub_list, sort_criteria)
    elif tipo == 3:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =sa.sort(sub_list, sort_criteria)
    
    return lista