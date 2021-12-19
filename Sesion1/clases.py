class Persona:
    # variables sera atributos
    # nombre = ""
    # edad= 0
    # estatura = 0.0

    # funcion sera metodo
    def saludar(self):
        print("Hola!", self.nombre)

    # constructor es el encargado de inicializar los atributos de las clases
    def __init__(self,nombre_persona,edad_persona,estatura_persona=10):
        self.nombre = nombre_persona
        self.edad = edad_persona
        self.estatura = estatura_persona
        self.sexo = "NS/NO" #valor por defecto

# cuando una variable le asignamos una clase pasa a ser una instancia
eduardo = Persona(nombre_persona="Eduardo",edad_persona=20,estatura_persona=1.89)
print(eduardo.nombre)
print(eduardo.sexo)
eduardo.sexo = "Masculino"
print(eduardo.sexo)
eduardo.saludar()