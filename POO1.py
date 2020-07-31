class Coche():          #Classe
    
    def __init__(self):     #Constructor
    
        self.__largoChasis=250
        self.__anchoChasis=120     #Propiedades
        self.__ruedas=4          #Encapsulamos con dos giones __
        self.__enmarcha=False

    def arrancar(self,arrancamos):  #comportamientos METODOS
        self.__enmarcha=arrancamos        #Variable

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
            
        if(self.__enmarcha and chequeo):
            return "El coche esta en emarcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. no podemos arrancar"

        else:
            return "El coche esta parado"

    def estado(self):                   #Comportamientos METODOS
        print("El cohe tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un lardo de ",
        self.__largoChasis)

    def __chequeo_interno(self):                    #Encapsulamos el metodo
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"                #variables
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

            return True
        else:
            return False


miCoche=Coche()      #Instanciar una classe

#print("El largo del coche es: ",miCoche.largoChasis) 
#print("El coche tiene ",miCoche.ruedas,"ruedas")    #Accedemos a las propiedades
print(miCoche.arrancar(True))                              #Intanciar la classe
print(miCoche.estado())                 #Imprimir 

print("--------A continuación creamos el segundo objeto---------")

miCoche2=Coche()
#print("El largo del coche es: ",miCoche2.largoChasis) 
#print("El coche tiene ",miCoche2.ruedas,"ruedas") 
print(miCoche2.arrancar(False))
print(miCoche2.estado()) 