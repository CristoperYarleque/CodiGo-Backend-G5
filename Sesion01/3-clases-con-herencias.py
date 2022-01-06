from types import DynamicClassAttribute


class Vehiculo:
    """Clase que sirve para el uso de vehiculos"""
    def __init__(self,color,modelo,traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        # encapsulado el atributo velocidad, no puede ser accedido desde afuera
        self.__velocidad = 0

    def acelerar(self):
        """clase que acelera el vehiculo de 20 en 20"""
        self.__velocidad += 20
        return f"La velocidad actual es: {self.__velocidad} km/h"
    
    def desacelerar(self):
        self.__velocidad -= 20
        return self.__velocidad

    def get_velocidad(self):
        return self.__velocidad

class VehiculoVolador(Vehiculo):
    def __init__(self, color, modelo, traccion,vuela=False):
        super().__init__(color,modelo,traccion)
        self.__vuela = vuela

    def volar(self):
        self.__vuela = True

    def aterrizar(self):
        self.__vuela = True

    def estado(self):
        estado_volando = "esta volando" if self.__vuela else "esta aterrizado"
        return f"el vehiculo es de color {self.color} ,modelo {self.modelo}, su traccion es {self.traccion},la velocidad es {self.get_velocidad()}, {estado_volando}"
    


class VehiculoOffRoad(VehiculoVolador):
    def __init__(self, color, modelo, traccion, vuela=False, sumergido=False):
        super().__init__(color, modelo, traccion, vuela)

obj_vehiculo = Vehiculo("verde","rx5","4x4")
obj_vehiculo_volador = VehiculoVolador("blanco","xyz","4x2")
obj_vehiculo_volador.acelerar()
obj_vehiculo_volador.volar()
# print(obj_vehiculo_volador.vuela)
# print(obj_vehiculo_volador.color)


obj_vehiculo_offroad = VehiculoOffRoad("azul","asda","4x2")
obj_vehiculo_offroad.acelerar()
obj_vehiculo_offroad.desacelerar()
obj_vehiculo_offroad.volar()

# primero que al atributo vuela sea privado
# luego tener un metodo estado en el cual me indique cual es el 
# estado del vehiculo,color,modelo,traccion,velocidad
# si esta volando o aterrizando.
print(obj_vehiculo_volador.estado())

# isinstance() devolvera true si es que la instancia es de la clase,si esa instancia es de una clase que esta heredando de otra clase,entonces tambien sera instancia de esa clase heredada
print(isinstance(obj_vehiculo_offroad,Vehiculo))
print(isinstance(obj_vehiculo,VehiculoOffRoad))

# issubclass() devolvera true si es que la primera clase es herencia de la segunda clase
print(issubclass(VehiculoOffRoad,Vehiculo))