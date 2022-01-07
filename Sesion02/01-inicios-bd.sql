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
-- ALTER TABLE actividades ADD persona_id

-- ingresaremos datos
-- DML LENGUAJE MANIPULACION DE DATOS (DATA MANIPULATION LANGUAJE)
-- insert: ingresar informacion a una tabla
INSERT INTO personas (id,nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 (1,"Cristoper","48874584","1991-09-10","MASCULINO",true,now());
                     
INSERT INTO personas (id,nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 (2,"Rogelio","72318863","1991-09-10","MASCULINO",true,now());
                     
INSERT INTO personas (nombre,dni,fecha_nacimiento,sexo,estado,created_at) VALUES
					 ("Ana Maria","67641863","1991-09-10","FEMENINO",true,now());
                     
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
                        
SELECT * FROM actividades