-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.6.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para seguimiento
CREATE DATABASE IF NOT EXISTS `seguimiento` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `seguimiento`;

-- Volcando estructura para tabla seguimiento.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.auth_group: ~3 rows (aproximadamente)
DELETE FROM `auth_group`;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` (`id`, `name`) VALUES
	(3, 'administradores'),
	(2, 'GrupoEmpresa'),
	(1, 'GrupoEstudiante');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.auth_group_permissions: ~128 rows (aproximadamente)
DELETE FROM `auth_group_permissions`;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
	(1, 1, 41),
	(2, 1, 42),
	(3, 1, 43),
	(4, 1, 44),
	(5, 1, 53),
	(6, 1, 54),
	(7, 1, 55),
	(8, 1, 56),
	(9, 1, 61),
	(10, 1, 62),
	(11, 1, 63),
	(12, 1, 64),
	(13, 1, 73),
	(14, 1, 74),
	(15, 1, 75),
	(16, 1, 76),
	(17, 1, 77),
	(18, 1, 78),
	(19, 1, 79),
	(20, 1, 80),
	(21, 1, 81),
	(22, 1, 82),
	(23, 1, 83),
	(24, 1, 84),
	(25, 1, 89),
	(26, 1, 90),
	(27, 1, 91),
	(28, 1, 92),
	(33, 2, 45),
	(34, 2, 46),
	(35, 2, 47),
	(36, 2, 48),
	(29, 2, 65),
	(30, 2, 66),
	(31, 2, 67),
	(32, 2, 68),
	(37, 3, 1),
	(38, 3, 2),
	(39, 3, 3),
	(40, 3, 4),
	(41, 3, 5),
	(42, 3, 6),
	(43, 3, 7),
	(44, 3, 8),
	(45, 3, 9),
	(46, 3, 10),
	(47, 3, 11),
	(48, 3, 12),
	(49, 3, 13),
	(50, 3, 14),
	(51, 3, 15),
	(52, 3, 16),
	(53, 3, 17),
	(54, 3, 18),
	(55, 3, 19),
	(56, 3, 20),
	(57, 3, 21),
	(58, 3, 22),
	(59, 3, 23),
	(60, 3, 24),
	(61, 3, 25),
	(62, 3, 26),
	(63, 3, 27),
	(64, 3, 28),
	(65, 3, 29),
	(66, 3, 30),
	(67, 3, 31),
	(68, 3, 32),
	(69, 3, 33),
	(70, 3, 34),
	(71, 3, 35),
	(72, 3, 36),
	(73, 3, 37),
	(74, 3, 38),
	(75, 3, 39),
	(76, 3, 40),
	(77, 3, 41),
	(78, 3, 42),
	(79, 3, 43),
	(80, 3, 44),
	(81, 3, 45),
	(82, 3, 46),
	(83, 3, 47),
	(84, 3, 48),
	(85, 3, 49),
	(86, 3, 50),
	(87, 3, 51),
	(88, 3, 52),
	(89, 3, 53),
	(90, 3, 54),
	(91, 3, 55),
	(92, 3, 56),
	(93, 3, 57),
	(94, 3, 58),
	(95, 3, 59),
	(96, 3, 60),
	(97, 3, 61),
	(98, 3, 62),
	(99, 3, 63),
	(100, 3, 64),
	(101, 3, 65),
	(102, 3, 66),
	(103, 3, 67),
	(104, 3, 68),
	(105, 3, 69),
	(106, 3, 70),
	(107, 3, 71),
	(108, 3, 72),
	(109, 3, 73),
	(110, 3, 74),
	(111, 3, 75),
	(112, 3, 76),
	(113, 3, 77),
	(114, 3, 78),
	(115, 3, 79),
	(116, 3, 80),
	(117, 3, 81),
	(118, 3, 82),
	(119, 3, 83),
	(120, 3, 84),
	(121, 3, 85),
	(122, 3, 86),
	(123, 3, 87),
	(124, 3, 88),
	(125, 3, 89),
	(126, 3, 90),
	(127, 3, 91),
	(128, 3, 92);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.auth_permission: ~92 rows (aproximadamente)
DELETE FROM `auth_permission`;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add carrera', 7, 'add_carrera'),
	(26, 'Can change carrera', 7, 'change_carrera'),
	(27, 'Can delete carrera', 7, 'delete_carrera'),
	(28, 'Can view carrera', 7, 'view_carrera'),
	(29, 'Can add empresa', 8, 'add_empresa'),
	(30, 'Can change empresa', 8, 'change_empresa'),
	(31, 'Can delete empresa', 8, 'delete_empresa'),
	(32, 'Can view empresa', 8, 'view_empresa'),
	(33, 'Can add encuesta_ laboral', 9, 'add_encuesta_laboral'),
	(34, 'Can change encuesta_ laboral', 9, 'change_encuesta_laboral'),
	(35, 'Can delete encuesta_ laboral', 9, 'delete_encuesta_laboral'),
	(36, 'Can view encuesta_ laboral', 9, 'view_encuesta_laboral'),
	(37, 'Can add estudiante', 10, 'add_estudiante'),
	(38, 'Can change estudiante', 10, 'change_estudiante'),
	(39, 'Can delete estudiante', 10, 'delete_estudiante'),
	(40, 'Can view estudiante', 10, 'view_estudiante'),
	(41, 'Can add hoja_de_vida', 11, 'add_hoja_de_vida'),
	(42, 'Can change hoja_de_vida', 11, 'change_hoja_de_vida'),
	(43, 'Can delete hoja_de_vida', 11, 'delete_hoja_de_vida'),
	(44, 'Can view hoja_de_vida', 11, 'view_hoja_de_vida'),
	(45, 'Can add informacion_laboral', 12, 'add_informacion_laboral'),
	(46, 'Can change informacion_laboral', 12, 'change_informacion_laboral'),
	(47, 'Can delete informacion_laboral', 12, 'delete_informacion_laboral'),
	(48, 'Can view informacion_laboral', 12, 'view_informacion_laboral'),
	(49, 'Can add periodo_ academico', 13, 'add_periodo_academico'),
	(50, 'Can change periodo_ academico', 13, 'change_periodo_academico'),
	(51, 'Can delete periodo_ academico', 13, 'delete_periodo_academico'),
	(52, 'Can view periodo_ academico', 13, 'view_periodo_academico'),
	(53, 'Can add referencias_ personales', 14, 'add_referencias_personales'),
	(54, 'Can change referencias_ personales', 14, 'change_referencias_personales'),
	(55, 'Can delete referencias_ personales', 14, 'delete_referencias_personales'),
	(56, 'Can view referencias_ personales', 14, 'view_referencias_personales'),
	(57, 'Can add pregunta', 15, 'add_pregunta'),
	(58, 'Can change pregunta', 15, 'change_pregunta'),
	(59, 'Can delete pregunta', 15, 'delete_pregunta'),
	(60, 'Can view pregunta', 15, 'view_pregunta'),
	(61, 'Can add preferencias_ laborales', 16, 'add_preferencias_laborales'),
	(62, 'Can change preferencias_ laborales', 16, 'change_preferencias_laborales'),
	(63, 'Can delete preferencias_ laborales', 16, 'delete_preferencias_laborales'),
	(64, 'Can view preferencias_ laborales', 16, 'view_preferencias_laborales'),
	(65, 'Can add oferta_ laboral', 17, 'add_oferta_laboral'),
	(66, 'Can change oferta_ laboral', 17, 'change_oferta_laboral'),
	(67, 'Can delete oferta_ laboral', 17, 'delete_oferta_laboral'),
	(68, 'Can view oferta_ laboral', 17, 'view_oferta_laboral'),
	(69, 'Can add mejor_ graduado', 18, 'add_mejor_graduado'),
	(70, 'Can change mejor_ graduado', 18, 'change_mejor_graduado'),
	(71, 'Can delete mejor_ graduado', 18, 'delete_mejor_graduado'),
	(72, 'Can view mejor_ graduado', 18, 'view_mejor_graduado'),
	(73, 'Can add logros_ personales', 19, 'add_logros_personales'),
	(74, 'Can change logros_ personales', 19, 'change_logros_personales'),
	(75, 'Can delete logros_ personales', 19, 'delete_logros_personales'),
	(76, 'Can view logros_ personales', 19, 'view_logros_personales'),
	(77, 'Can add instruccion_formal', 20, 'add_instruccion_formal'),
	(78, 'Can change instruccion_formal', 20, 'change_instruccion_formal'),
	(79, 'Can delete instruccion_formal', 20, 'delete_instruccion_formal'),
	(80, 'Can view instruccion_formal', 20, 'view_instruccion_formal'),
	(81, 'Can add experiencia_ laboral', 21, 'add_experiencia_laboral'),
	(82, 'Can change experiencia_ laboral', 21, 'change_experiencia_laboral'),
	(83, 'Can delete experiencia_ laboral', 21, 'delete_experiencia_laboral'),
	(84, 'Can view experiencia_ laboral', 21, 'view_experiencia_laboral'),
	(85, 'Can add eleccion', 22, 'add_eleccion'),
	(86, 'Can change eleccion', 22, 'change_eleccion'),
	(87, 'Can delete eleccion', 22, 'delete_eleccion'),
	(88, 'Can view eleccion', 22, 'view_eleccion'),
	(89, 'Can add capacitaciones', 23, 'add_capacitaciones'),
	(90, 'Can change capacitaciones', 23, 'change_capacitaciones'),
	(91, 'Can delete capacitaciones', 23, 'delete_capacitaciones'),
	(92, 'Can view capacitaciones', 23, 'view_capacitaciones');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.auth_user: ~5 rows (aproximadamente)
DELETE FROM `auth_user`;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$390000$5X4us4i8DvOVUveNCRxWig$r73YZ2DE5Svk/AJVOAiq//zsjmxmeIJoamITLOHHeOA=', '2023-01-26 05:21:25.837052', 1, 'allen', '', '', '', 1, 1, '2023-01-23 18:51:18.000000'),
	(2, 'pbkdf2_sha256$390000$IlDjhfxl8zXf6qv9jPZI9G$K4MIfrqKbyGr7mKZVOFSFxaIGBvHMRfOA2ExK0d175A=', '2023-01-26 05:25:36.725713', 0, 'estudiante1_', 'Luis', 'Sarmiento', '', 0, 1, '2023-01-23 18:55:34.329482'),
	(3, 'pbkdf2_sha256$390000$fGtFKmgaiCU4ebAMTbAgAJ$z8eCV34b4P1/qGEW1hJLXx3L9mPl5YGvaRCwKLykF0I=', '2023-01-26 04:35:44.601702', 0, 'empresa1_', 'Empresa grande de ejemplo', '', '', 0, 1, '2023-01-23 18:56:42.951762'),
	(4, 'pbkdf2_sha256$390000$XNDSAm5rFZ1b2dgTYiqEzM$rK9p9FrkvJo5fpUHTWygL+az+t912s57r6+E8My62iA=', '2023-01-23 19:01:36.435075', 0, 'empresa2_', 'Empresa de quito', '', '', 0, 1, '2023-01-23 18:58:00.000000'),
	(5, 'pbkdf2_sha256$390000$wNQDnApcG3yzkKX9SkPidh$KXInQdHtbTrcCcQRoJZwcP+jduBeGIcTAlLqojUdQ04=', NULL, 0, 'estudiante2_', 'Marcos', 'Aurelio', '', 0, 1, '2023-01-23 23:10:57.040176');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.auth_user_groups: ~5 rows (aproximadamente)
DELETE FROM `auth_user_groups`;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
	(1, 1, 3),
	(2, 2, 1),
	(3, 3, 2),
	(4, 4, 2),
	(5, 5, 1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.auth_user_user_permissions: ~0 rows (aproximadamente)
DELETE FROM `auth_user_user_permissions`;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.django_admin_log: ~10 rows (aproximadamente)
DELETE FROM `django_admin_log`;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
	(1, '2023-01-23 21:34:54.043710', '1', 'Luis Sarmiento', 2, '[{"changed": {"fields": ["Carrera"]}}]', 10, 1),
	(2, '2023-01-23 21:34:57.554211', '1', 'Luis Sarmiento', 2, '[]', 10, 1),
	(3, '2023-01-23 21:37:13.098160', '1', 'Ing. de seguridad en la empresa "Empresa grande de ejemplo"', 2, '[{"changed": {"fields": ["Carrera"]}}]', 17, 1),
	(4, '2023-01-23 21:37:17.332051', '2', 'Ing. de desarrollo en la empresa "Empresa de quito"', 2, '[{"changed": {"fields": ["Carrera"]}}]', 17, 1),
	(5, '2023-01-23 21:37:19.388132', '1', 'Ing. de seguridad en la empresa "Empresa grande de ejemplo"', 2, '[]', 17, 1),
	(6, '2023-01-23 21:37:21.082768', '2', 'Ing. de desarrollo en la empresa "Empresa de quito"', 2, '[]', 17, 1),
	(7, '2023-01-23 21:39:29.559163', '2', 'Ing. de desarrollo en la empresa "Empresa de quito"', 2, '[{"changed": {"fields": ["Carrera"]}}]', 17, 1),
	(8, '2023-01-23 22:05:12.597131', '3', 'programador', 1, '[{"added": {}}]', 12, 1),
	(9, '2023-01-23 22:05:23.038016', '3', 'programador en la empresa "Empresa de quito"', 1, '[{"added": {}}]', 17, 1),
	(10, '2023-01-24 03:36:40.638640', '3', 'programador en la empresa "Empresa de quito"', 2, '[{"changed": {"fields": ["Carrera"]}}]', 17, 1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.django_content_type: ~23 rows (aproximadamente)
DELETE FROM `django_content_type`;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(23, 'seguimiento', 'capacitaciones'),
	(7, 'seguimiento', 'carrera'),
	(22, 'seguimiento', 'eleccion'),
	(8, 'seguimiento', 'empresa'),
	(9, 'seguimiento', 'encuesta_laboral'),
	(10, 'seguimiento', 'estudiante'),
	(21, 'seguimiento', 'experiencia_laboral'),
	(11, 'seguimiento', 'hoja_de_vida'),
	(12, 'seguimiento', 'informacion_laboral'),
	(20, 'seguimiento', 'instruccion_formal'),
	(19, 'seguimiento', 'logros_personales'),
	(18, 'seguimiento', 'mejor_graduado'),
	(17, 'seguimiento', 'oferta_laboral'),
	(13, 'seguimiento', 'periodo_academico'),
	(16, 'seguimiento', 'preferencias_laborales'),
	(15, 'seguimiento', 'pregunta'),
	(14, 'seguimiento', 'referencias_personales'),
	(6, 'sessions', 'session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.django_migrations: ~19 rows (aproximadamente)
DELETE FROM `django_migrations`;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'contenttypes', '0001_initial', '2023-01-23 21:34:02.748959'),
	(2, 'auth', '0001_initial', '2023-01-23 21:34:03.546012'),
	(3, 'admin', '0001_initial', '2023-01-23 21:34:03.716268'),
	(4, 'admin', '0002_logentry_remove_auto_add', '2023-01-23 21:34:03.727904'),
	(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-01-23 21:34:03.734908'),
	(6, 'contenttypes', '0002_remove_content_type_name', '2023-01-23 21:34:03.832769'),
	(7, 'auth', '0002_alter_permission_name_max_length', '2023-01-23 21:34:03.900761'),
	(8, 'auth', '0003_alter_user_email_max_length', '2023-01-23 21:34:03.967046'),
	(9, 'auth', '0004_alter_user_username_opts', '2023-01-23 21:34:03.975249'),
	(10, 'auth', '0005_alter_user_last_login_null', '2023-01-23 21:34:04.041544'),
	(11, 'auth', '0006_require_contenttypes_0002', '2023-01-23 21:34:04.046099'),
	(12, 'auth', '0007_alter_validators_add_error_messages', '2023-01-23 21:34:04.054135'),
	(13, 'auth', '0008_alter_user_username_max_length', '2023-01-23 21:34:04.091918'),
	(14, 'auth', '0009_alter_user_last_name_max_length', '2023-01-23 21:34:04.131128'),
	(15, 'auth', '0010_alter_group_name_max_length', '2023-01-23 21:34:04.195813'),
	(16, 'auth', '0011_update_proxy_permissions', '2023-01-23 21:34:04.203807'),
	(17, 'auth', '0012_alter_user_first_name_max_length', '2023-01-23 21:34:04.242863'),
	(18, 'seguimiento', '0001_initial', '2023-01-23 21:34:06.345960'),
	(19, 'sessions', '0001_initial', '2023-01-23 21:34:06.437269');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.django_session: ~8 rows (aproximadamente)
DELETE FROM `django_session`;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('3yxhlvtgn54s2xqajrw0mtxs36jts2ao', '.eJxVjMsOwiAQRf-FtSFAKQ-X7v0GMswMUjU0Ke3K-O_apAvd3nPOfYkE21rT1nlJE4mzMOL0u2XAB7cd0B3abZY4t3WZstwVedAurzPx83K4fwcVev3WiHEYQralaHRcmA2MrDwaC0QKtMEIxM4FMjaiVjaP2cQSsmdgr1i8PxTXOR0:1pKA65:UV2ZUvgpoha1E1_46_9uLPs92UNJZO4gq5NYqQf4Hik', '2023-02-07 03:35:45.189728'),
	('6s0hzastghsyyjtvu64jyqp3n6x97paa', '.eJxVjEEOwiAQRe_C2hAmDDTj0r1nIMwAUjWQlHZlvLs26UK3_733XyrEba1hG3kJc1JnBer0u3GUR247SPfYbl1Lb-sys94VfdChrz3l5-Vw_w5qHPVbGyZA5IwAhjmWiYsvU0LxaAsRCmACcQ7IOlu8ASAj2QNlW5wwqfcH3wk3ng:1pKiui:VdBMxmnDpGNmGbV0Hf6QExh8-Xt1jCjSw7PIoHKXFd8', '2023-02-08 16:46:20.624656'),
	('7xyjvgzj59ol2gaq3gmbyquxsfxe6hoa', '.eJxVjMsOwiAQRf-FtSFAKQ-X7v0GMswMUjU0Ke3K-O_apAvd3nPOfYkE21rT1nlJE4mzMOL0u2XAB7cd0B3abZY4t3WZstwVedAurzPx83K4fwcVev3WiHEYQralaHRcmA2MrDwaC0QKtMEIxM4FMjaiVjaP2cQSsmdgr1i8PxTXOR0:1pKulU:V5vo347m3PiWbAebMLy2rqSdzuM8pUnuFeyYAFSv_j4', '2023-02-09 05:25:36.729707'),
	('81hs1x7azhhmpfr6gzvuztrbj2noxdrf', '.eJxVjMsOwiAQRf-FtSGUR6Eu3fsNZBhmpGogKe3K-O_apAvd3nPOfYkI21ri1mmJcxZnYcTpd0uAD6o7yHeotyax1XWZk9wVedAury3T83K4fwcFevnWGgbrrWI1WRs8mMBJZTdMiRVm1DqNSERsGJhY51Fbp4IjBDTeOofi_QHrTziL:1pKtzE:tw2VvLcGZighir9nyE4Ldl65SyrVWJdMERkRMlVBZ2k', '2023-02-09 04:35:44.616689'),
	('ikwc30grdyycdsltzxvli8djnxscqct3', '.eJxVjEEOwiAQRe_C2hAmDDTj0r1nIMwAUjWQlHZlvLs26UK3_733XyrEba1hG3kJc1JnBer0u3GUR247SPfYbl1Lb-sys94VfdChrz3l5-Vw_w5qHPVbGyZA5IwAhjmWiYsvU0LxaAsRCmACcQ7IOlu8ASAj2QNlW5wwqfcH3wk3ng:1pKA6k:BK6wGHnskaARo-7WeiRd4e_4UWEK2nEFx7TQJXdE0XQ', '2023-02-07 03:36:26.550803'),
	('jkxgvyo8tvfpa4r574haknfx0okin0vj', '.eJxVjEEOwiAQRe_C2hAmDDTj0r1nIMwAUjWQlHZlvLs26UK3_733XyrEba1hG3kJc1JnBer0u3GUR247SPfYbl1Lb-sys94VfdChrz3l5-Vw_w5qHPVbGyZA5IwAhjmWiYsvU0LxaAsRCmACcQ7IOlu8ASAj2QNlW5wwqfcH3wk3ng:1pK4SI:ieqek-dQ5Eb-AY2-sPjQiZC_ynpRQA24zGz58NT47tI', '2023-02-06 21:34:18.538545'),
	('jnedthv49ew1g6dbm56rbl9vqcrkcmr6', '.eJxVjEEOwiAQRe_C2hAmDDTj0r1nIMwAUjWQlHZlvLs26UK3_733XyrEba1hG3kJc1JnBer0u3GUR247SPfYbl1Lb-sys94VfdChrz3l5-Vw_w5qHPVbGyZA5IwAhjmWiYsvU0LxaAsRCmACcQ7IOlu8ASAj2QNlW5wwqfcH3wk3ng:1pK5xK:ELTKwE_b6hdgxcKBZZUa7snfHf4h4Zx1CFkO9BvFU1Q', '2023-02-06 23:10:26.554874'),
	('wq85j45d0dx00j5yr5hzofi96uttgi2f', '.eJxVjMsOwiAQRf-FtSFAKQ-X7v0GMswMUjU0Ke3K-O_apAvd3nPOfYkE21rT1nlJE4mzMOL0u2XAB7cd0B3abZY4t3WZstwVedAurzPx83K4fwcVev3WiHEYQralaHRcmA2MrDwaC0QKtMEIxM4FMjaiVjaP2cQSsmdgr1i8PxTXOR0:1pK4T2:ytxMqcElUz6sFVZsesgxZfECQvFy6itK-dniXRVOchQ', '2023-02-06 21:35:04.415204');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_capacitaciones
CREATE TABLE IF NOT EXISTS `seguimiento_capacitaciones` (
  `id_capacitaciones` int(11) NOT NULL AUTO_INCREMENT,
  `institucion` varchar(100) NOT NULL,
  `tipo_de_evento` varchar(50) NOT NULL,
  `area_de_estudio` varchar(100) NOT NULL,
  `nombre_de_evento` varchar(100) NOT NULL,
  `tipo_de_certificado` varchar(50) NOT NULL,
  `fecha_desde` date NOT NULL,
  `fecha_hasta` date NOT NULL,
  `dias` varchar(10) NOT NULL,
  `horas` varchar(10) NOT NULL,
  `hoja_de_vida_id` int(11) NOT NULL,
  PRIMARY KEY (`id_capacitaciones`),
  KEY `seguimiento_capacita_hoja_de_vida_id_44fbd6e4_fk_seguimien` (`hoja_de_vida_id`),
  CONSTRAINT `seguimiento_capacita_hoja_de_vida_id_44fbd6e4_fk_seguimien` FOREIGN KEY (`hoja_de_vida_id`) REFERENCES `seguimiento_hoja_de_vida` (`id_hoja_de_vida`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_capacitaciones: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_capacitaciones`;
/*!40000 ALTER TABLE `seguimiento_capacitaciones` DISABLE KEYS */;
INSERT INTO `seguimiento_capacitaciones` (`id_capacitaciones`, `institucion`, `tipo_de_evento`, `area_de_estudio`, `nombre_de_evento`, `tipo_de_certificado`, `fecha_desde`, `fecha_hasta`, `dias`, `horas`, `hoja_de_vida_id`) VALUES
	(1, 'UNL', 'SE', 'Ingenieria', 'Bootcamp software development', 'A', '2023-01-11', '2023-01-26', '12', '124', 1),
	(2, 'UTPL', 'TA', 'Pedagogia', 'Pedagogia de docentes', 'A', '2023-01-05', '2023-01-26', '32', '32', 2);
/*!40000 ALTER TABLE `seguimiento_capacitaciones` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_carrera
CREATE TABLE IF NOT EXISTS `seguimiento_carrera` (
  `id_carrera` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `estado` varchar(30) NOT NULL,
  `carrera_necesitada` varchar(30) NOT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_carrera: ~2 rows (aproximadamente)
DELETE FROM `seguimiento_carrera`;
/*!40000 ALTER TABLE `seguimiento_carrera` DISABLE KEYS */;
INSERT INTO `seguimiento_carrera` (`id_carrera`, `nombre`, `estado`, `carrera_necesitada`) VALUES
	(1, 'Mate', 'R', ''),
	(2, 'POO', 'E', 'PROGRAMCION');
/*!40000 ALTER TABLE `seguimiento_carrera` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_eleccion
CREATE TABLE IF NOT EXISTS `seguimiento_eleccion` (
  `id_eleccion` int(11) NOT NULL AUTO_INCREMENT,
  `texto_eleccion` int(11) NOT NULL,
  `votos` int(11) NOT NULL,
  `pregunta_id` int(11) NOT NULL,
  PRIMARY KEY (`id_eleccion`),
  KEY `seguimiento_eleccion_pregunta_id_bd656771_fk_seguimien` (`pregunta_id`),
  CONSTRAINT `seguimiento_eleccion_pregunta_id_bd656771_fk_seguimien` FOREIGN KEY (`pregunta_id`) REFERENCES `seguimiento_pregunta` (`id_pregunta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_eleccion: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_eleccion`;
/*!40000 ALTER TABLE `seguimiento_eleccion` DISABLE KEYS */;
/*!40000 ALTER TABLE `seguimiento_eleccion` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_empresa
CREATE TABLE IF NOT EXISTS `seguimiento_empresa` (
  `id_empresa` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` varchar(50) NOT NULL,
  `ubicacion` varchar(100) NOT NULL,
  `contacto` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id_empresa`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `seguimiento_empresa_user_id_491986c2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_empresa: ~2 rows (aproximadamente)
DELETE FROM `seguimiento_empresa`;
/*!40000 ALTER TABLE `seguimiento_empresa` DISABLE KEYS */;
INSERT INTO `seguimiento_empresa` (`id_empresa`, `direccion`, `ubicacion`, `contacto`, `user_id`) VALUES
	(1, 'AV. ANGEL', 'Loja', '0999', 3),
	(2, 'av. quito', 'quito', '1212', 4);
/*!40000 ALTER TABLE `seguimiento_empresa` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_encuesta_laboral
CREATE TABLE IF NOT EXISTS `seguimiento_encuesta_laboral` (
  `id_encuesta_laboral` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_pub` date NOT NULL,
  PRIMARY KEY (`id_encuesta_laboral`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_encuesta_laboral: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_encuesta_laboral`;
/*!40000 ALTER TABLE `seguimiento_encuesta_laboral` DISABLE KEYS */;
/*!40000 ALTER TABLE `seguimiento_encuesta_laboral` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_estudiante
CREATE TABLE IF NOT EXISTS `seguimiento_estudiante` (
  `id_estudiante` int(11) NOT NULL AUTO_INCREMENT,
  `cedula` varchar(10) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `estado` varchar(20) NOT NULL,
  `carrera_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id_estudiante`),
  UNIQUE KEY `cedula` (`cedula`),
  UNIQUE KEY `telefono` (`telefono`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `seguimiento_estudian_carrera_id_c9b40f93_fk_seguimien` (`carrera_id`),
  CONSTRAINT `seguimiento_estudian_carrera_id_c9b40f93_fk_seguimien` FOREIGN KEY (`carrera_id`) REFERENCES `seguimiento_carrera` (`id_carrera`),
  CONSTRAINT `seguimiento_estudiante_user_id_f69e1f1f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_estudiante: ~2 rows (aproximadamente)
DELETE FROM `seguimiento_estudiante`;
/*!40000 ALTER TABLE `seguimiento_estudiante` DISABLE KEYS */;
INSERT INTO `seguimiento_estudiante` (`id_estudiante`, `cedula`, `telefono`, `estado`, `carrera_id`, `user_id`) VALUES
	(1, '1106', '09', 'E', 1, 2),
	(2, '1107', '1212331', 'G', 2, 5);
/*!40000 ALTER TABLE `seguimiento_estudiante` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_estudiante_carrera
CREATE TABLE IF NOT EXISTS `seguimiento_estudiante_carrera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estudiante_id` int(11) NOT NULL,
  `carrera_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `seguimiento_estudiante_c_estudiante_id_carrera_id_c81fa1fc_uniq` (`estudiante_id`,`carrera_id`),
  KEY `seguimiento_estudian_carrera_id_f16f6c9f_fk_seguimien` (`carrera_id`),
  CONSTRAINT `seguimiento_estudian_carrera_id_f16f6c9f_fk_seguimien` FOREIGN KEY (`carrera_id`) REFERENCES `seguimiento_carrera` (`id_carrera`),
  CONSTRAINT `seguimiento_estudian_estudiante_id_e2b3ec99_fk_seguimien` FOREIGN KEY (`estudiante_id`) REFERENCES `seguimiento_estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_estudiante_carrera: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_estudiante_carrera`;
/*!40000 ALTER TABLE `seguimiento_estudiante_carrera` DISABLE KEYS */;
INSERT INTO `seguimiento_estudiante_carrera` (`id`, `estudiante_id`, `carrera_id`) VALUES
	(1, 1, 1);
/*!40000 ALTER TABLE `seguimiento_estudiante_carrera` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_estudiante_oferta
CREATE TABLE IF NOT EXISTS `seguimiento_estudiante_oferta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estudiante_id` int(11) NOT NULL,
  `oferta_laboral_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `seguimiento_estudiante_o_estudiante_id_oferta_lab_bc9907c4_uniq` (`estudiante_id`,`oferta_laboral_id`),
  KEY `seguimiento_estudian_oferta_laboral_id_9018e38e_fk_seguimien` (`oferta_laboral_id`),
  CONSTRAINT `seguimiento_estudian_estudiante_id_6a6f8e36_fk_seguimien` FOREIGN KEY (`estudiante_id`) REFERENCES `seguimiento_estudiante` (`id_estudiante`),
  CONSTRAINT `seguimiento_estudian_oferta_laboral_id_9018e38e_fk_seguimien` FOREIGN KEY (`oferta_laboral_id`) REFERENCES `seguimiento_oferta_laboral` (`id_oferta_laboral`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_estudiante_oferta: ~2 rows (aproximadamente)
DELETE FROM `seguimiento_estudiante_oferta`;
/*!40000 ALTER TABLE `seguimiento_estudiante_oferta` DISABLE KEYS */;
INSERT INTO `seguimiento_estudiante_oferta` (`id`, `estudiante_id`, `oferta_laboral_id`) VALUES
	(3, 1, 1),
	(4, 1, 2);
/*!40000 ALTER TABLE `seguimiento_estudiante_oferta` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_experiencia_laboral
CREATE TABLE IF NOT EXISTS `seguimiento_experiencia_laboral` (
  `id_experiencia_laboral` int(11) NOT NULL AUTO_INCREMENT,
  `institucion` varchar(100) NOT NULL,
  `tipo_de_institucion` varchar(100) NOT NULL,
  `area_de_trabajo` varchar(100) NOT NULL,
  `puesto` varchar(100) NOT NULL,
  `actividades` varchar(100) NOT NULL,
  `fecha_desde` date NOT NULL,
  `fecha_hasta` date NOT NULL,
  `trabaja_actualmente_en_este_lugar` tinyint(1) NOT NULL,
  `hoja_de_vida_id` int(11) NOT NULL,
  PRIMARY KEY (`id_experiencia_laboral`),
  KEY `seguimiento_experien_hoja_de_vida_id_9482a411_fk_seguimien` (`hoja_de_vida_id`),
  CONSTRAINT `seguimiento_experien_hoja_de_vida_id_9482a411_fk_seguimien` FOREIGN KEY (`hoja_de_vida_id`) REFERENCES `seguimiento_hoja_de_vida` (`id_hoja_de_vida`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_experiencia_laboral: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_experiencia_laboral`;
/*!40000 ALTER TABLE `seguimiento_experiencia_laboral` DISABLE KEYS */;
INSERT INTO `seguimiento_experiencia_laboral` (`id_experiencia_laboral`, `institucion`, `tipo_de_institucion`, `area_de_trabajo`, `puesto`, `actividades`, `fecha_desde`, `fecha_hasta`, `trabaja_actualmente_en_este_lugar`, `hoja_de_vida_id`) VALUES
	(1, 'UNL', 'Publica', 'Desarrollo', 'Programador Senior', 'Desarrollo de aplicaicones web y moviles', '2023-01-11', '2023-01-26', 1, 1),
	(2, 'UTPL', 'Pirvada', 'Docente', 'Docente encargado', 'Dar clase', '2023-01-05', '2023-01-26', 0, 2);
/*!40000 ALTER TABLE `seguimiento_experiencia_laboral` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_hoja_de_vida
CREATE TABLE IF NOT EXISTS `seguimiento_hoja_de_vida` (
  `id_hoja_de_vida` int(11) NOT NULL AUTO_INCREMENT,
  `estudiante_id` int(11) NOT NULL,
  PRIMARY KEY (`id_hoja_de_vida`),
  KEY `seguimiento_hoja_de__estudiante_id_958e80d4_fk_seguimien` (`estudiante_id`),
  CONSTRAINT `seguimiento_hoja_de__estudiante_id_958e80d4_fk_seguimien` FOREIGN KEY (`estudiante_id`) REFERENCES `seguimiento_estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_hoja_de_vida: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_hoja_de_vida`;
/*!40000 ALTER TABLE `seguimiento_hoja_de_vida` DISABLE KEYS */;
INSERT INTO `seguimiento_hoja_de_vida` (`id_hoja_de_vida`, `estudiante_id`) VALUES
	(1, 1),
	(2, 1);
/*!40000 ALTER TABLE `seguimiento_hoja_de_vida` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_informacion_laboral
CREATE TABLE IF NOT EXISTS `seguimiento_informacion_laboral` (
  `id_informacion_oferta_laboral` int(11) NOT NULL AUTO_INCREMENT,
  `cargo_ocupar` varchar(50) NOT NULL,
  `remuneracion_economica` decimal(8,2) NOT NULL,
  `actividades_desempenar` longtext NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  PRIMARY KEY (`id_informacion_oferta_laboral`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_informacion_laboral: ~5 rows (aproximadamente)
DELETE FROM `seguimiento_informacion_laboral`;
/*!40000 ALTER TABLE `seguimiento_informacion_laboral` DISABLE KEYS */;
INSERT INTO `seguimiento_informacion_laboral` (`id_informacion_oferta_laboral`, `cargo_ocupar`, `remuneracion_economica`, `actividades_desempenar`, `ciudad`) VALUES
	(1, 'Ing. de seguridad', 1231.00, 'Seguridad', 'loja'),
	(2, 'Ing. de desarrollo', 1980.00, 'desarrollo', 'loja'),
	(3, 'programador', 1234.00, 'qwe', '12'),
	(4, '12', 12.00, '12', '12'),
	(5, 'iNG EN REDES', 900.00, 'rEDES Y SISTEMAS', 'cuENCA');
/*!40000 ALTER TABLE `seguimiento_informacion_laboral` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_instruccion_formal
CREATE TABLE IF NOT EXISTS `seguimiento_instruccion_formal` (
  `id_instruccion_formal` int(11) NOT NULL AUTO_INCREMENT,
  `nivel_de_instruccion` varchar(100) NOT NULL,
  `instruccion_educativa` varchar(100) NOT NULL,
  `titulo_obtenido` varchar(100) NOT NULL,
  `no_del_registro_senescyt` varchar(100) NOT NULL,
  `hoja_de_vida_id` int(11) NOT NULL,
  PRIMARY KEY (`id_instruccion_formal`),
  KEY `seguimiento_instrucc_hoja_de_vida_id_4ae1d6d5_fk_seguimien` (`hoja_de_vida_id`),
  CONSTRAINT `seguimiento_instrucc_hoja_de_vida_id_4ae1d6d5_fk_seguimien` FOREIGN KEY (`hoja_de_vida_id`) REFERENCES `seguimiento_hoja_de_vida` (`id_hoja_de_vida`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_instruccion_formal: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_instruccion_formal`;
/*!40000 ALTER TABLE `seguimiento_instruccion_formal` DISABLE KEYS */;
INSERT INTO `seguimiento_instruccion_formal` (`id_instruccion_formal`, `nivel_de_instruccion`, `instruccion_educativa`, `titulo_obtenido`, `no_del_registro_senescyt`, `hoja_de_vida_id`) VALUES
	(1, 'Tercer nivel', 'Ingeniería', 'Ingeniero en Ciencias de la Computación', '890', 1),
	(2, 'Cuarto nivel', 'Postgrado', 'Magiter Sc.', '123', 1),
	(3, 'Tercer Nivel', 'Ingenieria', 'Ingeniero', '900', 2);
/*!40000 ALTER TABLE `seguimiento_instruccion_formal` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_logros_personales
CREATE TABLE IF NOT EXISTS `seguimiento_logros_personales` (
  `id_logros_personales` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_logro` varchar(50) NOT NULL,
  `descripcion` longtext NOT NULL,
  `hoja_de_vida_id` int(11) NOT NULL,
  PRIMARY KEY (`id_logros_personales`),
  KEY `seguimiento_logros_p_hoja_de_vida_id_cc204a86_fk_seguimien` (`hoja_de_vida_id`),
  CONSTRAINT `seguimiento_logros_p_hoja_de_vida_id_cc204a86_fk_seguimien` FOREIGN KEY (`hoja_de_vida_id`) REFERENCES `seguimiento_hoja_de_vida` (`id_hoja_de_vida`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_logros_personales: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_logros_personales`;
/*!40000 ALTER TABLE `seguimiento_logros_personales` DISABLE KEYS */;
INSERT INTO `seguimiento_logros_personales` (`id_logros_personales`, `tipo_logro`, `descripcion`, `hoja_de_vida_id`) VALUES
	(1, 'Logro personal', 'Fue un logro bonito', 1),
	(2, 'Muy bueno', 'es un logro que me costó sacar', 1),
	(3, 'Logro 2023', 'Fue un logro en el 2033', 2);
/*!40000 ALTER TABLE `seguimiento_logros_personales` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_mejor_graduado
CREATE TABLE IF NOT EXISTS `seguimiento_mejor_graduado` (
  `id_mejor_graduado` int(11) NOT NULL AUTO_INCREMENT,
  `nota_Grado` decimal(5,2) NOT NULL,
  `estudiante_id` int(11) NOT NULL,
  `periodo_academico_id` int(11) NOT NULL,
  PRIMARY KEY (`id_mejor_graduado`),
  KEY `seguimiento_mejor_gr_estudiante_id_2415a0ad_fk_seguimien` (`estudiante_id`),
  KEY `seguimiento_mejor_gr_periodo_academico_id_87f5ce9f_fk_seguimien` (`periodo_academico_id`),
  CONSTRAINT `seguimiento_mejor_gr_estudiante_id_2415a0ad_fk_seguimien` FOREIGN KEY (`estudiante_id`) REFERENCES `seguimiento_estudiante` (`id_estudiante`),
  CONSTRAINT `seguimiento_mejor_gr_periodo_academico_id_87f5ce9f_fk_seguimien` FOREIGN KEY (`periodo_academico_id`) REFERENCES `seguimiento_periodo_academico` (`id_periodo_academico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_mejor_graduado: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_mejor_graduado`;
/*!40000 ALTER TABLE `seguimiento_mejor_graduado` DISABLE KEYS */;
/*!40000 ALTER TABLE `seguimiento_mejor_graduado` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_oferta_laboral
CREATE TABLE IF NOT EXISTS `seguimiento_oferta_laboral` (
  `id_oferta_laboral` int(11) NOT NULL AUTO_INCREMENT,
  `carrera_id` int(11) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  `encuesta_id` int(11) DEFAULT NULL,
  `informacion_laboral_id` int(11) NOT NULL,
  PRIMARY KEY (`id_oferta_laboral`),
  KEY `seguimiento_oferta_l_carrera_id_936d9be7_fk_seguimien` (`carrera_id`),
  KEY `seguimiento_oferta_l_empresa_id_948f2a02_fk_seguimien` (`empresa_id`),
  KEY `seguimiento_oferta_l_encuesta_id_2b9bc89e_fk_seguimien` (`encuesta_id`),
  KEY `seguimiento_oferta_l_informacion_laboral__916831ea_fk_seguimien` (`informacion_laboral_id`),
  CONSTRAINT `seguimiento_oferta_l_carrera_id_936d9be7_fk_seguimien` FOREIGN KEY (`carrera_id`) REFERENCES `seguimiento_carrera` (`id_carrera`),
  CONSTRAINT `seguimiento_oferta_l_empresa_id_948f2a02_fk_seguimien` FOREIGN KEY (`empresa_id`) REFERENCES `seguimiento_empresa` (`id_empresa`),
  CONSTRAINT `seguimiento_oferta_l_encuesta_id_2b9bc89e_fk_seguimien` FOREIGN KEY (`encuesta_id`) REFERENCES `seguimiento_encuesta_laboral` (`id_encuesta_laboral`),
  CONSTRAINT `seguimiento_oferta_l_informacion_laboral__916831ea_fk_seguimien` FOREIGN KEY (`informacion_laboral_id`) REFERENCES `seguimiento_informacion_laboral` (`id_informacion_oferta_laboral`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_oferta_laboral: ~4 rows (aproximadamente)
DELETE FROM `seguimiento_oferta_laboral`;
/*!40000 ALTER TABLE `seguimiento_oferta_laboral` DISABLE KEYS */;
INSERT INTO `seguimiento_oferta_laboral` (`id_oferta_laboral`, `carrera_id`, `empresa_id`, `encuesta_id`, `informacion_laboral_id`) VALUES
	(1, 1, 1, NULL, 1),
	(2, 1, 2, NULL, 2),
	(3, 2, 2, NULL, 3),
	(5, 2, 2, NULL, 5);
/*!40000 ALTER TABLE `seguimiento_oferta_laboral` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_periodo_academico
CREATE TABLE IF NOT EXISTS `seguimiento_periodo_academico` (
  `id_periodo_academico` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_inicio` datetime(6) NOT NULL,
  `fecha_fin` datetime(6) NOT NULL,
  PRIMARY KEY (`id_periodo_academico`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_periodo_academico: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_periodo_academico`;
/*!40000 ALTER TABLE `seguimiento_periodo_academico` DISABLE KEYS */;
/*!40000 ALTER TABLE `seguimiento_periodo_academico` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_preferencias_laborales
CREATE TABLE IF NOT EXISTS `seguimiento_preferencias_laborales` (
  `id_preferencias_laborales` int(11) NOT NULL AUTO_INCREMENT,
  `sector` varchar(100) NOT NULL,
  `aspiracion_salarial` decimal(6,2) NOT NULL,
  `hoja_de_vida_id` int(11) NOT NULL,
  PRIMARY KEY (`id_preferencias_laborales`),
  KEY `seguimiento_preferen_hoja_de_vida_id_1e5c2363_fk_seguimien` (`hoja_de_vida_id`),
  CONSTRAINT `seguimiento_preferen_hoja_de_vida_id_1e5c2363_fk_seguimien` FOREIGN KEY (`hoja_de_vida_id`) REFERENCES `seguimiento_hoja_de_vida` (`id_hoja_de_vida`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_preferencias_laborales: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_preferencias_laborales`;
/*!40000 ALTER TABLE `seguimiento_preferencias_laborales` DISABLE KEYS */;
INSERT INTO `seguimiento_preferencias_laborales` (`id_preferencias_laborales`, `sector`, `aspiracion_salarial`, `hoja_de_vida_id`) VALUES
	(1, 'Privado', 900.00, 1),
	(2, 'Publico', 1200.00, 2);
/*!40000 ALTER TABLE `seguimiento_preferencias_laborales` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_pregunta
CREATE TABLE IF NOT EXISTS `seguimiento_pregunta` (
  `id_pregunta` int(11) NOT NULL AUTO_INCREMENT,
  `texto_pregunta` varchar(300) NOT NULL,
  `encuesta_laboral_id` int(11) NOT NULL,
  PRIMARY KEY (`id_pregunta`),
  KEY `seguimiento_pregunta_encuesta_laboral_id_89e9974a_fk_seguimien` (`encuesta_laboral_id`),
  CONSTRAINT `seguimiento_pregunta_encuesta_laboral_id_89e9974a_fk_seguimien` FOREIGN KEY (`encuesta_laboral_id`) REFERENCES `seguimiento_encuesta_laboral` (`id_encuesta_laboral`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_pregunta: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_pregunta`;
/*!40000 ALTER TABLE `seguimiento_pregunta` DISABLE KEYS */;
/*!40000 ALTER TABLE `seguimiento_pregunta` ENABLE KEYS */;

-- Volcando estructura para tabla seguimiento.seguimiento_referencias_personales
CREATE TABLE IF NOT EXISTS `seguimiento_referencias_personales` (
  `id_referencias_personales` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(100) NOT NULL,
  `telefono` int(11) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `hoja_de_vida_id` int(11) NOT NULL,
  PRIMARY KEY (`id_referencias_personales`),
  UNIQUE KEY `correo` (`correo`),
  KEY `seguimiento_referenc_hoja_de_vida_id_c3feddf7_fk_seguimien` (`hoja_de_vida_id`),
  CONSTRAINT `seguimiento_referenc_hoja_de_vida_id_c3feddf7_fk_seguimien` FOREIGN KEY (`hoja_de_vida_id`) REFERENCES `seguimiento_hoja_de_vida` (`id_hoja_de_vida`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;

-- Volcando datos para la tabla seguimiento.seguimiento_referencias_personales: ~0 rows (aproximadamente)
DELETE FROM `seguimiento_referencias_personales`;
/*!40000 ALTER TABLE `seguimiento_referencias_personales` DISABLE KEYS */;
INSERT INTO `seguimiento_referencias_personales` (`id_referencias_personales`, `nombres`, `telefono`, `correo`, `hoja_de_vida_id`) VALUES
	(1, 'Marco Fernandez', 98190, 'marco@gmail.com', 1),
	(2, 'Alberto', 9817, 'alb@gmail.com', 2);
/*!40000 ALTER TABLE `seguimiento_referencias_personales` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
