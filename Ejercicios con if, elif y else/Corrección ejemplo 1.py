#Se le solicita la edad al usuario
edad=int(input("Ingresa la edad: "))
#No se modifica nada adicional, ya que, se debe verificar si la edad es un número válido, quiere decir, es mayor o igual a 0.
if edad >= 0:
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("Edad invalida")