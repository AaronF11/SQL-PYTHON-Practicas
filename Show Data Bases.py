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

#Ver toddas las Bases de Datos
myCursor.execute("SHOW DATABASES")

#Ciclo for para acomodar en lista
for i in myCursor :
    print(i)