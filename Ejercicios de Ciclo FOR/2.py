
p = input("Ingrese la palabra")
vocales= "aeiouAEIOU"
g=0
for l in p:
    if l in vocales:
        g=+1
        print(f"{g}")
