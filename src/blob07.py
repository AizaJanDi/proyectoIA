import mysql.connector
from mysql.connector import Error
import os
import time
from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory #llamando a Flask
from werkzeug.utils import secure_filename
import pdb

app = Flask(__name__)
@app.route('/')#nombre para crear url #objeto llamado app
def home(): #ventana principal
    return render_template('home.html')

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData
@app.route("/uploader", methods = ['GET','POST'])

def insertBLOB():
    fArchivo = request.files['nombreArchivo']
    fArchivo.save(os.path.join('archivos',secure_filename(fArchivo.filename)))
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
        database='flaskprueba05',
        user='root',
        password='')

        cursor = connection.cursor()
        filetime = os.path.basename(fArchivo)
        sql_insert_blob_query = """ INSERT INTO prueba03
            (filetime, nombrArchivo) VALUES (%s,%s)"""

        empPicture = convertToBinaryData(nombrArchivo)

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

def upload_file():
    if request.method == 'POST':
        fArchivo = request.files['nombreArchivo']
        fArchivo.save(os.path.join('archivos',secure_filename(fArchivo.filename)))

if __name__ == '__main__':
    app.run(debug=True)

