#def generaPares(limite):
 #   num=1
  #  miLista=[] #Creamos una lista vacia
   # while num<limite:
    #    miLista.append(num*2) #Agregamos un numero a la lista en este caso 1*2
     #   num=num+1
    #return miLista
#print(generaPares(10)) 

#CON GENERADOR Ejercicio 1
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2 # yield almacena el numero del generador
        num=num+1
devuelvePares=generaPares(10) #Almacenamor¿s la funcion en una variable
#for i in devuelvePares:
#    print(i)               #Muestra en lista los numeros


print(next(devuelvePares))      #next Imprime sel primer un numero del generador
print("Aqui podria ir mas código...")

print(next(devuelvePares))         #Imprime el segundo numero del generador
print("Aqui podria ir mas código...")

print(next(devuelvePares))  #Imprime el tercer numero generado


#Ejercicio 2 para Sacar frase por frase

def devuelve_ciudades(*ciudades): #recibira un numero indeterminado de elementos y sera en forma de tupla
    for elemento in ciudades:
        yield elemento  #Genrador va contando de frase a frase

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas)) #Imprime la primera frase
print(next(ciudades_devueltas)) #Imprime la segunda frase


#Ejercicio 3 para Sacar letra por letra
def devuelve_ciudades(*ciudades): #recibira un numero indeterminado de elementos y sera en forma de tupla
    for elemento in ciudades:
        for Subelemento in elemento:
            yield elemento  #Genrador va contando de letra en letra

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas)) #Imprime la primera letra
print(next(ciudades_devueltas)) #Imprime la segunda letra

# Utilizamos el yield from para sacar la lista de palabra a palabra

#for elemento in ciudades:
 #       for Subelemento in elemento:
 #           yield elemento  #Genrador va contando de letra en letra

#En vez de esto simplicamos de la siguiente manera

#for elemento in ciudades:
#            yield from elemento
