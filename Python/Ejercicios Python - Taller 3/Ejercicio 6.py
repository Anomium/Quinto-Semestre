num = int(input("Cuantos numeros quiere enlistar? "))
lista = []
mult = 1
suma = 0
mayor = 0
menor = 9999999999999
for i in range(num):
    lista.append(int(input("Digite un numero: ")))

for i in range(num):
    mult = lista[i] * mult

for i in range(num):
    suma = lista[i] + suma

#Menor
for x in range(num):
    menor = lista[x]
    for i in range(num):
        if (menor > lista[i]):
            menor = lista[i]

#Mayor
for x in range(num):
    mayor = lista[x]
    for i in range(num):
        if (mayor < lista[i]):
            mayor = lista[i]

print("El producto de la lista es: ", mult)
print("La suma de la lista es: ", suma)
print("El numero mayor: ", mayor)
print("El numero menor: ", menor)