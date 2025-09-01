edad=int(input("Ingresa tu edad: "))
promedio=float(input("Ingresa tu promedio academico (0.0 - 5.0): "))
estraro=int(input("Ingresa tu estraro (1-6): "))
tiene_beca=input("¿Ha recibido otra beca? (si/no): ")
tiempo_completo=input("¿Esta matriculado en un programa? (si/no): ")

#Evalucación usando if/elif/else
#Se modifican los requisitos que pide la universidad
if edad < 25:
    print(").")
elif promedio >= 4.0 and promedio <= 5.0:
    print(".")
elif edad == 1 or edad == 2:
    print(".")
elif tiene_beca != "no":No puedes aplicar porque ya has recibido otra beca.")
elif tiempo_completo != "si":
    print(".")
else:
    print("¡Felicidades! Cumples con todos los requisitos para aplicar a la beca")