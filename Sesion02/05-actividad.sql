-- 1. todas los alumnos que comiencen la letra a y tengan una c
-- 2. mostrar cuantas alumnos tienen como correo @hotmail.com
-- 3. traer todos los alumnos que lleven comunicacion (id=1)
-- 4. contabilizar cuantos alumnos hay de cada curso
 
 -- actividad 1
SELECT * FROM alumnos WHERE nombre LIKE "A%C%";
-- actividad 2- distintas formas
SELECT count(*) FROM alumnos WHERE correo LIKE "%@hotmail.com";
SELECT count(*) 'conteo','alumnos' texto FROM ALUMNOS WHERE correo like '%@hotmail.com';
-- actividad 3- distintas formas
SELECT * FROM alumnos INNER JOIN alumnos_cursos ON alumnos.id = alumnos_cursos.alumno_id WHERE curso_id = 1;
SELECT * FROM alumnos as a inner join alumnos_cursos as ac ON a.id = ac.alumno_id WHERE curso_id = 1;
-- actividad 4
SELECT cursos.nombre,count(alumnos_cursos.curso_id) 
FROM alumnos INNER JOIN alumnos_cursos 
ON alumnos.id=alumnos_cursos.alumno_id 
INNER JOIN cursos ON  alumnos_cursos.curso_id=cursos.id
GROUP BY cursos.nombre
ORDER BY 2 ASC;