from faker import Faker
from faker.providers import person,internet
objFaker = Faker()
objFaker.add_provider(person)
objFaker.add_provider(internet)

# print(objFaker.first_name_nonbinary())
# print(objFaker.free_email())
# print(objFaker.name())

cursos = ['COMUNICACION', 'CTA', 'INGLES', 'FRENCH']

for curso in cursos:
    print(f"INSERT INTO CURSOS (nombre) values ('{curso}');")


for i in range(1,100):
    nombre = objFaker.first_name()
    apellido = objFaker.last_name()
    correo = objFaker.free_email()
    print(f"INSERT INTO ALUMNOS (nombre,apellido,correo) VALUES('{nombre}','{apellido}','{correo}');")

# hacer un for 200 veces encontrar un numero ramdon entre 1 y 100(seria el alumno)
# luego un ramdon entren el 1 y 4 para cursos

print(f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES(1,3);')
print(f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES(10,1);')
print(f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES(10,2);')
print(f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES(32,1);')
print(f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES(55,4);')
print(f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES(86,3);')