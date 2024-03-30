from flask import Flask, render_template, request
import mysql.connector

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '',
    'database': 'onpe'
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(dictionary=True)
app = Flask(__name__)

#INDEX ----------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actas_ubigeo')
def actas_Ubigeo():
    return render_template('actas_ubigeo.html')

@app.route('/actas_numero')
def actas_Numero(): 
    return render_template('actas_numero.html')

@app.route('/participacion')
def participacion():
    return render_template('participacion.html')

@app.route('/participacion_total/<id>')
def participacion_total(id):
    return render_template('participacion_total.html')
#INDEX ----------------------------------------------------------------

#POST ----------------------------------------------------------------
@app.route('/actas_numero/<int:id>', methods=["POST"])
def pst_numero(id):
    numero_mesa = request.form['nroMesa']
    print(numero_mesa)
    return render_template('actas_numero.html')
#POST ----------------------------------------------------------------

if __name__ == '__main__':
    app.run(port=5000, debug=True)