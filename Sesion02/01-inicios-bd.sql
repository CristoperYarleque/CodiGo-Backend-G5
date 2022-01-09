CREATE DATABASE pruebas;
USE pruebas;
CREATE TABLE personas(
	-- ahora definimos las columnas en esta tabla
    -- solo se puede tener una sola pk(primary-key) por tablas y solo una columna auto incrementebla
    id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT, -- solo enteros
    nombre VARCHAR(100) NOT NULL, -- caracteres hasta 100
    dni CHAR(8) UNIQUE NOT NULL, -- siempre seran 8
    fecha_nacimiento DATE, -- sera solo fecha 
    created_at DATETIME NOT NULL, -- sera fecha y hora
    sexo ENUM("MASCULINO","FEMENINO","OTRO","HELICOPTERO"), -- solo valores de parentesis
    estado BOOL -- true o false
);
-- cambiar nombre de una columna
-- ALTER TABLE personas RENAME COLUMN nombre to nombrecito;
-- agregar nueva columna
-- ALTER TABLE actividades ADD persona_id;
-- modificar columna 
-- ALTER TABLE actividades MODIFY id INT AUTO_INCREMENT PRIMARY KEY UNIQUE;

-- ingresaremos datos
-- DML LENGUAJE MANIPULACION DE DATOS (DATA MANIPULATION LANGUAJE)
-- insert: ingresar informacion a una tabla
INSERT INTO personas (id,nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 (1,"Cristoper","48874584","1991-09-10","MASCULINO",true,now());
                     
INSERT INTO personas (id,nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 (2,"Rogelio","72318863","1991-09-10","MASCULINO",true,now());
                     
INSERT INTO personas (nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 ("Ana Maria","67641863","1991-09-10","FEMENINO",true,now());
                     
INSERT INTO personas (nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 ("Patricio","24241863","1991-09-10","HELICOPTERO",true,now());
                     
-- select: leer los datos de una tabla
SELECT nombre,id FROM personas;
SELECT * from personas WHERE dni="48874584" AND nombre="Cristoper";
SELECT * from personas WHERE dni="48874584" OR nombre="Ana Maria";
SELECT * from personas ORDER BY sexo DESC;

-- DDL (DATA DEFINITION LANGUAJE) LENGUAJE DE DEFINICION DE DATOS
-- CREATE: CREAR TABLAS,BD,FUNCIONES,PROCEDIMIENTOS
-- DROP: ELIMINAR COMPLETAMENTE TODA UNA TABLA,BD,ESTRUCTURAS
-- no solo el contenido si no toda su estructura.
DROP TABLE personas;
-- eliminar contenido de tabla
DELETE FROM alumnos_cursos;
-- cambiar configuracion segura de proteccion sql
SET SQL_SAFE_UPDATES = true;

CREATE TABLE actividades(
	id INT PRIMARY KEY UNIQUE AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    intensidad ENUM("baja","media","alta","muy alta"),
    estado BOOL,
    persona_id INT,
    -- para crear relaciones
    FOREIGN KEY(persona_id) REFERENCES personas(id)
);

INSERT INTO actividades (nombre,intensidad,estado,persona_id) VALUES
						("PARRILLADAS","ALTA",true,1);
                        
INSERT INTO actividades (nombre,intensidad,estado,persona_id) VALUES
						("MANEJAR","MEDIA",false,2),
						("COCINAR","ALTA",true,1),
						("DISEÑAR","BAJA",false,3);
                        
INSERT INTO actividades (nombre,intensidad,estado) VALUES
						("PARRILLADAS","ALTA",true);
                        
SELECT * FROM personas;
-- haciendo inteserccion y comparando datos
SELECT * FROM personas INNER JOIN actividades ON personas.id = actividades.persona_id;
-- traer todas las personas pero opcional todas las actividades
SELECT * FROM personas LEFT JOIN actividades ON personas.id = actividades.persona_id;
-- traer todas las actividades pero opcional a todas las personas
SELECT * FROM personas RIGHT JOIN actividades ON personas.id = actividades.persona_id;
-- traer todas las personas y todas las actividades
SELECT * FROM personas LEFT JOIN actividades ON personas.id = actividades.persona_id UNION
SELECT * FROM personas RIGHT JOIN actividades ON personas.id = actividades.persona_id;

-- actualizar datos insertados de un tabla
UPDATE personas SET nombre="NADAR" where id=5;

-- ACTIVIDAD
-- MOSTRAR TODAS LAS PERSONAS CUYA INTENSIDAD EN LA ACTIVIDAD SEA ALTA
SELECT DISTINCT personas.nombre 
FROM actividades INNER JOIN personas 
ON actividades.persona_id = personas.id 
WHERE intensidad = "ALTA";

-- MOSTRAR TODOS LOS REGISTROS CUYO SEXO SEA MASCULINO o SU ESTADO DE LA ACTIVIDAD SEA true
SELECT * 
FROM actividades INNER JOIN personas 
ON actividades.persona_id = personas.id 
WHERE personas.sexo = "MASCULINO"
OR actividades.estado = true;

-- MOSTRAR LAS PERSONAS QUE NO TENGAN ACTIVIDADES SOLAMENTE SU NOMBRE Y ID
SELECT personas.nombre,personas.id 
FROM personas LEFT JOIN actividades 
ON personas.id = actividades.persona_id 
WHERE actividades.persona_id IS NULL;

-- sub-consulta
select nombre,id from personas where id not in (select persona_id from actividades WHERE persona_id is not null);


