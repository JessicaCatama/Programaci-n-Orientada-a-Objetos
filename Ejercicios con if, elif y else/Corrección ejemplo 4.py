peso=float(input("Ingresa su peso en kilogramos: "))
estatura=float(input("Ingresa su estatura en metros: "))
semestre=int(input("Ingresa el semestre que cursas actualmentre: ")

buen_estudiante=0
#Evaluación con if anidados
if peso < 70:
    if estatura > 1.80:
        if semestre < 4:
            if buen_estudiante:
                print ("Puedes ingresar")
            else:
                print("")
        else:
            print("")
    else:
        print("")
else:
print("")