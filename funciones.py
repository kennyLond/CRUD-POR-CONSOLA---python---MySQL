def listarCursos(cursos):
    print("\nCursos: \n")
    contador=1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2}  ({3} crédito)" 
        print(datos.format(contador, cur[0], cur[1],cur[2]))
        contador+=1
        print(" ")

def pedirDatosRegistro():
    codigoCorrecto=False
    while (not codigoCorrecto):
        codigo=input("Ingrese codigo: ") 
        if len(codigo)==10:
            codigoCorrecto=True
        else:
            print("Codigo incorrecto, debe tener 6 digitos")

    nombre=input("Ingrese nombre: ")

    creditosCorrectos=False
    while (not creditosCorrectos):
        credito=input("Ingrese créditos: ")
        if credito.isnumeric():
            if (int(credito)>0):
                creditosCorrectos=True 
                credito=int(credito)
            else:
                print("creditos incorrectos, debe ser un número mayor a 0")
        else:
            print("Creditos incorrectos: Debe ser un número unicamente")
    curso=(codigo,nombre,credito)
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar=input("Ingrese el codigo del cursos para editar: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo=True
            break
    if existeCodigo:
        nombre=input("Ingrese nombre para editar: ")

        creditosCorrectos=False
        while (not creditosCorrectos):
            credito=input("Ingrese créditos para editar: ")
            if credito.isnumeric():
                if (int(credito)>0):
                    creditosCorrectos=True 
                    credito=int(credito)
                else:
                    print("creditos incorrectos, debe ser un número mayor a 0")
            else:
                print("Creditos incorrectos: Debe ser un número unicamente")
        curso=(codigoEditar,nombre,credito)
    else:
        curso = None
    return curso    


def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar=input("Ingrese el codigo del curos para eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo=True
            break
    if not existeCodigo:
        codigoEliminar=""

    return codigoEliminar 