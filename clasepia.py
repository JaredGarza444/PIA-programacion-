#En este programa crearemos la clase que tuilizaremos mas adelante en nuestro PIA
#Importamos la libreria datetime ya que lo utilizaremos mas adelante en nuestro programa
import datetime

#Creamos la clase contacto que es donde guardaremos los objetos de nuestra lista y no sera utili al
#realizar el programa
class Contacto :
   #Decalro el uso del cosntructor
   #Este se utilizara para alamcenar los datos porporcionados por el archivo csv
   #Rellenamos con argumentos todas las propiedades de las clases
   #Pedimos todos los datos y tomamos la fecha proporcionada por el ususario
    def _init_(self,nickname,nombre,correo,telefono,gastos,fechanacimiento):
        self.nickname=nickname
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.gastos=gastos
        self.datetime=fechanacimiento



