num = int(input("Hasta donde descea los numeros triangulares? "))
for num in range(1, num+1):
    x = int((num*(num+1)/2))
    print(x)