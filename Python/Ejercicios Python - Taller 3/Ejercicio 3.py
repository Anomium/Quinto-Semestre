cadena = []
cadena = input("Escriba una oracion: ")
print("Dos primeros")
for i in range(0,2):
    print(cadena[i])

print("\nTres primeros")
for i in range(0,3):
    print(cadena[i])

print("\nCada dos caracteres")
for i in range(0, len(cadena), 2):
    print(cadena[i])

print("\nSentido inverso")
for i in range(len(cadena)-1, -1,-1):
    print(cadena[i])
