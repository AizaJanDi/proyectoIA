from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory #llamando a Flask
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
#Para BD
from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL

import mysql.connector
from mysql.connector import Error
#Fin para BD
#Fin para BD
import os
app = Flask(__name__)
# Configurar ruta de descargas
app.config['UPLOAD_FOLDER'] = "archivos"
app.config['MAX_CONTENT_PATH']=1000000

# Creando una ruta
@app.route('/')#nombre para crear url #objeto llamado app
def home(): #ventana principal
    return render_template('home.html')

@app.route('/about')#otra ventana

def about():
    return render_template('about.html')
#subiendo archivos
@app.route("/uploader", methods = ['GET','POST'])

def upload_file():
  if request.method == 'POST':
    fArchivo = request.files['nombreArchivo']
    fArchivo.save(os.path.join('archivos',secure_filename(fArchivo.filename)))
    insertBLOB(fArchivo)
    return 'sip'
  return render_template('upload.html')
#------ARCHIVOS A BD------#
#convertir archivo a binario
def convertToBinaryData(fArchivo):
    #with open(filename, 'rb') as file:
    #    binaryData = file.read()
    archivo=open(fArchivo,'rb')
    binaryData=archivo.read()
    return binaryData

#insertar archivos
def insertBLOB(fArchivo):

    print("insertar BLOB en tabla flaskprueba03")
    global connection
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='flaskprueba03',
                                             user='root',
                                             password='')

        cursor = connection.cursor()
        insertarEnBD= """ INSERT INTO prueba03
                          (nombreArchivo) VALUES (%s)"""

        #empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(fArchivo)

        # Convert data into tuple format
        insertBlobTupla = (file)
        result = cursor.execute(insertarEnBD, insertBlobTupla)
        connection.commit()
        print("Archivo insertado BLOB en tabla flaskprueba03", result)

    except mysql.connector.Error as error:
        print("Insercion fallida".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Fin de conexion")
#------ARCHIVOS A BD------#
#---------insert-------------#
#insertBLOB(1, "D:\downloadjhan\muevodb1.txt")
#insertBLOB(2, "D:\downloadjhan\muevodb2.txt")
#run
if __name__ == '__main__':
    app.run(debug=True)