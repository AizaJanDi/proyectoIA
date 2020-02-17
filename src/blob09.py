from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename#cambia el nombre del archivo si si este es perjudicial. cambia / por _
import os
import mysql.connector
from mysql.connector import Error

UPLOAD_FOLDER=os.path.abspath("./archivos/")
ALLOWED_EXTENSIONS=set(["png", "jpg", "jpge", "gif", "pdf", "docx", "doc"])
def allowed_file(filename):
  return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
#bd

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
    #with open(os.path.normpath(filename),'rb') as f:
        binaryData = file.read()
    return binaryData

def insertBLOB(nombrArchivo):
    print("insertar BLOB en flaskprueba05"+ nombrArchivo)
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='flaskprueba05',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        filetime = os.path.basename(nombrArchivo)
        sql_insert_blob_query = """ INSERT INTO prueba03
                          (filetime, nombrArchivo) VALUES (%s,%s)"""

        empPicture = convertToBinaryData(nombrArchivo)

        # Convert data into tuple format
        insert_blob_tuple = (filetime, empPicture)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Datos insertados BLOB en flaskprueba05", result)

    except mysql.connector.Error as error:
        print("Fallo en la insercion de datos BLOB en tabla MySQL ".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL conexion finalizada")


#fin bd
@app.route('/')#nombre para crear url #objeto llamado app
def home(): #ventana principal
  return render_template('home.html')

#subiendo archivos
@app.route("/uploader", methods = ['GET','POST'])

def upload():
  if request.method == 'POST':
    if "nombreArchivo" not in request.files:#en form para enctype...
      return "El formulario no tiene parte del archivo que corresponde al formulario"
    fArchivo = request.files['nombreArchivo']
    if fArchivo.filename=="":
      return "Ningun archivo seleccionado"
    if fArchivo and allowed_file(fArchivo.filename):
      filename=secure_filename(fArchivo.filename)
      fArchivo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
      return redirect(url_for("get_file", filename=filename))
    return "Archivo no permitido"
  return "l"

@app.route("/uploaders/<filename>")

#def insertBLOBBD(filename):
#  dir=os.path.abspath(filename)
#  return insertBLOB(dir)

def get_file(filename):
  directorio=os.path.abspath(filename)
  print (directorio)
  return send_from_directory(app.config["UPLOAD_FOLDER"], filename), insertBLOB(directorio)

if __name__ == '__main__':
  app.run(debug=True)