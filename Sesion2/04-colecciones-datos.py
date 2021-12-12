# LISTAS
dias = ["Lunes","Martes","Miercoles"]

dias.append("Jueves") #agregar nuevo valor al final
# print(dias)

dias.remove("Martes") #eliminar valor por contenido o posicion[0]
# print(dias)

dias.clear() #borrar la lista
# print(dias)

otros_dias = ["Sabado","Domingo"]

dias_semana = dias + otros_dias
dias_semana1 = [dias,otros_dias]
# print(dias_semana)
# print(dias_semana1)

# TUPLAS
# coleccion igual que la lista PERO la tupla no se puede modificar sus valores
alumnos = ("Eduardo","Pedro","Ana","Roberto") #valores primitivos que nunca cambiaran
CONFIGURACION = ( #colecion de datos dentro de tupla que si modifica
    {
        "Nombre":"API_KEY",
        "Valor":"xxxx.xxxx.xxxx"
    },{
        "Nombre":"Sengrid",
        "Valor":"adadasdas"
    }
)
# alumnos[0] = "Juan" #no cambia
CONFIGURACION[0]["Nombre"] = "XD" #si cambia

# DICCIONARIOS
# coleccion de elementos indexados , se puede modificar, se puede crear nuevas llaves

persona = {
    "nombre" : "Cristoper",
    "correo" : "caypsaturno@gmail.com",
    "direcciones" : [
        {
            "calle":"xxxx 1234",
            "dpto" : "arequipa"
        },
        {
            "calle" : "yyyy 4567",
            "dpto" : "lima"
        }
    ],
    "est_civil" : "soltero"
}
persona["estatura"] = "1.95"

print(persona.keys()) #saber las llaves
print(persona.values()) #saber el contenido

# CONJUNTOS
# coleccion de datos DESORDENADA,si permite agregar valores
colores = {"rojo","verde","amarillo","azul"}
colores.add("mostaza") #agregar en conjuntos
# print(colores)

# VARIABLES MUTABLES Y NO MUTABLES
# mutables todo tipo de colecciones
lista1 = [1,2,3,4,5]
lista2 = lista1

lista3 = lista1[:] #evita que sea mutable [:]

lista1[0] = 50

# print(id(lista1))
# print(id(lista2))
# print(id(lista3))
# print(lista1)
# print(lista2)
# print(lista3)

# no mutables tipo primitivo INT,STR,FLOAT,BOOLEAN,DATE
nombre1 = "Cristoper"
nombre2 = nombre1
nombre1 = "Andy"

# print(nombre1)
# print(nombre2)

