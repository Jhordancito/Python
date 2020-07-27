#def generaPares(limite):

 #   num=1

  #  miLista=[]

   # while num<limite:

    #    miLista.append(num*2)

     #   num=num+1
    #return miLista

#print(generaPares(10)) 

def generaPares(limite):

    num=1
    while num<limite:

        yield num*2 # yield almacena el numero del generador

        num=num+1

devuelvePares=generaPares(10)
print(next(devuelvePares))      #next Imprime solo un numero del generador
print("Aqui podria ir mas código...")

print(next(devuelvePares))         #Imprime el segundo numero del generador
print("Aqui podria ir mas código...")
