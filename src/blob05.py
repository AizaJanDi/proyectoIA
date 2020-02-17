import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(emp_id, nombrArchivo):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='flaskprueba03',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO prueba03
                          (id, nombrArchivo) VALUES (%s,%s)"""

        empPicture = convertToBinaryData(nombrArchivo)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, empPicture)
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

insertBLOB(2, "D:\downloadjhan\muevodb2.txt")