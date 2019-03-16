x = int(input("Hasta donde descea los numeros triangulares? "))
def f(x):
    return int((x*(x+1)/2))

print([f(i) for i in range(x)])
