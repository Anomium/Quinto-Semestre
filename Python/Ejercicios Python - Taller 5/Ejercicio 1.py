e = open('texto1.txt', 'w')
e.write(input("Escriba lo que quiera: \n"))
e.close
num = int(input("Numero de bytes que desea leer: "))

#Lectura de bytes
e = open('texto1.txt', 'r')
dato = e.read(num)
print(dato, "\n")
e.close()