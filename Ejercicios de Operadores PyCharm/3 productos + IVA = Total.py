a=int(input('Ingrese valor del producto 1: '))
b=int(input('Ingrese valor del producto 2: '))
c=int(input('Ingrese valor del producto 3: '))

iva = a * 0.19
total_a = a + iva

iva = b * 0.19
total_b = b + iva

iva = c * 0.19
total_c = c + iva

suma = total_a + total_b + total_c

print(f'{suma}')