from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory #llamando a Flask
#from werkzeug import secure_filename
from werkzeug.utils import secure_filename
#Para BD
from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL

#Fin para BD
import os
app = Flask(__name__)
# Configurar ruta de descargas
app.config['UPLOAD_FOLDER'] = "archivos"
app.config['MAX_CONTENT_PATH']=1000000
#Para BD
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskprueba01'
mysql=MySQL(app)
#Fin para BD

# Creando una ruta
@app.route('/')#nombre para crear url #objeto llamado app
def home(): #ventana principal
    return render_template('home.html')
#agregar inf a BD
@app.route('/add_contact', methods=['POST'])
def add_contact():
	if	request.method=='POST':
		nombreArchivo=request.form['nombreArchivo']
	return 'recibido'
#fin agregar inf a BD

@app.route('/about')#otra ventana

def about():
    return render_template('about.html')
#subiendo archivos
@app.route("/uploader", methods = ['GET','POST'])

def upload_file():
	if request.method == 'POST':
	  #print
	  	if (longitud<app.config['MAX_CONTENT_PATH']):
	  		fArchivo.save(secure_filename(fArchivo.filename))#por que así? no ees su else? crei que no da asi en python
		#fArchivo.save(os.path.join("descargas",
	  # obtenemos el archivo del input "archivo"

	  		fArchivo = request.files['nombreArchivo']
	  	#nuevo
		  	filenames = os.path.basename(fArchivo)
			for r, d, f in os.walk("c:\\"):
				for files in f:
					if files == filenames:
						print (os.path.join(r,files))
		#nuevo
		  	blob=request.files['nombreArchivo'].read()
		  	longitud=len(blob)secure_filename(fArchivo.filename)))#es el no oficial, ya limpie el codigo en blob07
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
    # que no es el mismo? F o V : R=