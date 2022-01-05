class Vehiculo:
    ruedas = 4
    color = "azul"

vehiculo1 = Vehiculo()
vehiculo1.ruedas = 5
# agregar atributo extra, no es buena practica.
vehiculo1.procedencia = "Japon"

vehiculo2 = Vehiculo()

print(vehiculo1.ruedas)
print(vehiculo2.ruedas)
print(vehiculo1.procedencia)

class VehiculoConConstructor():
    # en todo metodo usaremos la palabra self, se usa para referenciar
    def __init__(self,ruedas,color):
        self.ruedas = ruedas
        self.color = color
    def __str__(self):
        return f"Este Vehiculo tiene {self.ruedas} ruedas, y es de color {self.color}"

vehiculo3 = VehiculoConConstructor(4,"morado")
print(vehiculo3)