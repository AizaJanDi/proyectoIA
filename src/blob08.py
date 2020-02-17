from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename#cambia el nombre del archivo si si este es perjudicial. cambia / por _
import os
UPLOAD_FOLDER=os.path.abspath("./archivos/")
ALLOWED_EXTENSIONS=set(["png", "jpg", "jpge", "gif", "pdf", "docx", "doc"])
def allowed_file(filename):
  return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS
app = Flask(__name__)
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER
# Creando una ruta
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
def get_file(filename):
  return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == '__main__':
  app.run(debug=True)