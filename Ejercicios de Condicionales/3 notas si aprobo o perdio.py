a=int(input('Ingrese la nota 1: '))
b=int(input('Ingrese la nota 2: '))
c=int(input('Ingrese la nota 3: '))

suma = (a + b + c)
promedio = suma/50

if promedio<30:
    print('Perdiste :(!')
if (promedio>=30 and promedio<=40):
    print('Aprobaste!')
if (promedio>=41 and promedio<=45):
    print('Excelente!')
if (promedio>=46 and promedio<=50):
    print('Felicitaciones!')
elif (promedio>50):
    print("Marcha")
else:
    print("No se identifica")