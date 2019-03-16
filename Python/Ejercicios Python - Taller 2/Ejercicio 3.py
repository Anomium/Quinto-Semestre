def f(costo, seg):
    return costo * seg

def tiempo(seg):
    hora = (seg / 3600)
    minutos = (seg / 60)
    tiempo =  "En horas: "+str(hora) +", En minutos: "+ str(minutos) +", En segundos: "+ str(seg)
    return tiempo


c = int(input("Digite el costo por segundo: "))
s = int(input("Digite la duracion de la llamada: "))

costo = f(c,s)
duracion = tiempo(s)

print("El costo de la llamada es ${0} y la duracion {1}: ".format(costo, duracion))