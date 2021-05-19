print("Asignatura optativas Año 2700")
print("Aginatura optativas: Informatica grafica - Prubeas de Software - Matematicas" )
#opcion=input("Escribe la Asignatura: ") //Almaceno en una variable para el lower o upper
asignatura = input("Escribe la Asignatura: ")
#asignatura=opcion.lower() //transforma el valor a minisculas
if asignatura in ("Informatica grafica","Pruebas de Software", "Matematicas"):
    print("Asignatura elegida " + asignatura)
    #En caso de que asignatura sea numero habria que colocar str(asignatura) para que convierta a string 
else:
    print("La Asigatura escogida no esta completada")

    #lower() transforma un valor a minisculas
    #upper() transforma un valor a mayusculas