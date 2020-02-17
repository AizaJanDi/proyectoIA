import mysql.connector
from mysql.connector import Error
import os
import time

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        
        binaryData = file.read()
    return binaryData

def insertBLOB(nombrArchivo):
    print("Inserting BLOB into python_employee table"+nombrArchivo)#D:\downloadjhan\muevodb2.txt 
                                                                   #C:\Users\Equipo\Downloads\PYTHONWEB\proyectoIA\src\wow.svg.png
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='flaskprueba05',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        filetime = os.path.basename(nombrArchivo)
        sql_insert_blob_query = """ INSERT INTO prueba03
                          (filetime, nombrArchivo) VALUES (%s,%s)"""
        print("archivo2"+nombrArchivo)
        empPicture = convertToBinaryData(nombrArchivo)
        print(empPicture)
        # Convert data into tuple format
        insert_blob_tuple = (filetime, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB("D:\downloadjhan\muevodb2.txt")
