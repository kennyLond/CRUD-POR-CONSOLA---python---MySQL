# Importa la clase DAO (Data Access Object) desde el módulo BD.conexion
# Esta clase se encarga de interactuar con la base de datos (consultas, inserciones, actualizaciones, etc.)
from BD.conexion import DAO

# Importa el módulo funciones, que contiene funciones auxiliares para pedir datos y mostrar información
import funciones

# Función principal del programa que muestra el menú y gestiona la interacción del usuario
def menuPrincipal():
    continuar = True  # Variable de control para mantener el programa en ejecución
    while continuar: 
        opcionCorrecta = False  # Bandera para controlar si se ha ingresado una opción válida
        while not opcionCorrecta:
            # Mostrar el menú principal
            print("========= MENÚ PRINCIPAL =============")
            print("1 - Listar Curso")
            print("2 - Registrar Curso")
            print("3 - Actualizar Curso")
            print("4 - Eliminar Curso")
            print("5 - Salir")
            print(" ===================================== ")
            # Solicita al usuario que seleccione una opción del menú
            opcion = int(input("Seleccione una opción: "))

            # Validación de la opción ingresada
            if opcion < 1 or opcion > 5:
                print("Opción Incorrecta, Ingrese nuevamente....")
            elif opcion == 5:
                # Si selecciona la opción 5, el programa termina
                continuar = False 
                print("Gracias por usar este sistema")
                break 
            else:
                # Si la opción es válida, se ejecuta la acción correspondiente
                opcionCorrecta = True
                ejecutarOpcion(opcion)

# Función que ejecuta la acción seleccionada por el usuario en el menú
def ejecutarOpcion(opcion):
    # Se crea una instancia del DAO para manejar las operaciones de base de datos
    dao = DAO()

    # Opción 1: Listar todos los cursos
    if opcion == 1:
        try:
            cursos = dao.listarCursos()  # Obtener lista de cursos desde la base de datos
            if len(cursos) > 0:
                funciones.listarCursos(cursos)  # Mostrar los cursos en consola
            else: 
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error..")        

    # Opción 2: Registrar un nuevo curso
    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()  # Pedir los datos del nuevo curso al usuario
        try:
            dao.registrarCurso(curso)  # Insertar el nuevo curso en la base de datos
        except:
            print("Ocurrió un error...")

    # Opción 3: Actualizar un curso existente
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()  # Obtener la lista actual de cursos
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)  # Pedir los datos de actualización
                if curso:
                    dao.actualizarCurso(curso)  # Actualizar los datos del curso en la base de datos
                else:
                    print("Código de curso a actualizar no encontrado")
            else:
                print("Código de curso no encontrado")
        except:
            print("Ocurrió un error...")

    # Opción 4: Eliminar un curso
    elif opcion == 4:
        try:
            cursos = dao.listarCursos()  # Obtener lista de cursos
            if len(cursos) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)  # Solicita el código del curso a eliminar
                if not (codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)  # Elimina el curso de la base de datos
                else:
                    print("Código de curso no encontrado")
        except:
            print("Ocurrió un error...")

    # Cualquier otra opción no es válida
    else:
        print("Opción no válida...")

# Llamada a la función principal para iniciar la ejecución del programa
menuPrincipal()
