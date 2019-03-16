num1 = int(input("Digite un numero: "))
num2 = int(input("Digite el segundo numero: "))

if num1 > num2:
    for num2 in range(num2, num1):
        if num2 % 2 == 0:
            print(num2)

elif num2 > num1:
    for num1 in range(num1, num2):
        if num1 % 2 == 0:
            print(num1)
elif num1 == num2:
    print("No existe numero par entre estos dos numeros.")