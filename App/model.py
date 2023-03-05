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
    data["Costos y gastos nómina"] = costos_gastos_nom
    data["Aportes seguridad"] = apor_seguridad
    data["Aportes a entidades"] = apor_entidades
    data["Efectivo y equivalentes"] = efec_equivalentes
    data["Inversiones e instrumentos"] = inv_instru
    data["Cuentas y otros por cobrar"] = cuentas_cob
    data["Inventarios"] = inventario
    data["Propiedades"] = propiedades
    data["Otros activos"] = otros_act
    data["Total patrimonio bruto"] = total_patrim_bruto
    data["Pasivos"] = pasivos
    data["Total patrimonio líquido"] = total_patrim_liquido
    data["Ingresos ordinarios"] = ingresos_ordin
    data["Ingresos financieros"] = ingresos_finan
    data["Otros ingresos"] = ingresos_otr
    data["Total ingresos brutos"] = total_ingresos_brut
    data["Devoluciones, rebajas"] =devoluciones_rebaj
    data["Ingresos no renta"] = ingresos_no_renta
    data["Total ingresos netos"] = total_netos
    data["Costos"] = costos
    data["Gastos administración"] = gastos_ad
    data["Gastos distribución"] = gastos_dist
    data["Gastos financieros"] = gastos_finan
    data["Otros gastos"] = gastos_otr
    data["Total costos y gastos"] = total_c_g
    data["Renta líquida ordinaria"] = renta_liq_ord
    data["Pérdida líquida"] = perdida_liq
    data["Compensaciones"] = compensaciones
    data["Renta líquida"] = renta_liq
    data["Renta presuntiva"] = renta_presu
    data["Renta exenta"] = renta_exen
    data["Rentas gravables"] = renta_grava
    data["Renta líquida gravable"] = renta_liq_grava
    data["Ingresos ganancias ocasionales"] = ingreso_ganan_oca
    data["Costos ganancias ocasionales"] = costos_ganan_oca
    data["Ganancias ocasionales no gravadas"] = ganan_oca_no_grava
    data["Ganancias ocasionales gravables"] = ganan_oca_grava
    data["Impuesto RLG"] = impuesto_rlg
    data["Descuentos tributarios"] = descuentos_trib
    data["Impuesto neto de renta"]= imp_net_rent
    data["Impuesto ganancias ocasionales"] = imp_ganan_oca
    data["Total Impuesto a cargo"] = total_imp_carg
    data["Anticipo renta año anterior"] = antic_anio_ant
    data["Saldo a favor año anterior"] = saldo_afav_ant
    data["Autorretenciones"] = autoreten
    data["Otras retenciones"] = otras_reten
    data["Total retenciones"] = total_reten
    data["Anticipo renta siguiente año"] = anti_rent_sig
    data["Saldo a pagar por impuesto"] = saldo_paga_imp
    data["Sanciones"] = sanciones
    data["Total saldo a pagar"] = total_s_pagar
    data["Total saldo a favor"] = total_favor
    data['Total retenciones'] =total_reten

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

def encontrar_mayor(lista):
    #encuentra el mayor dentro de una lista
    i =0
    tamanio = lt.size(lista)
    
    while i < tamanio:
        exacto = lt.getElement(lista,i)
        if int(exacto["Total saldo a favor"])>i:
            respuesta = exacto
        i+=1
    return respuesta






def crear_lista_con_mayor(dict_anios, factor):
 # crea una lista con el mayor de cada año segun factor
    lista_de_mayores = lt.newList(datastructure="ARRAY_LIST")
    for fecha in dict_anios.keys():
        mayor_por_anio = encontrar_mayor(dict_anios[fecha],factor)
        lt.addLast(lista_de_mayores, mayor_por_anio)

    return lista_de_mayores






def crear_diccionario(data_structs):
    tamanio = data_size(data_structs)
    i =0
    anios = {}
    #organiza la informacion en diccionarios con la llave como el año
    while i < tamanio:
        variable = lt.getElement(data_structs["data"],i)
        momento = variable["Año"]
        if variable["Año"] not in anios.keys():
            anios[momento] = lt.newList(datastructure="SINGLE_LINKED")
            lt.addLast(anios[momento], variable )
        elif variable["Año"] in anios.keys():
            lt.addLast(anios[momento], variable  )
        
        i +=1
    # crea una lista con el mayor de cada año
    busca = "Total saldo a favor"

    mayor = lt.newList(datastructure="ARRAY_LIST")
    for fecha in anios.keys():
        alto = encontrar_mayor(anios[fecha])
        lt.addLast(mayor, alto)
    
    repeticiones = lt.size(mayor)
    respuesta = ordenar(mayor, "Año", repeticiones, 0)
    
    final = lt.iterator(respuesta)
    return (final)

 
    

    
    
def crear_lista_subsectores_por_anio(lista_actividades):
    ### Crea lista TAD ARRAY de subsectores por año
    dic_subsecs ={}
    
    lista_actividades = lt.iterator(lista_actividades)
    ## primero crea diccionario
    for impuesto in lista_actividades:
        llave_subsector_dado =impuesto['Código subsector económico']
        if llave_subsector_dado not in dic_subsecs.keys():
            
            dict_subsector_dado = {}
            dict_subsector_dado['Año']=impuesto['Año']
            dict_subsector_dado['Código sector económico']=impuesto['Código sector económico']
            dict_subsector_dado['Nombre sector económico']=impuesto['Nombre sector económico']
            dict_subsector_dado['Código subsector económico']=impuesto['Código subsector económico']
            dict_subsector_dado['Nombre subsector económico']=impuesto['Nombre subsector económico']
            dict_subsector_dado['Total retenciones']=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']=float(impuesto['Total saldo a favor'])
            dict_subsector_dado['Primeras y últimas 3 actividades en contribuir'] = 0

            dic_subsecs[llave_subsector_dado]=dict_subsector_dado
        else:
            ## Va contando los totales
            dict_subsector_dado =dic_subsecs[llave_subsector_dado]
            dict_subsector_dado['Total retenciones']+=float(impuesto['Total retenciones'])
            dict_subsector_dado['Total ingresos netos']+=float(impuesto['Total ingresos netos'])
            dict_subsector_dado['Total costos y gastos']+=float(impuesto['Total costos y gastos'])
            dict_subsector_dado['Total saldo a pagar']+=float(impuesto['Total saldo a pagar'])
            dict_subsector_dado['Total saldo a favor']+=float(impuesto['Total saldo a favor'])
    
     ### Lista Tad       
    lista_subsects=lt.newList(datastructure="ARRAY_LIST")
    for llave in dic_subsecs.keys():
        lt.addLast(lista_subsects,dic_subsecs[llave])

    return lista_subsects

def agregar_lista_de_6_a_subsector(subsector, lista_de_actividades_un_anio):

        tamanio = lt.size(lista_de_actividades_un_anio)
        
        
        
        lista_6_activ_por_anio = lt.newList(datastructure='ARRAY_LIST')
        
        lt.addLast(lista_6_activ_por_anio,lt.getElement(lista_de_actividades_un_anio,1))
        lt.addLast(lista_6_activ_por_anio,lt.getElement(lista_de_actividades_un_anio,2))
        lt.addLast(lista_6_activ_por_anio,lt.getElement(lista_de_actividades_un_anio,3))
        lt.addLast(lista_6_activ_por_anio,lt.getElement(lista_de_actividades_un_anio,(tamanio-2)))
        lt.addLast(lista_6_activ_por_anio,lt.getElement(lista_de_actividades_un_anio,(tamanio-1)))
        lt.addLast(lista_6_activ_por_anio,lt.getElement(lista_de_actividades_un_anio,(tamanio)))

        subsector['Primeras y últimas 3 actividades en contribuir']= lista_6_activ_por_anio
        return subsector



            

            






def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    ### Crea diccionario por años
    
    dic_por_anios = crear_diccionario(data_structs)

    
    lista_menores_por_anio =lt.newList(datastructure='ARRAY_LIST')
    
    

    for anio in dic_por_anios.keys():

        

        ### llama la lista de impuestos por año y la ordena 
        lista_impuestos_por_anio = quk.sort(dic_por_anios[anio],sort_criteria_retenciones)
        
       
        lista_subsects = crear_lista_subsectores_por_anio(lista_impuestos_por_anio)
        menor =encontrar_menor(lista_subsects,'Total retenciones')

        agregar_lista_de_6_a_subsector(menor,lista_impuestos_por_anio)
        lt.addLast(lista_menores_por_anio,menor)
    lista_menores_por_anio = quk.sort(lista_menores_por_anio, sort_criteria)   
    
    return lista_menores_por_anio

    

def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_struct):
    """
    Función que soluciona el requerimiento 5
    """
    codigos= ["Descuentos tributarios", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor" ]
    tamanio = data_size(data_struct)
    anios = organizar(data_struct,"data", "Año", tamanio)
    organizado = {}
    extremos = {}
    respuesta = {}
    
    for fecha in anios.keys():
        repeticiones = lt.size(anios[fecha])
        if repeticiones <=6:
            orden = ordenar(anios[fecha], "Descuentos tributarios", repeticiones, 0 )

        else:
            orden = []
            orden.append(ordenar(anios[fecha], "Descuentos tributarios", 3, 0 ))
            comienza = lt.size(anios[fecha])-3
            orden.append(ordenar(anios[fecha], "Descuentos tributarios", 3, comienza ))


        extremos[fecha] = orden

        size = lt.size(anios[fecha])

        sub_sector = organizar(anios,fecha, "Código subsector económico", size )
        organizado[fecha] = sub_sector
        
        for sector in organizado[fecha].keys():
            respuesta = {}
            
            for codigo in codigos:
            
                suma = suma_variable(organizado[fecha][sector],codigo )
                respuesta[codigo] = suma
                
            organizado[fecha][sector] = respuesta

                
    print (organizado)
    

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
            cod_1 = impuesto_1['Año'].split()[0]
            cod_2 = impuesto_2['Año'].split()[0]
            return(float(impuesto_1['Año'])> float(impuesto_2['Año']))
    
    else:
            cod_1 = impuesto_1['Código actividad económica'].split()[0].split('/')[0]
            cod_2 = impuesto_2['Código actividad económica'].split()[0].split('/')[0]
            return(float(cod_1)>float(cod_2))
    

def sort_criteria_retenciones(impuesto1,impuesto2):
    cod_1 = impuesto1['Total retenciones'].split()[0].split('/')[0]
    cod_2 = impuesto2['Total retenciones'].split()[0].split('/')[0]
    return(float(cod_1)>float(cod_2))

    
    
    


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
    
    elif tipo == 4:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =quk.sort(sub_list, sort_criteria)
    
    elif tipo == 5:
        sub_list = lt.subList(data_structs['data'],1,data_size(data_structs))
        lista =merg.sort(sub_list, sort_criteria)
    
    return lista

#encontrar el mayor en una lista 
def encontrar_mayor(lista, nommbre):
    
    i =0
    tamanio = lt.size(lista)
    
    while i < tamanio:
        exacto = lt.getElement(lista,i)
        if int(exacto[nommbre])>i:
            respuesta = exacto
        i+=1
    return respuesta

#organiza la informacion en diccionarios con la llave como el año
def organizar (data_structs, tipo ,categoria,tamanio):
    
    i =0
    dic = {}
    
    while i < tamanio:
        variable = lt.getElement(data_structs[tipo],i)
        momento = variable[categoria]
        if variable[categoria] not in dic.keys():
            dic[momento] = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(dic[momento], variable )
        elif variable[categoria] in dic.keys():
            lt.addLast(dic[momento], variable  )
        
        i +=1
    return dic

#ordenar la lista en orden
def ordenar(lista, criterio, repeticiones, donde ):
    #organiza por años de menor a mayor
    respuesta = lt.newList("SINGLE_LINKED")
    
    for x in range( repeticiones):
        inicio = pos = lt.getElement(lista,donde)
        superior = inicio[criterio]
        a = 0
        elim = 0
        while a < lt.size(lista):
            pos = lt.getElement(lista,a)
            if  int(pos[criterio])>int(superior):
                superior = int(pos[criterio])
                elim = a
                dict = pos
            a+=1
            
        lt.addFirst(respuesta, dict)
        lt.deleteElement(lista, elim)

    return respuesta 

#suma la variable dentro de una lista con un criterio expecifico
def suma_variable(dic, suma):
    tamanio = lt.size(dic)
    i = 0
    valor = 0

    while i < tamanio:
        pos = lt.getElement(dic, i)
        valor += int(pos[suma])
        i+=1
    
    
    
    return valor