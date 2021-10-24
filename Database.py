#Importar librerias para errores de logging y conector mysql
from logging import error 
import mysql.connector as mysql

#Crear una conexión
Connection = mysql.connect(
    host='localhost',
    user='aaron',
    password='1234'
)

#Crear un cursor
myCursor = Connection.cursor()

#Crear una Base de Datos
myCursor.execute("CREATE DATABASE registro")

#Nota: una vez creada la base de datos ya no volver a ejecutar este código 