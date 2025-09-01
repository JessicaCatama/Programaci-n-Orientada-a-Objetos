a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

suma = a + b
resultado = suma

if suma < 50:
    suma = resultado / 2
    print("La respuesta es: ", suma)
elif suma > 50:
    suma = resultado * 2
    print("La respuesta es: ", suma)