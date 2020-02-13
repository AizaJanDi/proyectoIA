from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory #llamando a Flask
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
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
	  # obtenemos el archivo del input "archivo"
	  fArchivo = request.files['nombreArchivo']
	  
	  blob=request.files['nombreArchivo'].read()
	  longitud=len(blob)
	  #print
	  if (longitud<app.config['MAX_CONTENT_PATH']):
	  	fArchivo.save(secure_filename(fArchivo.filename))
		#fArchivo.save(os.path.join("descargas",secure_filename(fArchivo.filename)))
	  	return 'El archivo fue cargado con exito'
	  else:
	  	return 'el archivo excede la longitud'
  #filename = secure_filename(f.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  #f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  #return "Archivo subido exitosamente"
#fin subiendo archivos
#run
if __name__ == '__main__':
    app.run(debug=True)