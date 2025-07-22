import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='universidad'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al listar los cursos: {0}".format(ex))

    def registrarCurso(self,curso):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="INSERT INTO cursos (codigo, nombre, credito) VALUES ('{0}','{1}','{2}')"
                cursor.execute(sql.format(curso[0], curso[1],curso[2]))
                self.conexion.commit()
                print("¡Curso REGISTRADO!\n")
            except Error as ex:
                print("Error al intentar la conexión:{0}".format(ex))
    
    def actualizarCurso(self,curso):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="UPDATE cursos SET nombre = '{0}', credito = {1} where codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2],curso[0]))
                self.conexion.commit()
                print("¡Curso ACTUALIZADO!\n")
            except Error as ex:
                print("Error al intentar la conexión:{0}".format(ex))

    def eliminarCurso(self,codigoCursoEiminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sql="DELETE FROM cursos WHERE codigo = '{0}' "
                cursor.execute(sql.format(codigoCursoEiminar))
                self.conexion.commit()
                print("¡Curso ELIMINADO!\n")
            except Error as ex:
                print("Error al intentar la conexión:{0}".format(ex))
