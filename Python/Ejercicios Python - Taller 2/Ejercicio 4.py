def Conversion(p):
    print("En dolares americanos: ", (p*0.00032))
    print("En euros: ", (p*0.00028))
    print("En bitcoins: ", (p*8.3e-8))

pesos = float(input("Ingrese la cantidad de pesos a convertir: "))
Conversion(pesos)
