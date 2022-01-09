CREATE DATABASE colegio;
USE colegio;
CREATE TABLE alumnos(
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
	nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(50) NOT NULL
);
CREATE TABLE cursos(
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
    nombre VARCHAR(100) NOT NULL
);
CREATE TABLE alumnos_cursos(
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE NOT NULL,
	alumno_id INT,
    curso_id INT,
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

SELECT * FROM alumnos;

-- funciones de agregacion (aggregation function)
-- avg(columna) => da el promedio de una columna numerica
-- max(columna) => traera el valor maximo de resultados
-- min(columna) => traera el valor minimo
-- count(columna) => puede ser numero o strings
-- sum(columna) => solo numericos, traera la suma de dicha columna
-- first(columna) => traera el primer valor
-- last(columna) => traera el ultimo valor
SELECT avg(id) FROM alumnos WHERE id BETWEEN 1 AND 2; -- ENTRE 1 HASTA 2
SELECT MAX(id) FROM alumnos;
-- contador , el GROUP BY agrupa y luego cuenta, ORDER BY ordenar
SELECT count(nombre), nombre FROM alumnos GROUP BY nombre
ORDER BY count(nombre) desc , nombre asc;
-- buscar coincidencias LIKE, BUSCAR ANTES DESPUES O ENTRE % (solo string)
SELECT * FROM cursos WHERE nombre LIKE "%A%O%";

-- orden de escritura select
-- SELECT col..
-- FROM tablas[JOINS]
-- WHERE condicionales
-- GROUP BY col...
-- ORDER BY col...

use colegio;
select * from alumnos_cursos;
select * from django_session;
DELETE FROM django_session;
CREATE DATABASE blog;