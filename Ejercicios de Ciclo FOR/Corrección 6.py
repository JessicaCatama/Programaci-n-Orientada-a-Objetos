n = int(input("Ingrese un número: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()