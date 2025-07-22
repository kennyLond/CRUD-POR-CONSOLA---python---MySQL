# Función para listar todos los cursos en consola
def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        # Formatea y muestra cada curso con su código, nombre y créditos
        datos = "{0}. Código: {1} | Nombre: {2}  ({3} crédito)" 
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador += 1
        print(" ")

# Función que solicita al usuario los datos para registrar un nuevo curso
def pedirDatosRegistro():
    codigoCorrecto = False
    while not codigoCorrecto:
        codigo = input("Ingrese codigo: ") 
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Código incorrecto, debe tener 6 dígitos")  

    nombre = input("Ingrese nombre: ")

    creditosCorrectos = False
    while not creditosCorrectos:
        credito = input("Ingrese créditos: ")
        if credito.isnumeric():
            if int(credito) > 0:
                creditosCorrectos = True 
                credito = int(credito)
            else:
                print("Créditos incorrectos, debe ser un número mayor a 0")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente")
    
    # Retorna una tupla con los datos del curso
    curso = (codigo, nombre, credito)
    return curso

# Función que solicita los datos para actualizar un curso existente
def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el codigo del cursos para editar: ")
    
    # Verifica si el código ingresado existe en la lista de cursos
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre para editar: ")
        
        creditosCorrectos = False
        while not creditosCorrectos:
            credito = input("Ingrese créditos para editar: ")
            if credito.isnumeric():
                if int(credito) > 0:
                    creditosCorrectos = True 
                    credito = int(credito)
                else:
                    print("Créditos incorrectos, debe ser un número mayor a 0")
            else:
                print("Créditos incorrectos: Debe ser un número únicamente")

        # Retorna tupla con los datos editados
        curso = (codigoEditar, nombre, credito)
    else:
        # Si el código no existe, retorna None
        curso = None
    return curso    

# Función que pide el código de un curso para eliminarlo
def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el código del curso para eliminar: ")
    
    # Verifica si el código existe
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    # Si no existe, retorna string vacío
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar
