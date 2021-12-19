from flask import Flask

# tenemos varias variables que son de uso propio de python no se puede modificar
# esta variable sirve para indicar si estamos archivo principal del proyecto
app = Flask(__name__)

@app.route("/")
def inicio():
    return {"lista":"lista","valor":2}

@app.route("/bienvenido")
def bienvenido():
    return "Bienvenido a bienvenido API"

@app.route("/bienvenido/home")
def bienvenido_home():
    return "Bienvenido a bienvenido_home API"

if __name__ == "__main__":
    app.run(debug=True,port=3000)
