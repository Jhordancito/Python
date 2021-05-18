print("Programa tendra una función llamada DEVUELVEMAX")

num1 = int(input("Introducir el primer Numero:" ))
num2 = int(input("Introducir el segundo Numero:" ))

def DevuelveMax(num1,num2):
 if num1>num2:
     print(f"El {num1} es mayor")
 else:
    print(f"El {num2} es mayor")

DevuelveMax(num1,num2)