use rh3;
set sql_safe_updates=0;
drop table if exists curso_has_aparicion;
drop table if exists puesto_has_cursos;
drop table if exists curso_has_empleados;
drop table if exists curso;
drop table if exists cursos;
drop table if exists empleados;
drop table if exists modo_aplicacion_curso;


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
/*Provicional en lo que conseguimos la tabla del otro equipo*/
create table empleados(
	id_empleado int primary key auto_increment not null,
    nombre varchar(40) not null
    #...Equipo colaborando
);
insert into empleados(nombre) values
	("MARTIN"),
    ("PEDRO"),
    ("GREGORIO"),
    ("ALFONSO"),
    ("JUAN");
/**/
create table cursos(
	id_curso int primary key auto_increment not null,
    nombre varchar(50) not null,
    descripcion varchar(100) not null,
    duracion varchar (15) not null, 
    objetivos_de_aprendizaje varchar(300) not null,
    obligatorio boolean not null
);
insert into cursos(nombre,descripcion,duracion,objetivos_de_aprendizaje,obligatorio) values
	("Curso de Induccion","Curso para la capacitacion de nuevos empleados","32 horas","entendimiento de politicas de la empresa, desempeño optimo del trabajo",True),
    ("Capacitacion de obrero","Curso para la capacitacion de los obreros","20 horas","entendimiento de politicas de la empresa, desempeño optimo del trabajo",True),
    ("Papiroflexia","curso de origami","5 horas","capacitar tus dedos para tareas delicadas",false);
/*
create table capacitadores(
	id_capacitador int primary key,
    id_empleado int,
    id_curso int
);

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
	id_registro int primary key auto_increment not null,
    id_curso int not null,
    id_puesto int not null
    #,foreign key (id_curso) references cursos(id_curso),
    #foreign key (id_puesto) references puesto(idPuesto)
);
insert into puesto_has_cursos(id_curso,id_puesto) values
	(1,1),
    (1,3);
create table curso_has_empleados(
	id_registro int primary key auto_increment not null, 
	id_curso int not null, 
	id_empleado int not null, 
	calificacion int
    #,foreign key (id_curso) references cursos(id_curso),
    #foreign key (id_empleado) references empleados(id_empleado)
);
insert into curso_has_empleados(id_curso,id_empleado,calificacion) values
	/*(1,2,"2002-04-02","2002-04-20",null),
    (2,2,"2002-03-27","2002-04-15",8);*/
    (1,2,null),
    (2,2,8); 

create table modo_aplicacion_curso(
	id_modo int primary key auto_increment not null,
    nombre varchar(40) not null
);
insert into modo_aplicacion_curso(nombre) values
	("PRESENCIAL"),
    ("SOLO MATERIAL DIDACTICO"),
    ("VIRTUAL");
create table curso_has_aparicion(
	id_registro int primary key auto_increment not null,
    id_metodo_aplicacion int not null,
    lugar varchar(40) not null,
    id_curso int not null,
    inicio date not null,
    fin date not null,
    id_encargado int not null
    #,foreign key (id_curso) references cursos(id_curso),
    #foreign key (id_metodo_aplicacion) references modo_aplicacion_curso(id_modo),
    #foreign key (id_encargado) references empleados(id_empleado)
);
insert into curso_has_aparicion(id_metodo_aplicacion,lugar,id_curso,inicio,fin,id_encargado) values
	(1,"Area 51",1,"2002-04-02","2002-04-20",2),
    (3,"NO HAY",2,"2002-03-27","2002-04-15",3);