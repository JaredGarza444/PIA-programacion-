# Importamos libreria de expresiones regulares que igualmente se utilzara mas adelante
import re
#Se importa la clase contacto elaborada previamente
from clasepia import Contacto

#Importamos libreria de archivos csv, lo usaremos mas adelante
import csv


#Importamos la libreria para trabajar directamente con el sistema operativo
import os
#Importamos la libreria para trabajar con expresiones regulares
import re

#Se establece la funcion borrar pantalla para trabajar de mejor manera en el
#Sistema operativo
LimpiarPantalla = lambda: os.system('cls')

#Establecemso un validador de expresiones regulares en donde retornara positivo si solo
#se cumpla con la validacion de la expresion regular
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        #Le mostramos al usuario las diferentes opciones que se pueden ejecutar dentro del programa
        print("Mostrando lista de contactos")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        #Le preguntamos al usario cual es su decision
        opcion= input("¿Qué es lo que deseas hacer?  > ")
        if RegEx(opcion,"^[123450]{1}$"):
            if opcion=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break

            if opcion=="1":
                print("Llamar procedimiento para la acción")

            if opcion=="2":
                print("Llamar procedimiento para la acción")

            if opcion=="3":
                print("Llamar procedimiento para la acción")

            if opcion=="4":
                print("Llamar procedimiento para la acción")
               #REALIZAMOS EL PROGRAMA CORRESPONDIENTE A LA ELECCION 4
                with open('contactos_mobilcsv.csv') as archivo_csv:
                    lector_csv = csv.reader(archivo_csv, delimiter='|')
                    #Inicio el contador de lineas, para poderlas  al final.
                    contadorlinea=0
                    #Realizamos una lectura en la que examina uno po uno los datos del archivo.
                    for linea_datos in lector_csv:
                        if contadorlinea== 0:
                            #En caso que la linea examinada sea la primera entonces se despliga los datos que se guardara en la clase
                            print(f'Los nombres de las columnas son {", ".join(linea_datos)}')
                        else:
                            #Si el resultado es contrario entonces se procede a  imprimir los datos examinados del archivo
                            print(f'\tnickname: {linea_datos[0]}.')
                            print(f'\tnombre: {linea_datos[1]}.')
                            print(f'\tcorreo: {linea_datos[2]}.')
                            print(f'\ttelefono: {linea_datos[3]}.')
                            print(f'\tfechanacimiento: {linea_datos[4]}.')
                            print(f'\tgastos: {linea_datos[5]}.')
                            print(f'\t------------------------------------------')
                            #Se incrementa la  linea independientemente de lo que pase, para que de esta manera el programa llegue a su fin
                        contadorlinea += 1
                        print(f'Lineas examinadas {contadorlinea} lineas.')

            if opcion=="5":
                print("Llamar procedimiento para la acción")


            input("Pulsa enter para contunuar...")
        else:
            print("Esta no es una opcion valida por favor intentar otra")
            input("Pulsa enter para continuar")
            #Cada vez que el usuario termina su decision les pedimos que continue para cerrar el programa o realizar otra accion




principal()












