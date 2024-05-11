use rh3;
set sql_safe_updates=0;
/*
create table dias(
	id_dia int primary key auto_increment,
    dia varchar(15)
);
insert into dias(dia) values
	("LUNES"),
    ("MARTES"),
    ("MIERCOLES"),
    ("JUEVES"),
    ("VIERNES"),
    ("SABADO"),
    ("DOMINGO");
*/
create table empleados(
	id_empleado int primary key auto_increment,
    nombre varchar(40)
    #...Equipo colaborando
);
insert into empleados(nombre) values
	("MARTIN"),
    ("PEDRO"),
    ("JUAN");
create table cursos(
	id_curso int primary key auto_increment,
    nombre varchar(50),
    descripcion varchar(100),
    duracion varchar (15), 
    objetivos_de_aprendizaje varchar(200),
    lugar varchar(40),
    obligatorio boolean
);
insert into cursos(nombre,descripcion,duracion,objetivos_de_aprendizaje,lugar,obligatorio) values
	("Curso de Induccion","Curso para la capacitacion de nuevos empleados","32 horas","entendimiento de politicas de la empresa, desempeño optimo del trabajo","Area 51",True),
    ("Capacitacion de obrero","Curso para la capacitacion de los obreros","20 horas","entendimiento de politicas de la empresa, desempeño optimo del trabajo","Area 15",True);
/*
create table horario_has_actividad(
	id_registro int,
    dia varchar(10),
	hora_inicio datetime,
    hora_fin time,
    descripcion_actividad varchar(40),
    id_horario int 
);
insert into horario_has_actividad(dia,hora_inicio,hora_fin,descripcion_actividad,id_horario) values
	();
create table curso_has_horario (
    id_horario int primary key auto_increment,
    id_curso int
);
*/
create table puesto_has_cursos(
	id_registro int primary key auto_increment,
    id_curso int,
    id_puesto int
);
insert into puesto_has_cursos(id_curso,id_puesto) values
	(1,1),
    (1,3);
create table curso_has_empleados(
	id_registro int primary key auto_increment, 
	id_curso int, 
	id_empleado int , 
	#inicio date, 
	#fin date, 
	calificacion int
);
insert into curso_has_empleados(id_curso,id_empleado,calificacion) values
	/*(1,2,"2002-04-02","2002-04-20",null),
    (2,2,"2002-03-27","2002-04-15",8);*/
    (1,2,null),
    (2,2,8);
#delete from curso_has_empleados;
#drop table curso_has_empleados;
select * from curso_has_empleados;

create table curso_has_aparicion(
	id_registro int primary key auto_increment,
    id_curso int,
    inicio date,
    fin date
);
insert into curso_has_aparicion(id_curso,inicio,fin) values
	(1,"2002-04-02","2002-04-20"),
    (2,"2002-03-27","2002-04-15");