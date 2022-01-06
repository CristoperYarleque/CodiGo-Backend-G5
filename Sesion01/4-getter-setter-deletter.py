class Electrodomesticos:
    def __init__(self):
        self.__nombre = ""
        self.__precio = 0.0
        self.__color = ""

    def __getNombre(self):
        return self.__nombre

    def __setNombre(self,nombre):
        self.__nombre = nombre

    def __deleteNombre(self):
        del self.__nombre
    
    # propiedad de clases que sirve para indicar el comportamiento que va a tener el atributo publico en relacion del privado que hemos definido con su getter,setter,deleter
    nombre = property(__getNombre,__setNombre,__deleteNombre)

microondas = Electrodomesticos()
microondas.nombre = "Microondas"
print(microondas.nombre)
del microondas.nombre
print(microondas.nombre)