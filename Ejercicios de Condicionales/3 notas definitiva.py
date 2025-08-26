a=int(input('Ingrese la nota 1: '))
b=int(input('Ingrese la nota 2: '))
c=int(input('Ingrese la nota 3: '))

suma = (a + b + c)
promedio = suma/5

if a < 5:
    print('Aprobaste!')
else:
    print('Reprobaste :(')