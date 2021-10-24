#Importar librerias para errores de logging y conector mysql
from logging import error 
import mysql.connector as mysql

#Crear una conexión
Connection = mysql.connect(
    host='localhost',
    user='aaron',
    password='1234',
    database='registro'
)

#Crear un cursor
myCursor = Connection.cursor()

#Crear tabla en la Base de Datos
myCursor.execute("CREATE TABLE `DATOS` ( `MATRICULA` VARCHAR(7) NOT NULL , `NOMBRE` VARCHAR(150) NOT NULL , `APELLIDOS` VARCHAR(150) NOT NULL , `CORREO INSTITUCIONAL` VARCHAR(150) NOT NULL ) ENGINE = InnoDB")

#Nota: una vez creada la tabla ya no volver a ejecutar este código