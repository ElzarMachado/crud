#Para activar el ambinte usamos: > .venv\Scripts\activate
# Para arrancar el proyecto se usa: flask --app hello run --debug

from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pos"
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
  return render_template('index.html')

@app.route("/catalogousuarios", methods=['GET'])
def catalogoUsuarios():
    # Conexión a la base de datos:
  mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
  mycursor.execute('SELECT * FROM usuarios')
  usuarios = mycursor.fetchall()
    
    # Cerrar la conexión:
  mycursor.close()
  return render_template('catalogousuarios.html', usuarios = usuarios)

@app.route("/catalogoclientes", methods=['POST','GET'])
def catalogoClientes():
# Conexión a la base de datos:
  mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
  mycursor.execute('SELECT * FROM clientes')
  clientes = mycursor.fetchall()
    
    # Cerrar la conexión:
  mycursor.close()
  return render_template('catalogoclientes.html', clientes = clientes)


@app.route("/catalogoproductos", methods=['POST','GET'])
def catalogoProductos():
    # Conexión a la base de datos:
  mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
  mycursor.execute('SELECT * FROM productos')
  productos = mycursor.fetchall()
    
    # Cerrar la conexión:
  mycursor.close()
  return render_template('catalogoproductos.html', productos=productos)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
   # Conexión a la base de datos:
   mycursor = mydb.cursor()

    # Obtener datos de la base de datos:
   mycursor.execute('SELECT * FROM productos')
   productos = mycursor.fetchall()
    
    # Cerrar la conexión:
   mycursor.close()
    
   return render_template("menu.html")

if __name__ == '__main__':
  app.run()