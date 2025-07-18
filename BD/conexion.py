import mysql.connector
from mysql.connector import Error

class DAO():

    def _init_(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port = 3306,
                user='root',
                password='',
                db='universidad'
            )
        except Error as ex :
            print("Error al intentar la Conexión {0}".format(ex))

            def listarCursos(self):
                if self.conexion.is_connected();
                    try:
                        cursor=self.conexion.cursor()
                        cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                        resultados=cursor.fetchall()
                        return resultados
                    except  Error as ex:
                        print ("Error al intentar la conexión: {0}".format)