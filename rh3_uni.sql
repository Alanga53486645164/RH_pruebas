-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: rh3_uni
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `idad` int(2) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `contraseña` varchar(50) NOT NULL,
  PRIMARY KEY (`idad`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'Octavio Emilio Martinez Fonseca','123'),(2,'Diego Samuel Aguila Duron','456'),(3,'Ramiro Trujillo Ramirez','789');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area` (
  `idArea` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(60) NOT NULL,
  PRIMARY KEY (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (1,'DIRECCION GENERAL'),(2,'ADMINISTRACION Y RECURSOS HUMANOS'),(3,'PRODUCCION'),(4,'FINANZAS Y CONTABILIDAD'),(5,'MERCADOTECNIA'),(8,'informática');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `candidato`
--

DROP TABLE IF EXISTS `candidato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `candidato` (
  `idCandidato` int(11) NOT NULL,
  `idVacante` int(11) NOT NULL,
  `idRequisicion` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `CURP` varchar(30) NOT NULL,
  `RFC` varchar(20) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `domCalle` varchar(40) NOT NULL,
  `domNumExtInt` varchar(30) NOT NULL,
  `domColonia` varchar(40) NOT NULL,
  `tel1` varchar(20) NOT NULL,
  `tel2` varchar(20) NOT NULL,
  `correoE` varchar(40) NOT NULL,
  `edad` int(11) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `entrevSelecReq` tinyint(4) NOT NULL,
  `entrevSelecPresen` tinyint(4) NOT NULL,
  `entrevSelecResult` varchar(40) NOT NULL,
  `evalMedicaReq` tinyint(4) NOT NULL,
  `evalMedicaPresen` tinyint(4) NOT NULL,
  `evalMedicaResult` varchar(40) NOT NULL,
  `evalPsicolgReq` tinyint(4) NOT NULL,
  `evalPsicologPresen` tinyint(4) NOT NULL,
  `evalPsicologResult` varchar(40) NOT NULL,
  `evalPsicometReq` tinyint(4) NOT NULL,
  `evalPsicometPresene` tinyint(4) NOT NULL,
  `evalPsicometResult` varchar(40) NOT NULL,
  `evalTecnicaReq` tinyint(4) NOT NULL,
  `evalTecnicaPresen` tinyint(4) NOT NULL,
  `evalTecnicaResult` varchar(41) NOT NULL,
  `evalConocReq` tinyint(4) NOT NULL,
  `evalConocPresen` tinyint(4) NOT NULL,
  `evalConocResult` varchar(40) NOT NULL,
  `entrevFinalReq` tinyint(4) NOT NULL,
  `entrevFinalPresen` tinyint(4) NOT NULL,
  `entrevFinalResul` varchar(40) NOT NULL,
  `estado` enum('aceptado','rechazado') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `candidato`
--

LOCK TABLES `candidato` WRITE;
/*!40000 ALTER TABLE `candidato` DISABLE KEYS */;
INSERT INTO `candidato` VALUES (1,1,1,1,'ROGH760106MASDML03','dfadf','fasdfads','adsfa','23','erqwr','32','23','rqwr',23,'Indistinto',1,2,1,1,0,0,'',0,0,'',0,0,'',0,0,'',0,0,'',0,0,'',0,0,'','aceptado'),(2,1,1,1,'ROML551119HASDCR08','dfadf','juan','adsfa','23','erqwr','32','23','rqwr',23,'Indistinto',3,2,3,1,0,0,'',0,0,'',0,0,'',0,0,'',0,0,'',0,0,'',0,0,'','aceptado'),(12,1,1,1,'efgge4','334','juan','1','1','1','1','1','1',18,'femenino',1,1,1,1,1,1,'1',1,1,'1',1,1,'1',1,1,'1',1,1,'1',1,1,'1',1,1,'1','aceptado'),(22,1,1,1,'fefe34','edsg','wesd','sdad','121','dsef','22222','33333','wfffw',18,'femenino',1,1,1,1,0,0,'0',0,0,'0',0,0,'0',0,0,'0',0,0,'0',0,0,'0',0,0,'0','aceptado'),(233,2,2,2,'22','22','Raul','22','22','2','22','2','22',18,'femenino',2,3,2,2,2,2,'2',2,2,'2',2,2,'2',2,2,'2',2,2,'2',2,2,'2',2,2,'2','aceptado');
/*!40000 ALTER TABLE `candidato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrera`
--

DROP TABLE IF EXISTS `carrera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrera` (
  `idCarrera` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idCarrera`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrera`
--

LOCK TABLES `carrera` WRITE;
/*!40000 ALTER TABLE `carrera` DISABLE KEYS */;
INSERT INTO `carrera` VALUES (1,'NO APLICA'),(2,'ADMINISTRACION DE EMPRESAS'),(3,'ADMINISTRACIÓN DE PRODUCCIÓN Y SERVICIOS'),(4,'ADMINISTRACIÓN FINANCIERA'),(5,'COMERCIO INTERNACIONAL'),(6,'COMERCIO ELECTRONICO'),(7,'COMUNICACION'),(8,'CONTADOR '),(9,'DERECHO'),(10,'ECONOMIA'),(11,'GESTION TURISTICA'),(12,'LOGISTICA EMPRESARIAL'),(13,'MERCADOTECNIA'),(14,'SISTEMAS COMPUTACIONALES Y AFINES'),(15,'INDUSTRIAL'),(16,'ELECTRICA'),(17,'ROBOTICA'),(18,'RELACIONES INDUSTRIALES'),(19,'PSICOLOGIA'),(20,'ELECTRONICA'),(21,'GESTION EMPRESARIAL');
/*!40000 ALTER TABLE `carrera` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso_has_aparicion`
--

DROP TABLE IF EXISTS `curso_has_aparicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso_has_aparicion` (
  `id_registro` int(11) NOT NULL AUTO_INCREMENT,
  `id_metodo_aplicacion` int(11) NOT NULL,
  `lugar` varchar(40) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `edicion` mediumtext NOT NULL,
  `inicio` date NOT NULL,
  `fin` date NOT NULL,
  `id_encargado` int(11) NOT NULL,
  PRIMARY KEY (`id_registro`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso_has_aparicion`
--

LOCK TABLES `curso_has_aparicion` WRITE;
/*!40000 ALTER TABLE `curso_has_aparicion` DISABLE KEYS */;
INSERT INTO `curso_has_aparicion` VALUES (1,1,'Area 51',1,'1','2002-04-02','2002-04-20',2),(2,3,'NO HAY',2,'1','2002-03-27','2002-04-15',3);
/*!40000 ALTER TABLE `curso_has_aparicion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso_has_empleados`
--

DROP TABLE IF EXISTS `curso_has_empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso_has_empleados` (
  `id_registro` int(11) NOT NULL AUTO_INCREMENT,
  `id_curso` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `calificacion` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_registro`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso_has_empleados`
--

LOCK TABLES `curso_has_empleados` WRITE;
/*!40000 ALTER TABLE `curso_has_empleados` DISABLE KEYS */;
INSERT INTO `curso_has_empleados` VALUES (1,1,5,NULL),(2,2,5,NULL),(3,3,5,NULL),(4,1,1,NULL),(5,2,1,NULL),(6,3,1,NULL),(7,1,1,NULL),(8,2,8,NULL),(9,3,9,NULL),(10,1,5,NULL),(11,2,8,NULL),(12,2,5,NULL);
/*!40000 ALTER TABLE `curso_has_empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `duracion` varchar(15) NOT NULL,
  `objetivos_de_aprendizaje` varchar(300) NOT NULL,
  `obligatorio` tinyint(1) NOT NULL,
  `veces_aparecido` mediumtext DEFAULT NULL,
  PRIMARY KEY (`id_curso`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,'Curso de Induccion','Curso para la capacitacion de nuevos empleados','32 horas','entendimiento de politicas de la empresa, desempeño optimo del trabajo',1,'1'),(2,'Capacitacion de obrero','Curso para la capacitacion de los obreros','20 horas','entendimiento de politicas de la empresa, desempeño optimo del trabajo',1,'1'),(3,'Papiroflexia','curso de origami','5 horas','capacitar tus dedos para tareas delicadas',0,'0');
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `docto_solic`
--

DROP TABLE IF EXISTS `docto_solic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `docto_solic` (
  `idDoctoSolic` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(70) NOT NULL,
  `original` varchar(2) NOT NULL,
  `numCopias` int(5) NOT NULL,
  PRIMARY KEY (`idDoctoSolic`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `docto_solic`
--

LOCK TABLES `docto_solic` WRITE;
/*!40000 ALTER TABLE `docto_solic` DISABLE KEYS */;
INSERT INTO `docto_solic` VALUES (1,'Solicitud de empleo','SI',1),(2,'CURRICULUM VITAE con fotografía','SI',1),(3,'Carta de presentación','SI',1),(4,'Carta de recomendación','SI',1),(5,'Comprobante de domicilio reciente','NO',2),(6,'Acta de nacimiento','SI',1),(7,'Número del seguro social','NO',2),(8,'CURP','NO',2),(9,'Credencial para votar','NO',2),(10,'Licencia automovilista','NO',2),(11,'Licencia chofer','NO',2),(12,'Certificado Carrera Comercial o Técnica','NO',2),(13,'Certificado Preparatoria o Equivalente','NO',2),(14,'Certificado Licenciatura o Equivalente','NO',2),(15,'Constancia de Estudios','SI',2),(16,'Carta de Pasante Carrera Técnica','NO',2),(17,'Carta de Pasante Licenciatura','NO',2),(18,'Carta de Pasante Posgrado','NO',2),(19,'Cédula Profesional','NO',2),(20,'Título Licenciatura','NO',2),(21,'Título Posgrado','NO',2),(22,'Certificado Médico','SI',2),(23,'Antecedentes No penales','Si',1);
/*!40000 ALTER TABLE `docto_solic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `escolaridad`
--

DROP TABLE IF EXISTS `escolaridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `escolaridad` (
  `idEscolaridad` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idEscolaridad`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `escolaridad`
--

LOCK TABLES `escolaridad` WRITE;
/*!40000 ALTER TABLE `escolaridad` DISABLE KEYS */;
INSERT INTO `escolaridad` VALUES (1,'NO APLICA / NO REQUERIDA '),(2,'PREPARATORIA'),(3,'CARRERA TÉCNICA O COMERCIAL'),(4,'BACHILLERATO TÉCNICO O ESPECIALIZADO'),(5,'TÉCNICO SUPERIOR UNIVERSITARIO'),(6,'LICENCIATURA / INGENIERÍA / PROFESIONAL'),(7,'MAESTRIA'),(8,'DOCTORADO'),(9,'kinder según andrei');
/*!40000 ALTER TABLE `escolaridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_civil`
--

DROP TABLE IF EXISTS `estado_civil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_civil` (
  `idEstadoCivil` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idEstadoCivil`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_civil`
--

LOCK TABLES `estado_civil` WRITE;
/*!40000 ALTER TABLE `estado_civil` DISABLE KEYS */;
INSERT INTO `estado_civil` VALUES (1,'INDISTINTO'),(2,'SOLTERO'),(3,'CASADO'),(4,'UNION LIBRE');
/*!40000 ALTER TABLE `estado_civil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grado_avance`
--

DROP TABLE IF EXISTS `grado_avance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grado_avance` (
  `idGradoAvance` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) NOT NULL,
  PRIMARY KEY (`idGradoAvance`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grado_avance`
--

LOCK TABLES `grado_avance` WRITE;
/*!40000 ALTER TABLE `grado_avance` DISABLE KEYS */;
INSERT INTO `grado_avance` VALUES (1,'NO APLICA'),(2,'CURSANDO'),(3,'TERMINADO'),(4,'INCONCLUSO'),(5,'PASANTE'),(6,'TITULADO');
/*!40000 ALTER TABLE `grado_avance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `habilidad`
--

DROP TABLE IF EXISTS `habilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `habilidad` (
  `idHabilidad` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) NOT NULL,
  PRIMARY KEY (`idHabilidad`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habilidad`
--

LOCK TABLES `habilidad` WRITE;
/*!40000 ALTER TABLE `habilidad` DISABLE KEYS */;
INSERT INTO `habilidad` VALUES (1,'NO REQUERIDAS'),(2,'FACILIDAD DE PALABRA'),(3,'MANEJO DE CONFLICTOS'),(4,'CAPACIDAD PARA TRABAJAR BAJO PRESION'),(5,'CAPACIDAD DE TRABAJO EN EQUIPO'),(6,'TOMA DE DECISIONES'),(7,'PENSAMIENTO CREATIVO'),(8,'PENSAMIENTO CRITICO'),(9,'MANEJO DE EMOCIONES'),(10,'PROACTIVIDAD'),(11,'PROFESIONALIDAD'),(12,'ESCUCHA ACTIVA');
/*!40000 ALTER TABLE `habilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `idioma`
--

DROP TABLE IF EXISTS `idioma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `idioma` (
  `idIdioma` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idIdioma`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `idioma`
--

LOCK TABLES `idioma` WRITE;
/*!40000 ALTER TABLE `idioma` DISABLE KEYS */;
INSERT INTO `idioma` VALUES (1,'NO REQUERIDO'),(2,'INGLES BASICO'),(3,'INGLES INTERMEDIO'),(4,'INGLES AVANZADO'),(5,'JAPONES BASICO'),(6,'JAPONES CONVERSACIONAL'),(7,'JAPONES ESCRITO Y CONVERSACIONAL'),(9,'ALEMAN AVANZADO');
/*!40000 ALTER TABLE `idioma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mediopublic`
--

DROP TABLE IF EXISTS `mediopublic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mediopublic` (
  `idMedioPublic` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(70) NOT NULL,
  PRIMARY KEY (`idMedioPublic`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mediopublic`
--

LOCK TABLES `mediopublic` WRITE;
/*!40000 ALTER TABLE `mediopublic` DISABLE KEYS */;
INSERT INTO `mediopublic` VALUES (1,'Convocatoria en áreas estratégicas de la empresa'),(2,'Sitio web de la empresa'),(3,'Servicio estatal de empleo'),(4,'Redes sociales para empleo'),(5,'Agencia particular de empleo'),(6,'Radio'),(7,'Televisión'),(8,'Periódico Digital');
/*!40000 ALTER TABLE `mediopublic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modo_aplicacion_curso`
--

DROP TABLE IF EXISTS `modo_aplicacion_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modo_aplicacion_curso` (
  `id_modo` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id_modo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modo_aplicacion_curso`
--

LOCK TABLES `modo_aplicacion_curso` WRITE;
/*!40000 ALTER TABLE `modo_aplicacion_curso` DISABLE KEYS */;
INSERT INTO `modo_aplicacion_curso` VALUES (1,'PRESENCIAL'),(2,'SOLO MATERIAL DIDACTICO'),(3,'VIRTUAL');
/*!40000 ALTER TABLE `modo_aplicacion_curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publi`
--

DROP TABLE IF EXISTS `publi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publi` (
  `idp` int(2) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL,
  PRIMARY KEY (`idp`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publi`
--

LOCK TABLES `publi` WRITE;
/*!40000 ALTER TABLE `publi` DISABLE KEYS */;
INSERT INTO `publi` VALUES (1,'Publicada'),(2,'No Publicada');
/*!40000 ALTER TABLE `publi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puesto`
--

DROP TABLE IF EXISTS `puesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puesto` (
  `idPuesto` int(11) NOT NULL AUTO_INCREMENT,
  `codPuesto` varchar(15) NOT NULL,
  `idArea` int(11) NOT NULL,
  `nomPuesto` varchar(50) NOT NULL,
  `puestoJefeSup` varchar(50) NOT NULL,
  `jornada` varchar(70) NOT NULL,
  `remunMensual` int(11) NOT NULL,
  `prestaciones` varchar(70) NOT NULL,
  `descripcionGeneral` varchar(250) NOT NULL,
  `funciones` varchar(250) NOT NULL,
  `edad` varchar(50) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `idEstadoCivil` int(11) NOT NULL,
  `idEscolaridad` int(11) NOT NULL,
  `idGradoAvance` int(11) NOT NULL,
  `idCarrera` int(11) NOT NULL,
  `experiencia` varchar(70) NOT NULL,
  `conocimientos` varchar(70) NOT NULL,
  `manejoEquipo` varchar(70) NOT NULL,
  `reqFisicos` varchar(70) NOT NULL,
  `reqPsicologicos` varchar(70) NOT NULL,
  `responsabilidades` varchar(70) NOT NULL,
  `condicionesTrabajo` varchar(70) NOT NULL,
  PRIMARY KEY (`idPuesto`),
  KEY `idEscolaridad` (`idEscolaridad`),
  KEY `idEstadoCivil` (`idEstadoCivil`),
  KEY `idGradoAvance` (`idGradoAvance`),
  KEY `idCarrera` (`idCarrera`),
  KEY `area` (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puesto`
--

LOCK TABLES `puesto` WRITE;
/*!40000 ALTER TABLE `puesto` DISABLE KEYS */;
INSERT INTO `puesto` VALUES (1,'V009',5,'SUPERVISOR DE TIENDA ','SUPERVISOR','LUNES A VIERNES',5000,'DE LEY','VENTAS AL PÚBLICO','VENDER','18 A 45 AÑOS','Hombre',1,3,2,2,'2 AÑOS','VENTAS','DE COMPUTO','AGUDEZA VISUAL','MEMORIA A CORTO Y LARGO PLAZO','INVENTARIO','AGRADABLES'),(3,'v0008',3,'OBRERO','SUPERVISOR','LUNES A VIERNES',5000,'DE LEY','maquilar','trabajar','18 A 45 AÑOS','Indistinto',1,2,2,1,'2 AÑOS','VENTAS','DE COMPUTO','AGUDEZA VISUAL','MEMORIA A CORTO Y LARGO PLAZO','INVENTARIO','AGRADABLES'),(5,'p001',5,'JEFE DE MERCADOTECNIA','GERENTE','LUNES A VIERNES 8:30am 4:30am SABADOS 9:00am  A 2:00am',6500,'DE LEY','COORDINAR A PERSONAL DE MERCADOTECNIA','CORDINACIÓN','25 A 50','Indistinto',1,3,4,13,'2 AÑOS','VENTAS','DE COMPUTO','NO NECESARIOS','MEMORIA A CORTO Y LARGO PLAZO','NO ESPECIFICADAS','AGRADABLES');
/*!40000 ALTER TABLE `puesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puesto_has_cursos`
--

DROP TABLE IF EXISTS `puesto_has_cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puesto_has_cursos` (
  `id_registro` int(11) NOT NULL AUTO_INCREMENT,
  `id_curso` int(11) NOT NULL,
  `id_puesto` int(11) NOT NULL,
  PRIMARY KEY (`id_registro`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puesto_has_cursos`
--

LOCK TABLES `puesto_has_cursos` WRITE;
/*!40000 ALTER TABLE `puesto_has_cursos` DISABLE KEYS */;
INSERT INTO `puesto_has_cursos` VALUES (1,1,1),(2,1,3);
/*!40000 ALTER TABLE `puesto_has_cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puesto_has_habilidad`
--

DROP TABLE IF EXISTS `puesto_has_habilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puesto_has_habilidad` (
  `idPuesto` int(11) NOT NULL,
  `idHabilidad` int(11) NOT NULL,
  PRIMARY KEY (`idPuesto`,`idHabilidad`),
  KEY `idHabilidad` (`idHabilidad`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puesto_has_habilidad`
--

LOCK TABLES `puesto_has_habilidad` WRITE;
/*!40000 ALTER TABLE `puesto_has_habilidad` DISABLE KEYS */;
INSERT INTO `puesto_has_habilidad` VALUES (1,1),(3,4),(3,5),(5,2),(5,3),(5,4),(5,5),(5,6),(5,7),(5,8),(5,9),(5,10),(5,11),(5,12);
/*!40000 ALTER TABLE `puesto_has_habilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puesto_has_idioma`
--

DROP TABLE IF EXISTS `puesto_has_idioma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puesto_has_idioma` (
  `idPuesto` int(11) NOT NULL,
  `idIdioma` int(11) NOT NULL,
  PRIMARY KEY (`idPuesto`,`idIdioma`),
  KEY `idIdioma` (`idIdioma`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puesto_has_idioma`
--

LOCK TABLES `puesto_has_idioma` WRITE;
/*!40000 ALTER TABLE `puesto_has_idioma` DISABLE KEYS */;
INSERT INTO `puesto_has_idioma` VALUES (1,2),(3,1),(5,2);
/*!40000 ALTER TABLE `puesto_has_idioma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requisicion`
--

DROP TABLE IF EXISTS `requisicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requisicion` (
  `idRequisicion` int(11) NOT NULL AUTO_INCREMENT,
  `folio` varchar(25) NOT NULL,
  `fechaElab` date NOT NULL,
  `fechaRecluta` date NOT NULL,
  `fechaInicVac` date NOT NULL,
  `motivoRequisicion` varchar(30) NOT NULL,
  `motivoEspecifique` varchar(70) NOT NULL,
  `tipoVacante` varchar(15) NOT NULL,
  `nomSolicita` varchar(70) NOT NULL,
  `nomAutoriza` varchar(70) NOT NULL,
  `nomRevisa` varchar(70) NOT NULL,
  `autorizada` tinyint(1) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `idArea` int(11) NOT NULL,
  PRIMARY KEY (`idRequisicion`),
  KEY `idPuesto` (`idPuesto`),
  KEY `idArea` (`idArea`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requisicion`
--

LOCK TABLES `requisicion` WRITE;
/*!40000 ALTER TABLE `requisicion` DISABLE KEYS */;
INSERT INTO `requisicion` VALUES (1,'1','0000-00-00','0000-00-00','0000-00-00','1','','','LUIS, JEFE DE VENTAS','luis','juan',1,1,1),(10,'2','2023-11-23','2023-11-27','2023-12-01','Otro','temporada','Temporal','LUIS, JEFE DE VENTAS','luis','juan',1,1,1);
/*!40000 ALTER TABLE `requisicion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sexo`
--

DROP TABLE IF EXISTS `sexo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sexo` (
  `idSexo` int(2) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(20) NOT NULL,
  PRIMARY KEY (`idSexo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sexo`
--

LOCK TABLES `sexo` WRITE;
/*!40000 ALTER TABLE `sexo` DISABLE KEYS */;
INSERT INTO `sexo` VALUES (1,'Masculino'),(2,'Femenino'),(3,'Indistinto');
/*!40000 ALTER TABLE `sexo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajadores`
--

DROP TABLE IF EXISTS `trabajadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajadores` (
  `idTrabajador` int(11) NOT NULL AUTO_INCREMENT,
  `idArea` int(6) NOT NULL,
  `idPuesto` int(6) NOT NULL,
  `NombreTrab` varchar(100) NOT NULL,
  `edad` varchar(2) DEFAULT NULL,
  `sexo` varchar(50) DEFAULT NULL,
  `idEstadoCivil` int(6) NOT NULL,
  `idEscolaridad` int(6) NOT NULL,
  `idGradoAvance` int(6) NOT NULL,
  `idCarrera` int(6) NOT NULL,
  PRIMARY KEY (`idTrabajador`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajadores`
--

LOCK TABLES `trabajadores` WRITE;
/*!40000 ALTER TABLE `trabajadores` DISABLE KEYS */;
INSERT INTO `trabajadores` VALUES (7,5,5,'Gael Alecastro','17','Hombre',2,4,2,16),(8,5,5,'Hilda Juliana','16','Mujer',2,4,2,16),(9,8,1,'Ana Sanchez','16','Mujer',2,4,2,17),(10,8,5,'Gael Abdiel Cruz Ramos','7','Hombre',2,2,3,10);
/*!40000 ALTER TABLE `trabajadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacante`
--

DROP TABLE IF EXISTS `vacante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacante` (
  `idVacante` int(11) NOT NULL AUTO_INCREMENT,
  `conseVR` int(11) NOT NULL,
  `fuenteCandidato` varchar(40) NOT NULL,
  `inicioFechaPublic` date NOT NULL,
  `finFechaPublic` date NOT NULL,
  `publicada` tinyint(4) NOT NULL,
  `observaciones` varchar(40) NOT NULL,
  `candidatoSelecc` int(11) NOT NULL,
  `fechaContratacion` date NOT NULL,
  `idRequisicion` int(11) NOT NULL,
  `idPuesto` int(11) NOT NULL,
  `estado_vacante` varchar(50) NOT NULL,
  PRIMARY KEY (`idVacante`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacante`
--

LOCK TABLES `vacante` WRITE;
/*!40000 ALTER TABLE `vacante` DISABLE KEYS */;
INSERT INTO `vacante` VALUES (1,0,'Interno','2023-11-23','2023-11-27',1,'gfgf',0,'0000-00-00',1,1,'');
/*!40000 ALTER TABLE `vacante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'rh3_uni'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-22  9:08:05
