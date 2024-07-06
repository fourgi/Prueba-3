import csv
estudiantescsv = []
nuevos_alumnos = []
menu = 0

def proceso_estudiantes():
    with open ("ListaCurso5B.csv", "r") as procesoscsv:
        estudiantecsv = csv.DictReader(procesoscsv)
        print (procesoscsv)

def registro_estudiantes():
    try:
        print ("Por favor ingresa los siguietes datos: ")
        rut = input("Ingresa tu Rut: ")
        nombre = input("Ingresa tu nombre: ")
        nota_1 = float(input("Ingresa nota 1: "))
        nota_2 = float(input("Ingresa nota 2: "))
        if rut== "" or nombre ==""or nota_1==""or nota_2==0:
            print("Debe rellenar todos los datos")
        else:
            registro = {'Rut': rut,'NomBRE': nombre,'Nota 1': nota_1,'Nota 2': nota_2,}
            return registro
    except:
        print("Ingresa una opción válida.")        

    nuevos_alumnos.append({
        "Rut": rut,
        "Nombre": nombre,
        "Nota 1": nota_1,
        "Nota 2": nota_2
        })
    print(proceso_estudiantes)
registro_estudiantes()

def modificar_notas():
    rut_alumno = int(input("Ingresa tu Rut: "))
    for i in nuevos_alumnos:
        nueva_nota = int(input("¿Qué nota deseas modificar? 1.-Nota 1, 2.-Nota 2"))
        if nueva_nota == 1:
            modificar = float(input("Ingresa tu nueva Nota 1: "))
        elif nueva_nota == 2:
            modificar = float(input("Ingresa tu nueva Nota 2: "))
        else:
            print("Ingresa una opción válida.")


def eliminar_estudiantes():
    pass

def generar_promnotas():
    pass

def generar_acta_cierre():
    pass

def salir():
    pass

while True:
    menu != 7:
    try:
        menu = int(input("1- Procesar lista de estudiantes. \n2-Registrar estudiante.\n3-Modificar nota.\n4-Eliminar estudiante.\n5-Generar promedio de notas.\n6.-Generar acta de cierre de curso.\n7.-Salir.."))"))
        if menu==1:
            proceso_estudiantes()
        elif menu==2:
            registro_estudiantes()
        elif menu==3:
            modificar_notas()
        elif menu==4:   
            eliminar_estudiantes()
        elif menu==5:
            generar_promnotas()
        elif menu==6:
            generar_acta_cierre()
            elif menu==7:
                salir()
            else:
                print("ingrese una opcion valida")
    except:
        print("debe ingresar un numero")