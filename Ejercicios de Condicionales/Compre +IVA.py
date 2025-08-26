a=int(input('Ingrese valor del producto: '))
iva = a * 0.19
total = a + iva

if total > 1000000:
    product = (total * 5)/100
elif total < 1000000:
    product = (total * 1)/100

print(f'{product}')