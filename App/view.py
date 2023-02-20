﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import traceback
from tabulate import tabulate



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(input('Que tipo de datos entre ARRAY_LIST y SINGLE_LINKED quiere'))
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar las actividades económicas con mayor total saldo a pagar para todos los años")
    print("3- Listar las actividades económicas con mayor total saldo a favor para para todos los años")
    print("4- Encontrar el subsector económico con el menor total de retenciones para todos los años disponibles")
    print("5- Encontrar el subsector económico con los mayores costos y gastos de nómina para todos los años disponibles")
    print("6- Encontrar el subsector econmico con los mayores descuentos tributarios para todos los años disponibles")
    print("7- Encontrar la actividad económica con el mayor total de ingresos netos para cada sector económico en un año específico")
    print("8- Listar el TOP (N) de las actividades económicas con el menor total de costos y gastos para un periodo de tiempo")
    print("9-  Listar el TOP (N) de actividades económicas de cada subsector con los mayores totales de impuestos a cargo para un periodo de tiempo ")
    print("10- Obtener dato dado un ID")

    print("0- Salir")

def print_3_primeros_y_ultimos(lista, sample=3):

    size = lt.size(lista)
    lista_1 =lt.iterator(lista)

    
    if size<= sample*2:
        print('Los',size,'primeros impuestos son:')
        for impuesto in lista_1:
            print(impuesto)

    else:
        print('Los',sample, 'primeros impuestos son:')
        i=1
        while i <=sample:
            impuesto = lt.getElement(lista, i)
            print(impuesto)
            i+=1
        print('los',sample, 'últimos libros ordenados son:')
        i= size- sample +1
        while i <=size:
            impuesto = lt.getElement(lista, i)
            print(impuesto)
            i+=1 



def load_data(control):
    """
    Carga los datos
    """
    control_1 =controller.load_data(control, input('Ingrese nombre del archivo '))
    return control_1
def sort_data(control):
    type = input('Ingrese método de ordenamiento  sa para shell, se para selection o ins para insertion')
    control_1 = 0
    if type =='sa':
     control_1 = controller.sort_sa(control)
    elif type == 'se':
        control_1 = controller.sort_se(control)
    elif type == 'ins':
        control_1 = controller.sort_ins(control)

    else:
        print('error')
    return control_1

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print(controller.req_1(control))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    print(controller.req_2(control))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))


# Se crea el controlador asociado a la vista


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                control = new_controller()
                load_data(control)
                sort_data_result =sort_data(control)
                print_3_primeros_y_ultimos(sort_data_result[0])
                print(sort_data_result[1])
            
                
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
