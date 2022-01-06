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
        self.__prueba()
        return self.__velocidad

    def __prueba(self):
        """metodo privado que no puede ser accedido dentro de la misma"""
        print("esto no deberia pasar")

vehiculo1 = Vehiculo("azul","x3","4x2")
vehiculo1.velocidad = 100
print(vehiculo1.acelerar())
print(vehiculo1.acelerar())
print(vehiculo1.acelerar())
print(vehiculo1.desacelerar())