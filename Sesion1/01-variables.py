# variable numerica
numero = 10 
numero2 = 10.5

# variable de texto o string
# numero = "Febrero"

nombre = "Cristoper"
apellido = "Yarleque"

fecha = 0

soltero = True

# print("holaaa :)")
# print(type(numero))

# str = string
# int = integer
# float = float
# bool = boolean}

# VARIABLES que tienen varios VALORES
# ARREGLOS ARRAY > LISTA LIST
edades = [10,12.40,60,"cristoper",14.5,False,[1,2]]
# print(edades[-1]) reversa
# print(edades[0]) 
# print(edades[2:4]) rangos
# print(edades[:3]) hasta
# print(edades[2:]) desde

# JSON (JavaScript Object Notation)  Diccionario 
curso = {
    "nombre" : "Backend",
    # "nombre" : "Frontend",
    "dificultad" : "Dificil",
    "skills" : [
        {
            "nombre" : "Base de datos",
            "nivel" : "Intermedio"
        },
        {
            "nombre" : "ORM",
            "nivel" : "Avanzando"
        }
    ]
}
# print(curso["skills"][1]["nivel"])

# destructuring
[primero,segundo,tercero,cuarto,quinto] = ["Enero","Febrero","Marzo","Abril","Mayo"]
# print(segundo)

personas = [{
    "nombre" : "Cristoper",
    "nacionalidad" : "peruano",
    "hobbies" : [
        {
            "nombre" : "Volar drones",
            "experiencia" : "2 años"
        },{
            "nombre" : "Programar",
            "experiencia" : "1 mes"
        }
    ]
},{
    "nombre" : "Juliana",
    "nacionalidad" : "colombiana",
    "hobbies" : [
        {
            "nombre" : "Montar bici",
            "experiencia" : "4 años"
        },{
            "nombre" : "Bases de datos",
            "experiancia" : "8 meses"
        }
    ]
}
]
del personas[0] #eliminar variable , contenido
# print(personas)

# nacionalidad primera persona
# print(personas[0]["nacionalidad"])

# hobbies segunda persona
# print(personas[1]["hobbies"])
# print(personas[1]["hobbies"][0]["nombre"])
# print(personas[1]["hobbies"][1]["nombre"])

# experiencia hobbie primera persona
# print(personas[0]["hobbies"][1]["experiencia"])