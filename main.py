from os import system
from msvcrt import getch
from progress.bar import ChargingBar, Bar
import time
import random
import mysql.connector as sql
Connection = sql.connect(
    host='localhost',
    user='aaron',
    passwd='1234',
    database='registro')

print("\nCONEXIÓN EXITOSA : ",Connection)

#Crear cursor
myCursor = Connection.cursor()


def text():
    print('''
                        OPCIONES                        CODIGO
            |------------------------------|----------------------------|
            |       REGRESAR AL MENU       |              1             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            |        CERRAR PROGRAMA       |              0             |
            |------------------------------|----------------------------|
                ''')

def question(code):
    if code == 0:
        exit(0)

def code_1():
    print('''
                        OPCIONES                        CODIGO
            |------------------------------|----------------------------|
            |    INSERTAR UNICO REGISTRO   |              1             | 
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            |    INSERTAR MÁS REGISTROS    |              2             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            | INSERTAR REGISTROS Y GUARDAR |              3             |
            |  EN UN ARCHIVO EL REGISTRO   |                            |
            |------------------------------|----------------------------|
                ''')

def code_2():
    print('''
                        OPCIONES                        CODIGO
            |------------------------------|----------------------------|
            |    ELIMINAR UNICO REGISTRO   |              1             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            |         ELIMINAR TODO        |              2             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            | ELIMINAR REGISTROS Y BORRAR  |              3             |
            |    EL ARCHIVO EL REGISTRO    |                            |
            |------------------------------|----------------------------|
                ''')

print('''
            *************************************************************
            *                                                           *
            *                 BASE DE DATOS - REGISTRO                  *
            *                                                           *
            *************************************************************
''')

while True:
    print('''
                        OPCIONES                        CODIGO
            |------------------------------|----------------------------|
            |   INSERTAR NUEVO REGISTRO    |              1             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            |  ELIMINAR REGISTRO EXISTENTE |              2             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            |  MOSTRAR REGISTRO EXISTENTE  |              3             |
            |------------------------------|----------------------------|
            |------------------------------|----------------------------|
            |        CERRAR PROGRAMA       |              0             |
            |------------------------------|----------------------------|
        ''')

    code = int(input('==> '))
    if code == 0:
        break

    elif code == 1:
        code_1()        
        code = int(input('==> '))
        if code == 1:
            print('\n--- INSERTAR DATOS ---\n')

            #Insertar datos
            print('INGRESA LA MATRICULA : ')
            enrollment = str(input('==> '))
            print('INGRESA EL NOMBRE : ')
            name = str(input('==> ')).upper()
            print('INGRESA LOS APELLIDOS : ')
            lastnames = str(input('==> ')).upper()
            print('INGRESA EL CORREO INSTITUCIONAL : ')
            mail = str(input('==> ')).lower()

            table = "INSERT INTO `datos` (`MATRICULA`, `NOMBRE`, `APELLIDOS`, `CORREO INSTITUCIONAL`) VALUES (%s, %s, %s, %s)"
            values = (enrollment , name, lastnames, mail)

            myCursor.execute(table, values)

            bar = ChargingBar('GUARDANDO REGISTRO:', max=100)
            for num in range(100):
                time.sleep(random.uniform(0, 0.10))
                bar.next()
            bar.finish()

            #Guardar cambios
            Connection.commit()

            text()
            code = int(input('==> '))
            question(code)
            system('cls') 

        if code == 2:
            print('INGRESA LA CANTIDAD DE REGISTROS A INGRESAR : ')
            loops = int(input('==> '))

            for i in range(loops):
                
                print('\n--- INSERTAR DATOS ---\n')

                #Insertar datos
                print('INGRESA LA MATRICULA : ')
                enrollment = str(input('==> '))
                print('INGRESA EL NOMBRE : ')
                name = str(input('==> ')).upper()
                print('INGRESA LOS APELLIDOS : ')
                lastnames = str(input('==> ')).upper()
                print('INGRESA EL CORREO INSTITUCIONAL : ')
                mail = str(input('==> ')).lower()

                table = "INSERT INTO `datos` (`MATRICULA`, `NOMBRE`, `APELLIDOS`, `CORREO INSTITUCIONAL`) VALUES (%s, %s, %s, %s)"
                values = (enrollment , name, lastnames, mail)

                myCursor.execute(table, values)
                
                bar = ChargingBar('GUARDANDO REGISTROS:', max=100)
                for num in range(100):
                    time.sleep(random.uniform(0, 0.10))
                    bar.next()
                bar.finish()

                #Guardar cambios
                Connection.commit()

            text()
            code = int(input('==> '))
            question(code)
            system('cls')
        
        if code == 3:
            print('INGRESA LA CANTIDAD DE REGISTROS A INGRESAR : ')
            loops = int(input('==> '))
            
            for i in range(loops):
                
                print('\n--- INSERTAR DATOS ---\n')

                #Insertar datos
                print('INGRESA LA MATRICULA : ')
                enrollment = str(input('==> '))
                print('INGRESA EL NOMBRE : ')
                name = str(input('==> ')).upper()
                print('INGRESA LOS APELLIDOS : ')
                lastnames = str(input('==> ')).upper()
                print('INGRESA EL CORREO INSTITUCIONAL : ')
                mail = str(input('==> ')).lower()
                
                file = open('Register.txt', 'a')
                include_enrollment = 'MATRICULA: ' + enrollment
                include_name = 'NOMBRE : ' + name
                include_lastnames = 'APELLIDOS : ' + lastnames
                include_mail = 'CORREO INSTITUCIONAL : ' + mail
                file.write(include_enrollment)
                file.write(', ')
                file.write(include_name)
                file.write(', ')
                file.write(include_lastnames)
                file.write(', ')
                file.write(include_mail)
                file.write('\n')
                file.close()

                table = "INSERT INTO `datos` (`MATRICULA`, `NOMBRE`, `APELLIDOS`, `CORREO INSTITUCIONAL`) VALUES (%s, %s, %s, %s)"
                values = (enrollment , name, lastnames, mail)

                myCursor.execute(table, values)

                bar = ChargingBar('GUARDANDO REGISTROS:', max=100)
                for num in range(100):
                    time.sleep(random.uniform(0, 0.10))
                    bar.next()
                bar.finish()

                #Guardar cambios
                Connection.commit()

            text()
            code = int(input('==> '))
            question(code)
            system('cls')

    elif code == 2:
        code_2()        
        code = int(input('==> '))
        if code == 1:
            delete = "DELETE FROM datos WHERE MATRICULA = %s"
            print('INGRESA LA MATRICULA : ')
            enrollment = str(input('==> '))
            
            adr = (enrollment, )

            myCursor.execute(delete, adr)

            bar = Bar('ELIMINANDO REGISTRO:', max=100)
            for num in range(100):
                time.sleep(0.10)
                bar.next()
            bar.finish()

            Connection.commit()

            print('\n--- REGISTRO ELIMINADO CON EXITO ---')

            print('\n### PARA CONTINUAR TECLEA - ENTER - ###')
            getch()
            system('cls')

        elif code == 2:
            myCursor.execute("TRUNCATE datos")

            bar = Bar('ELIMINANDO REGISTROS:', max=100)
            for num in range(100):
                time.sleep(0.10)
                bar.next()
            bar.finish()

            print('--- REGISTROS DE LA BASE DE DATOS ELIMINADOS CON EXITO ---')

            print('\n### PARA CONTINUAR TECLEA - ENTER - ###')
            getch()
            system('cls')

        elif code == 3: 
            myCursor.execute("TRUNCATE datos")
            bar = Bar('ELIMINANDO REGISTROS DE LA BASE DE DATOS:', max=100)
            for num in range(100):
                time.sleep(0.10)
                bar.next()
            bar.finish()
            print('--- REGISTROS DE LA BASE DE DATOS ELIMINADOS CON EXITO ---')
            file = open('Register.txt', 'w')
            file.truncate()
            file.close()
            bar = Bar('ELIMINANDO REGISTROS DEL ARCHIVO LOCAL:', max=100)
            for num in range(100):
                time.sleep(0.10)
                bar.next()
            bar.finish()
            print('--- REGISTROS DEL ARCHIVO LOCAL ELIMINADOS CON EXITO ---')

            print('\n### PARA CONTINUAR TECLEA - ENTER - ###')
            getch()
            system('cls')


    elif code == 3:
        bar = ChargingBar('RECOPILANDO REGISTROS:', max=100)
        for num in range(100):
            time.sleep(random.uniform(0, 0.10))
            bar.next()
        bar.finish()
        print('\n--- REGISTROS CAPTURADOS EN LA BASE DE DATOS ---\n')
        print('##### TABLAS #####')
        myCursor.execute("SHOW TABLES")
        for table in myCursor:
            print(table)
        print('##### REGISTROS #####')
        myCursor.execute("SELECT * FROM `datos`")
        for records in myCursor:
            print(records)
        print('\n--- REGISTROS CAPTURADOS EN ARCHIVO LOCAL ---\n')
        file = open('Register.txt')
        print(file.read())

        print('\n### PARA CONTINUAR TECLEA - ENTER - ###')
        getch()
        system('cls')

    else:
            print('### ERROR - CÓDIGO NO VALIDO ###')  