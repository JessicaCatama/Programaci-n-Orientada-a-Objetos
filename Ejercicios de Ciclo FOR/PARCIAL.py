carro_electrico=1
carro_hibrido=2
carro_combustion=3

for a in range (1, 2, 3):
    print(a)

    A=float(input("Ingresa el valor del carro 1: "))
    B= float(input("Ingresa el valor del carro 2: "))
    C=float(input("Ingresa el valor del carro 3: "))

    soat = 542000

    if a == carro_electrico:
        matricula_tasa1 = 0.01
        iva_tasa1 = 0.05
        costo_total1 = (A * (1 + matricula_tasa1 + iva_tasa1)) + soat
        print(f"El valor total del carro eléctrico es: ${costo_total1:,.2f}")
    elif a == carro_hibrido:
        matricula_tasa2 = 0.05
        iva_tasa2 = 0.08
        costo_total2 = (B * (1 + matricula_tasa2 + iva_tasa2)) + soat
        print(f"El valor total del carro híbrido es: ${costo_total2:,.2f}")
    elif a == carro_combustion:
        matricula_tasa3 = 0.10
        iva_tasa3 = 0.19
        costo_total3 = (C * (1 + matricula_tasa3 + iva_tasa3)) + soat
        print(f"El valor total del carro a combustión es: ${costo_total3:,.2f}")

    valor_total = costo_total1 + costo_total2 + costo_total3
else:
    print(f"El valor total de los carros: ${valor_total:,.2f}")