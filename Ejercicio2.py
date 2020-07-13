#Ejercicio 1
nombre=input("Ingrese el nombre del alumno: ")
apellido=input("Ingrese apellidos del alumno: ")
Español = float(input("Español: "))
Matematicas =float(input("Matematicas: "))
Programacion = float(input("Programacion: ")) 
promedio= (Español+Matematicas+Programacion)/3
print(f"El Alumno: {nombre} {apellido} ")
print(f"El promedio es: {promedio}")