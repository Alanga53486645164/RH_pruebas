use rh3;
drop table if exists empleados;
drop table if exists cursos;
drop table if exists puesto_has_cursos;
drop table if exists curso_has_empleados;
drop table if exists modo_aplicacion_curso;
drop table if exists curso_has_aparicion;

drop table if exists trabajadores;    
CREATE TABLE `trabajadores` (
  `idTrabajador` int(11) NOT NULL AUTO_INCREMENT,
  `idPuesto` int(6) NOT NULL,
   edad varchar(3) not null,
   sexo varchar(15) not null,
  `idEstadoCivil` int(6) NOT NULL,
  `NombreTrab` varchar(100) NOT NULL,
  PRIMARY KEY (`idTrabajador`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `trabajadores` VALUES 
	(4,1,'16','Mujer',3,'Nelly Hinojo'),
    (3,5,'16','Hombre',2,'Gael Alecastro'),
    (2,5,'16','Mujer',2,'Hilda Juliana'),
    (1,1,'16','Mujer',2,'Ana Sanchez');

drop table if exists modo_aplicacion_curso;
create table modo_aplicacion_curso(
	id_modo int primary key auto_increment not null,
    nombre varchar(40) not null
);
insert into modo_aplicacion_curso(nombre) values
	("PRESENCIAL"),
    ("SOLO MATERIAL DIDACTICO"),
    ("VIRTUAL");
   
drop table if exists cursos;
CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `duracion` varchar(15) NOT NULL,
  `objetivos_de_aprendizaje` varchar(300) NOT NULL,
  `obligatorio` tinyint(1) NOT NULL,
  veces_aparecido long,
  PRIMARY KEY (`id_curso`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
INSERT INTO `cursos` VALUES 
	(1,'Curso de Induccion','Curso para la capacitacion de nuevos empleados','32 horas','entendimiento de politicas de la empresa, desempeño optimo del trabajo',1,1),
	(2,'Capacitacion de obrero','Curso para la capacitacion de los obreros','20 horas','entendimiento de politicas de la empresa, desempeño optimo del trabajo',1,1),
	(3,'Papiroflexia','curso de origami','5 horas','capacitar tus dedos para tareas delicadas',0,0);

drop table if exists puesto_has_cursos;
create table puesto_has_cursos(
	id_registro int primary key auto_increment not null,
    id_curso int not null,
    id_puesto int not null
);
insert into puesto_has_cursos(id_curso,id_puesto) values
	(1,1),
    (1,3);

drop table if exists curso_has_aparicion;
create table curso_has_aparicion(
	id_registro int primary key auto_increment not null,
    id_metodo_aplicacion int  not null,
    lugar varchar(40) not null,
    id_curso int not null,
    edicion long not null,
    inicio date not null,
    fin date not null,
    id_encargado int not null /*fk a empleados*/
);
insert into curso_has_aparicion(id_metodo_aplicacion,lugar,id_curso,edicion,inicio,fin,id_encargado) values
	(1,"Area 51",1,1,"2002-04-02","2002-04-20",2),
	(3,"NO HAY",2,1,"2002-03-27","2002-04-15",3);
    
/*
drop table if exists trabajadores_cursos;
CREATE TABLE `trabajadores_cursos` (
  `idTrabajador` int(11) NOT NULL,
  `idCurso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
*/

drop table if exists curso_has_empleados;
create table curso_has_empleados(
	id_registro int primary key auto_increment not null, 
	id_curso int not null, 
	id_empleado int  not null, 
	#inicio date not null, 
	#fin date not null, 
	calificacion int
);
insert into curso_has_empleados(id_empleado,id_curso,calificacion) values
    /*(2,1,null),
    (2,1,8),*/
    (5,1,null),(5,2,null),(5,3,null),(1,1,null),(1,2,null),(1,3,null),(1,1,null),(8,2,null),(9,3,null),(5,1,null),(8,2,null),(5,2,null);
    
#INSERT INTO `trabajadores_cursos` VALUES (5,1),(5,2),(5,3),(1,1),(1,2),(1,3),(1,1),(8,2),(9,3),(5,1),(8,2),(5,2);

