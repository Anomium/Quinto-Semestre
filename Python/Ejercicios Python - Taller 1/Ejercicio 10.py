def Celsius_F(grados):
    res = grados * 1.8 + 32
    return res 

def Celsius_K(grados):
    res = grados + 273.15
    return res

temperatura = float(input("Ingrese una temperatura a grados celsius"))
print("En Fahrenheit ", Celsius_F(temperatura))
print("En Kelvin ", Celsius_K(temperatura))