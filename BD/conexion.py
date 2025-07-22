# Importamos el conector de MySQL y la clase de manejo de errores
import mysql.connector
from mysql.connector import Error

# Definimos la clase DAO (Data Access Object) para interactuar con la base de datos
class DAO():

    # Constructor: se ejecuta automáticamente al crear una instancia de DAO
    def __init__(self):
        try:
            # Intentamos establecer la conexión a la base de datos
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='universidad'  # Nombre de la base de datos
            )
        except Error as ex:
            # En caso de error, se imprime un mensaje con la excepción
            print("Error al intentar la conexión: {0}".format(ex))

    # Método para listar todos los cursos ordenados por nombre
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()  # Creamos cursor para ejecutar SQL
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")  # Consulta SQL
                resultados = cursor.fetchall()  # Obtenemos todos los registros
                return resultados  # Devolvemos la lista de cursos
            except Error as ex:
                print("Error al listar los cursos: {0}".format(ex))

    # Método para registrar (insertar) un nuevo curso
    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # Definimos la sentencia SQL con placeholders
                sql = "INSERT INTO cursos (codigo, nombre, credito) VALUES ('{0}','{1}','{2}')"
                # Ejecutamos la sentencia SQL con los valores del curso
                cursor.execute(sql.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()  # Confirmamos los cambios
                print("¡Curso REGISTRADO!\n")
            except Error as ex:
                print("Error al intentar registrar el curso: {0}".format(ex))

    # Método para actualizar un curso existente
    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # Sentencia SQL para actualizar nombre y crédito basado en código
                sql = "UPDATE cursos SET nombre = '{0}', credito = {1} WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()  # Confirmamos los cambios
                print("¡Curso ACTUALIZADO!\n")
            except Error as ex:
                print("Error al intentar actualizar el curso: {0}".format(ex))

    # Método para eliminar un curso dado su código
    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # Sentencia SQL para eliminar curso por código
                sql = "DELETE FROM cursos WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()  # Confirmamos los cambios
                print("¡Curso ELIMINADO!\n")
            except Error as ex:
                print("Error al intentar eliminar el curso: {0}".format(ex))
