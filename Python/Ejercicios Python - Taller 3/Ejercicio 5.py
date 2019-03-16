num = int(input("Cuantas entratas de texto desea? "))
lista = []
for i in range(num):
    lista.append(input("Escriba lo que desee. "))

cadena = input("Que cadena desea buscar? ")
print(lista.count(cadena))