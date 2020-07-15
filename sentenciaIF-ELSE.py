print("Verificacion de acceso")

edad_usuario=int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
    print("no puede pasar")
elif edad_usuario>100:
    print("Edad Incorrecta")
else:
    print("Puede pasar")

print("El programa a finalizado")