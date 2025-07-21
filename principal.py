from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while continuar: 
        opcionCorrecta = False
        while not opcionCorrecta:
            print("========= MENÚ PRINCIPAL =============")
            print("1 - Listar Curso")
            print("2 - Registrar Curso")
            print("3 - Actualizar Curso")
            print("4 - Eliminar Curso")
            print("5 - Salir")
            print(" ===================================== ")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción Incorrecta, Ingrese nuevamente....")
            elif opcion == 5:
                continuar = False 
                print("Gracias por usar este sistema")
                break 
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cursos=dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrio un error..")        

    elif opcion == 2:
        print ("Registro")
    elif opcion == 3:
        print ("Actualización")
    elif opcion == 4:
        print("Eliminación")
    else:
        print("Opción no Valida...")

menuPrincipal()
