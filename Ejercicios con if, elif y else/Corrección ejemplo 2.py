#Se le solicita un numero al usuario
numero=int(input("Ingresa un numero: "))
#No se modifica nada adicional, ya que, se debe verificar si el nunero o es cero o es menor que 0, para definir un negativo
if numero > 1:
    if numero % 2 == 0:
        print("El numero es positivo y par")
    else:
        print("El numero es positivo e impar")
elif  numero < 0:
     print("El numero es negativo")
else:
    print("El numero es cero")