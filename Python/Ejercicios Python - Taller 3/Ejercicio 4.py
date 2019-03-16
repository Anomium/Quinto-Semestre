lista = []
for i in range(11):
    lista.append(input("Digite varios numeros: "))

listaD = lista
listaU = dict.fromkeys(lista)

print(listaD, "\n")
print(listaU)