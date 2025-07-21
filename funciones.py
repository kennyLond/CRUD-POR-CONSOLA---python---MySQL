def listarCursos(cursos):
    print("\nCursos: \n")
    contador=1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2}  ({3} créditos)" 
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
    curso=(codigo,nombre,credito)
    return curso