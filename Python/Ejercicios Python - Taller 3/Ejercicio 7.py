lista = ["Primero", "Segundo", "Tercero", "Cuarto"]
lista2 = ["Quinto", "Sexto", "Septimo", "Octavo", "Noveno"]
lista3 = []
for i in range(4):
    lista3.append(lista[i])
    for x in range(1):
        lista3.append(lista2[i])
print(lista3)





#7.   Diseñar un programa, que permita generar una lista de N cadenas, 
#posteriormente solicite un carácter, que se deberá insertar antes de 
#cada una de las cadenas de la lista original. El resultado debe imprimir ambas listas.