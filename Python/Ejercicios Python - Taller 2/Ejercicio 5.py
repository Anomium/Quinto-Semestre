def orden(num):
    #y = sorted(num)
    num.sort()
    return num
    
x=[]
for i in range(3):
    x.append(input("Digite 3 valores enteros: "))

print(orden(x))
