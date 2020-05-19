def main():
  #Este programa se encaragar de almacemar las dos clases que seran necesarias para nuestro PIA  
  #Seran dos clases una llamada "Pais" y otra "Incidentes "
  #Los nombre de los objetos cumplen con las reglas del Pascal Casing

   #Utilozamos este import ya que usaremos fechas en el programa
  import Datetime 
  #Creamos la clase "Pais"
  class Pais():
    #Procedemso a gregar valores y porpiedades al objeto 
    #Lo hacemos mediante el cosntructor, en que idicamos sus argumentos correspondientes entre parentesis


    def _init_(self,Poblacion,NombreEsp,NombreIng,PDC,Contagios,Fallecidos):
          #Poblacion:Es la cantidad de personas con las que cuenta el Pais(int)
          #NombreEsp:Nombre del pais en español(str)
          #NombreIng:Nombre del pais en ingles(str)
          #PDC:Informa el primer dia de contagio del pais(date)
          #Contagiaos:El total de contagios del pais(int)
          #Fallecidos:Total de fallcidos en el pais(int)
          
          self.Poblacion=Poblacion
          self.NombreEsp=NombreEsp
          self.NombreIng=NombreIng
          self.PDC=PDC
          self.Contagios=Contagios
          self.Fallecidos=Fallecidos
  

  #Posteriormente procedemos con la creacion de la clase "Incidentes"
  class Incidentes():
    #Y le agregamos valores al objeto 
    
    def _init_(self, Fecha, Pais, Contagios, Fallecidos):
        #La fecha que en las que se obutvieron los datos(Datetime)
        #Pais:Nombre de la entidad correspondientes(str)
        #NuContagios:Nuevos contagios presentados(int)
        #NuFallacidos:Nuevos fallecidos presentados(int)
        
        self.Fecha=Fecha
        self.Pais=Pais
        self.Contagios=Contagios
        self.Fallecidos=Fallecidos

        #El seld no es un argumento de la clase si no que nos permite agregar valores al objeto de la clase 


     #Probamos la funcionalidad de nuestro porgrama garegando valores 
     
   miPais= Pais(str(Mexico),str(Mexico),int(1000),int(5000),datetime.datetime(2020, 5, 18))

   IncidentesNuevos= Incidentes(datetime.datetime(2020, 5, 18),str("Mexico"),int(1500),int(18))IncidentesHoy=Incidentes(datetime.datetime(2020, 5 18),str("Mexico"),int(1400),int(12))   
     
     print(miPais.NombreEsp)
     print(IncidentesNuevos.Fallecidos)

