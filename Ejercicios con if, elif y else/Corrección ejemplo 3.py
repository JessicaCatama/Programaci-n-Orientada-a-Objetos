#Se le solicita la edad al usuario, si es miembros o no y si es miembro
edad=int(input("Ingresa un numero: "))
es_miembro=int(input("Confirma si eres miembro: "))
es_miembro = 0
#No se modifica nada adicional, ya que, se debe verificar si el usuario pertenece o no y si aplica por edad
if edad >= 60:
    if es_miembro:
        print("Descuento del 30% para mayores miembros")
    else:
        print("Descuento del 20% para mayores no miembros")
elif  edad >= 18:
    if es_miembro:
        print("Descuento del 10% para miembros adultos")
    else:
        print("No hay descuento para adultos no miembros")
else:
    print("Descuento solo para adultos")