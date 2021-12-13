# Condicional IF ELSE y ELIF
edad = 30
edad_minima = 18

if edad >= edad_minima:
    print("eres mayor de edad, puedes ingresar")
elif edad > 15:
    print("puedes ingresar solo a los quinceañeros")
elif edad > 10:
    print("puedes ingresar al zoo gratis")
else:
    print("eres menor de edad, no puedes ingresar")

# Operador Ternario
# devolver valor y almacenar en variable

print("eres mayor de edad") if edad >= edad_minima else print("eres menor de edad")

resultado = "eres mayor de edad" if edad >= edad_minima else "eres menor de edad"
print(resultado)

# siguiente numero
numero = 10
# saber si es par

if numero % 2 == 0 :
    print("es par")
else:
    print("es impar")

resultado1 = "es par" if numero % 2 == 0 else "es impar"
print(resultado1)

persona = {
    "nombre" : "Raul",
    "nacionalidad" : "Ecuatoriana",
    "sexo" : "M"
}

# validad si es Raul y es Peruana

if persona["nombre"] == "Raul" and persona["nacionalidad"] == "Peruana":
    print(f'SI, la persona es {persona["nombre"]} y su nacionalidad es {persona["nacionalidad"]}')
else:
    print(f'NO, la persona es {persona["nombre"]} y su nacionalidad es {persona["nacionalidad"]}')

# FOR sirve para iterar
meses = ["Enero","Febrero","Marzo","Abril"]
for mes in meses:
    if mes == "Enero":
        print("vamos a la playa, es",mes)
    print(mes)

for mes in meses[:1]: #desde la posicion 1 hasta el final
    print(mes)

#puede ser varios rangos ejm (5,10) hasta 3 parametros
# range siempre recibe numeros
# range(n) => el limite <n
# range(n,m) => n inicio, m el limite (<m)
# range(n,m,o) => n inicio, m el limite(<m), o cuanto suma cada ciclo
for numero in range(10): 
    print(numero)

# imprime las posiciones len()=sacar longitud de variable
# convertir a entero int()
# convertir a string str()
# convertir a float float()
# convertir a booleano bool()
for numero in range(len(meses)):#longitud de todos los meses
    print(numero) #posicion

for numero in range(int(len(meses)/2),len(meses)):#ir desde la mitad al final
    print(numero) #posicion
    print(meses[numero]) #valor de la posicion

# TAREAAA
personas = [
    {
        "nombre" : "Adriana",
        "edad" : 25
    },
    {
        "nombre" : "Nicolas",
        "edad" : 15
    },
    {
        "nombre" : "Maria",
        "edad" : 23
    },
    {
        "nombre" : "Guillermo",
        "edad" : 10
    }
]
# 1. Cuantas personas tienen mas de 20 años (numero).
# 2. Que personas tienes menos de 20 años (nombre)
# HINT: crear una lista donde se almacene nombres a las personas que tienen menos de 20 años, y contador a las personas de mas de 20 años

# parametro end modifica el salto de linea
print("aaaaaaa",end="")
print("bbbbbb")