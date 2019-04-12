def Agregar():
    nombre = input("Introduzca el nombre: \n")
    telefono = input("Introduzca el telefono: \n")
    email = input("Introduzca el email: \n")
    contacto = open("agenda.txt", "a")
    contacto.write(nombre + "," + telefono + "," + email + "\n")
    contacto.close()
    print("Se ha añadido con éxito\n")
    Opciones()

def Ver():
    contacto = open("agenda.txt", "r")
    contacto = contacto.read()
    print(Contenido)
    contacto.close()

def Borrar():
    e = open("agenda.txt", "r")
    lineas = e.readlines()
    NombreBorrar = input("Nombre del contacto a borrar: ")
    contacto = open("agenda.txt", "w")
    
    for linea in lineas:
        lista = linea.split(",")
        if (lista[0] != NombreBorrar):
            contacto.write(linea)
    contacto.close()
    print("Se borró el contacto\n")
    Opciones()

def Opciones():
    try:
        Opcion = int(input("¿Qué quieres hacer? Seleccione un número \n 1) Agregar | 2) Ver | 3) Borrar | 4) Salir \n"))
    except Exception as e:
        raise e 
    if (Opcion == 1):
        Agregar()
    elif (Opcion == 2):
        Ver()
    elif (Opcion == 3):
        Borrar()
    elif (Opcion == 4):
        print("¡Adios!")
        exit()
    else: 
        print("\n\nDebe seleccionar una opción valida\n\n")
        Opciones()

Opciones()