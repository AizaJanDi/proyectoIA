from flask import Flask,render_template #llamando a Flask

app = Flask(__name__)

# Creando una ruta
@app.route('/')#nombre para crear url #objeto llamado app

def home(): #ventana principal
    return render_template('home.html')

@app.route('/about')#otra ventana

def about():
    return render_template('about.html')
#run
if __name__ == '__main__':
    app.run(debug=True)