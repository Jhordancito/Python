#i = 1
#while i<=10:
#    print("Ejecución " + str(i))
#    i=i+1;
#print("Terminó la ejecución")

#edad=int(input("Introduce tu edad por favor: "))

#while edad<0 or edad>100:
#    print("Has introducido una edad Inocrrecta. Vuelve a intentarlo")
#    edad = int(input("Introduce tu edad por favor: "))
#print("Gracias por colaborar. Puedes Pasar")
#print("Edad del aspirante " + str(edad))

import math
print("Programa de cálculo de raiz cuadrada")
numero = int(input("Introudce un Numero: "))

intentos=0

while numero<0:
    print("No se puede hallar la raíz de un numero negativo")

    if(intentos==2):
        print("Has consumido demaisados intentos. El programa ha finalizado")
        break;
    numero=int(input("Introudce un Numero: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion= math.sqrt (numero)
    print("La Raiz cuadrada de " + str(numero) + " es " + str(solucion) )

