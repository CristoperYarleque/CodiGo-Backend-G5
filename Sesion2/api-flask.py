from flask import Flask, request
# request nos da toda la informacion del cliente

app = Flask(__name__)
# si solamente le pasamos la aplicacion o la instancia de flask habilitara
# los cors para todos los dominios y todos los metodos
CORS(app=app)

misProductos = [
    {
    "nombre" : "Paneton con arto bromato",
    "precio" : 17.50,
    "disponible" : True,
    "fecha_vencimiento" : "2022-01-04"
},
{
    "nombre" : "Chocolate con arta azucar",
    "precio" : 6.90,
    "disponible" : False,
    "fecha_vencimiento" : "2021-12-30"
}
]

@app.route("/",methods=["POST","GET"])
def inicio():
    # request.method nos da el metodo que esta queriendo acceder el cliente
    print(request.method)
    if request.method == "POST":
        # request.get_json() captura el json y lo convierte a diccionario
        print(request.get_json())
        data = request.get_json()

        # validar nombre , si hay retornar saludo, si no pedir informacion con estado(400)
        # metodo get() sirve para extraer informacion de un diccionario
        # si no existe retorna vacio o null, adicional
        # como segundo parametro se puede indicar el valor
        if data.get("nombre"):
            nombre = data["nombre"]
            return "Hola, {}!".format(nombre)
        else:
            return "Necesito la Informacion",404

    elif request.method == "GET":
        return "Bienvenido a mi API de Productos",200

@app.route("/productos",methods=["GET","POST"])
def productos():
    if request.method == "GET":
        return {
            "data" : misProductos,
            "message" : "Los productos son:",
            "ok" : True
        }, 200
    elif request.method == "POST":
        data = request.get_json()
        misProductos.append(data) #simular insertando registro en una bd
        return {
            "data" : data,
            "message" : "Productos agregado exitosamente",
            "ok" : True
        }, 201
        
# al ponerle el tipo de dato que podemos aceptar y si el momento de enviar
# no es ese tipo de dato entonces se rechazan automaticamente la peticion
# con un estado 404
@app.route("/producto/<int:id>",methods=["GET","PUT"])
def producto(id):
    if request.method == "GET":
        if id < len(misProductos):
            return {
                "ok" : True,
                "data" : misProductos[id],
                "message" : "EL producto es:"
            }
        else:
            return {
                "ok" : False,
                "data" : None,
                "message" : "El producto no existe"
            }

        # recibir el id que vendria a ser la posicion de la lista y dar el producto a buscar,
        # si no exites dar mensaje que no existe el producto
        # {
        # "data" : null,
        # "message" : "el producto no existe",
        # "ok:False
        # }
        # si existe entonces dar el producto
    elif request.method == "PUT":
        data = request.get_json()
        if id < len(misProductos):
            misProductos[id] = data #sobreescribir informacion en esa posicion
            return {
                "ok" : True,
                "data" : misProductos[id],
                "message" : "Producto actualizado exitosamente"
                }, 201
        else:
            return {
                "ok" : False,
                "data" : None,
                "message" : "El producto con el id {} no existe".format(id)
            }

if __name__ == "__main__":
    app.run(debug=True)

