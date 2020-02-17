from flask import Flask, flash,render_template, request, redirect, url_for, send_from_directory,flash
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
#import mysql.connector
#from mysql.connector import Error
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "archivos"
#app.config['MAX_CONTENT_PATH']=1000000
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskprueba03'
mysql=MySQL(app)

@app.route('/')#nombre para crear url #objeto llamado app
def home(): #ventana principal
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM prueba03')
    data = cur.fetchall()
    cur.close()
    return render_template('home.html', prueba03 = data)

@app.route('/about')#otra ventana
def about():
    return render_template('about.html')
#subiendo archivos
@app.route("/uploader", methods = ['GET','POST'])

def upload_file():
    if request.method == 'POST':
        fArchivo = request.files['nombreArchivo']
        fArchivo.save(os.path.join('archivos',secure_filename(fArchivo.filename)))
        #fArchivo=open(fArchivo,'rb')
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO prueba03 (nombrArchivo) VALUES (%s)", (fArchivo))
        mysql.connection.commit()
        #return redirect(url_for('blob04'))

if __name__ == '__main__':
    app.run(debug=True)