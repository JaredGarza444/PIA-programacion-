#Importamos el modulo csv ya que en este programa se exportara un csv ya hecho
#Para trabajar con el
import csv
#Se importa el modulo itertools para el conteo identificador, ademas de que es
#Ncesario para trabajar con datos en secuencia
import itertools
#Tambien importamos  las libreria de expresiones regulares para poder ejecutar
#diversas validaciones
import re
#Ademas de importar el modulo datetime para que de esa manera se puedan trabajar
#Con fehcas de forma validada
import datetime
#Importamos os para poder trabajar con el sistema operativo
import os

#Procedemos a la creacion de las clases que seran necesarias para la grabacion y el uso
#De datos en nuestro csv
class Contacto:
  nuevoId=itertools.count()
  # Se declara un procedimiento constructor.
  # Aqui pondremos los datos que almacenaremos de nuestro contacto.
  def __init__(self,nickname,nombre,correo,telefono,fechanac,gastos):
    #De esta manera agregamos informacion a nuestra clase
    self.codigo=next(self.nuevoId)
    self.nickname = nickname
    self.nombre = nombre
    self.correo = correo
    self.telefono = telefono
    self.fechanac = fechanac
    self.gastos = gastos
    #Creamos la clase agenda que trabajara sobre la clase contactos llamandola y posteriormente
    #Creando una lista una lista
class Agenda:
    def __init__(self):
        self.contactos=[]
    #Creamos los metodos o funciones que vamos a utilizar en nuestra agenda
    def ordenarNickname(self):
        #Utilizamos lambda como clave ya que es una funcion anonima
        #Utiizamos la funcion sort para ordenar
        self.contactos.sort(key=lambda contacto: contacto.nickname)
    def ordenarNombre(self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)
    #Sirve para añadir infirmacion a nuestra clase contactos con la funcion append
    def añadir(self,nickname,nombre,correo,telefono,fechanac,gastos):
        contacto=Contacto(nickname,nombre,correo,telefono,fechanac,gastos)
        self.contactos.append(contacto)
     #Creamos metodo para mostrar informacion
    def mostrarTodos(self):
        self.submenuOrden()
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
      #Utilizamos metodo para que nos busque informacion en la clase por medio de
      # Expresiones regulares
    def buscar(self,textoBuscar):
        encontrado=0
        for contacto in self.contactos:
            if(re.findall(textoBuscar,contacto.nickname)) or (re.findall(textoBuscar,contacto.nombre)):
                self.imprimeContacto(contacto)
                encontrado=encontrado+1
                self.submenuBuscar(contacto.codigo)
        if encontrado==0:
            self.noEncontrado()
    def buscarborrar(self,textoBuscar):
        encontrado=0
        for contacto in self.contactos:
            if(re.findall(textoBuscar,contacto.nickname)) or (re.findall(textoBuscar,contacto.nombre)):
                self.imprimeContacto(contacto)
                encontrado=encontrado+1
                self.submenuBuscarBorrar(contacto.codigo)
        if encontrado==0:
            self.noEncontrado()
    #Por ultimo creamos un metodo para poder borrar informacion solititada
    def borrar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                print('--------------------------------')
                print('Quieres borrar el contacto?')
                print('1:Si 2:No')
                print('--------------------------------')
                opcion=str(input(""))
                #Establecemos una estrucura de decision que jecutara dependiento
                #Lo que pida el usuario
                if opcion=='1':
                    print('Contacto Borrado Correctamente')
                    del self.contactos[codigo]
                    break
                elif opcion=='2':
                    break
    #Creamos modulo para modificar informacion ya guardada en el archivo
    def modificar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                del self.contactos[codigo]
                nickname=str(input('Escribe el nickname: '))
                nombre=str(input('Escribe los nombre: '))
                correo=str(input('Escribe la correo: '))
                telefono=int(input('Escribe el telefono: '))
                fechanac=datetime.date(input('Escribe la fecha de nacimiento: '))
                gastos=int(input('Escribe los gastos: '))
                #Utilizamos capitalize para que la primera letra del dato siempre sea mayuscula
                contacto=Contacto(nickname.capitalize(),nombre.capitalize(),correo.capitalize(),telefono,fechanac,gastos)
                self.contactos.append(contacto)
                break
    #Agregamos este submenu para cuando ek usuario escoja la opcion de borrar informacion
    #Le damos una instruccion para que pueda borrar
    def submenuBuscar(self,codigo):
        print('Gracias por buscar')
        print('--------------------------------')
    def submenuBuscarBorrar(self,codigo):
        print('Escribe el siguiente valor para borrar la informacion solicitada ')
        print('1=Borrar')
        print('--------------------------------')
        opcion=str(input(""))
        if opcion=='1':
            self.borrar(codigo)
        elif opcion=='2':
            print('Continuamos sin realizar modificacion alguna')
    #Establecemos el metodo suborden para cuando el usuario seleccione la opcion de mostrar informacion
    #Se le da la opcion de la manera en como quiere en que aparezacan los datos es decir primero en nombre o el nikcname
    def submenuOrden(self):
        print('Quieres ordenar por nickname o por nombre?')
        print('1=Nickname')
        print('2=Nombre')
        print('--------------------------------')
        opcion=str(input(""))
        if opcion=='1':
            self.ordenarNickname()
        elif opcion=='2':
            self.ordenarNombre()
    #Por ultimo creamos el metodo grabar al que llamaremos cada vez que el archivo correspondiente sea modificado
    #Utilizamos la funcion writerow para que guarde la informacion dentro de la  lsita
    def grabar(self):
        with open('contactos_mobilcsv.csv','w') as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(('nickname','nombre','correo','telefono','fechanac','gastos'))
            for contacto in self.contactos:
                escribir.writerow((contacto.nickname,contacto.nombre,contacto.correo,contacto.telefono,contacto.fechanac,contacto.gastos))
    #Ejecutamos este metodo para cuando el usuaerio seleccione la opcion de mostrar los datps de nuestro archivo
    #e pedimos los datos a encotrar y dependiendo si se encuentra o no le despleiga un meseaje diciendo que fuen encontrado
    #O en su caso que no se encuentra y que ingrese uno nuevo
    def imprimeContacto(self,contacto):
        print('Contacto encontrado:')
        print('Nickname: {}'.format(contacto.nickname))
        print('Nombre: {}'.format(contacto.nombre))
        print('Correo: {}'.format(contacto.correo))
        print('Telefono: {}'.format(contacto.telefono))
        print('FechaNac: {}'.format(contacto.fechanac))
        print('Gastos: {}'.format(contacto.gastos))
        print('--------------------------------')
    def noEncontrado(self):
        print('Contacto no encontrado, por favor ingrese uno nuevo')
        print('--------------------------------')
#Por ultimo ponemos la funcion que ejecutara todo el programa
def ejecutar():
    agenda=Agenda()
    #Establecemos funcion en la que abrimos e archivo y corroboramos que existe, si es que existe la informacion sera modificada con
    #La informacion proporcioanda por el usuario
    #Si en dado casi el archivo aun no se crea entonces le informamos que aun no existe y que lo cree
    try:
        with open('contactos_mobilcsv.csv','r') as fichero:
            lector=csv.DictReader(fichero,delimiter='|')
            for fila in lector:
                agenda.añadir(fila['nickname'].capitalize(),fila['nombre'].capitalize(),fila['correo'].capitalize(),fila['telefono'].capitalize(),fila['fechanac'].capitalize(),fila['gastos'].capitalize())
    except:
        print('Error al abrir fichero o que no existe aun')
    #Mientras el archivo exista desplegamos el menu de opciones a escoger
    while True:
        menu=int(input("""
        \nSelecciona una opcion\n
        1: Añadir contacto
        2: Buscar contacto
        3: Eliminar contacto
        4: Mostrar lista de contactos
        0: Salir \n\n
        """))
        #Si la opcion es la 1 llamamos al metodo añadir y le pedimos al usuario los datos a añadir en el archivo
        if menu==1:
            nickname=str(input('Escribe el nickname: '))
            nombre=str(input('Escribe el nombre: '))
            correo=str(input('Escribe el correo: '))
            telefono=int(input('Escribe el telefono: '))
            año = int(input('Escribe el año de nacimiento "yyyy": '))
            mes = int(input('Escribe el numero de mes de nacimiento "mm": '))
            dia = int(input('Escribe el numero de dia de nacimiento "dd": '))
            gastos=int(input('Escribe los gastos: '))
            fechanac = datetime.date(año, mes, dia)
            print(type(fechanac))
            agenda.añadir(nickname.capitalize(),nombre.capitalize(),correo.capitalize(),telefono,fechanac,gastos)
            agenda.grabar()
        #Si la opcion escogida es la 2 entonces llamamos al metodo buscar y le pedimos al usario la informacion a buscar
        elif menu==2:
            texto=str(input('Escribe el texto a buscar en contactos: '))
            agenda.buscar(texto.capitalize())
            agenda.grabar()
        #Si la opcion elegida es 3 entonces llamamos al metodo buscarborrar y le pedimos al usuario la informaion a borrar
        elif menu==3:
            texto=str(input('Escribe el texto a buscar en contactos: '))
            agenda.buscarborrar(texto.capitalize())
            agenda.grabar()
        #Si la opcion elegida es 4 entonces llamamos al metodo mostrarTodos y le mostramos todos los contactos guardados
        elif menu==4:
            agenda.mostrarTodos()
        # Y pot ultimo si la opcion escogida es 0 mandamos mensaje de despedida y salimos del programa
        elif menu==0:
            print('Hasta pronto!!!')
            agenda.grabar()
            break
        #Si no selecciona ningun valor o algun erroneo le idicamos que esa opcion no es valida
        else:
            print('Opcion no valida!!!')
#Establecemos estructura para que se ejecute correctamente
if __name__=='__main__':
    ejecutar()