numero=int(input('Ingrese un número: '))

if numero == 0:
    print('El número es cero')
elif numero % 2 == 0:
    print(f'{numero} es un número par')
else:
    print(f'{numero} es un número impar')