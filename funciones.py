def listarCursos(cursos):
    print("\nCursos: \n")
    contador=1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2}  ({3} créditos)" 
        print(datos.format(contador, cur[0], cur[1],cur[2]))
        contador+=1
        print(" ")

def pedirDatosRegistro():
    codigo=input("Ingrese codigo: ")   
    nombre=input("Ingrese nombre: ")
    creditos=int(input("Ingrese créditos: ")) 

    curso=(codigo,nombre,creditos)
    return curso