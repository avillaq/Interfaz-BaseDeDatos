-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-06-2024 a las 19:55:22
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ventacigarrillo`
--
CREATE DATABASE IF NOT EXISTS `ventacigarrillo` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `ventacigarrillo`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `almacen`
--

CREATE TABLE `almacen` (
  `AlmIdeFisEst` varchar(10) NOT NULL,
  `AlmCigMar` varchar(20) NOT NULL,
  `AlmCigFil` char(1) NOT NULL,
  `AlmCigCol` char(1) NOT NULL,
  `AlmClaTra` varchar(10) NOT NULL,
  `AlmCarMen` char(1) NOT NULL,
  `AlmUniSto` int(4) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `almacen`
--

INSERT INTO `almacen` (`AlmIdeFisEst`, `AlmCigMar`, `AlmCigFil`, `AlmCigCol`, `AlmClaTra`, `AlmCarMen`, `AlmUniSto`) VALUES
('1', 'Benson & Hedges', 'S', 'R', 'Light', 'S', 120),
('1', 'Benson & Hedges', 'S', 'R', 'Normal', 'N', 100),
('1', 'Camel', 'S', 'R', 'Light', 'N', 200),
('10', 'L&M', 'S', 'R', 'UltraLight', 'N', 120),
('10', 'Lucky Strike', 'S', 'R', 'Normal', 'S', 100),
('10', 'Marlboro', 'S', 'R', 'Normal', 'N', 170),
('11', 'Lucky Strike', 'N', 'N', 'Light', 'N', 90),
('11', 'Marlboro', 'S', 'R', 'Light', 'S', 160),
('11', 'Salem', 'N', 'N', 'Light', 'N', 100),
('11', 'Winston', 'S', 'R', 'Light', 'S', 140),
('12', 'Pall Mall', 'N', 'N', 'Normal', 'N', 80),
('12', 'Salem', 'S', 'R', 'Normal', 'S', 170),
('14', 'Pall Mall', 'S', 'R', 'Light', 'N', 70),
('14', 'Salem', 'S', 'R', 'Normal', 'S', 110),
('15', 'Parliament', 'N', 'N', 'UltraLight', 'S', 90),
('15', 'Parliament', 'S', 'R', 'Normal', 'N', 100),
('15', 'Winston', 'S', 'R', 'Normal', 'N', 150),
('16', 'Marlboro', 'S', 'R', 'Light', 'S', 180),
('16', 'Parliament', 'S', 'R', 'Normal', 'N', 95),
('16', 'Winston', 'S', 'R', 'Normal', 'N', 180),
('17', 'Camel', 'S', 'R', 'Light', 'N', 200),
('17', 'Gudang Garam', 'S', 'N', 'Light', 'N', 95),
('17', 'Winston', 'S', 'R', 'Light', 'S', 130),
('18', 'Dunhill', 'S', 'R', 'UltraLight', 'N', 115),
('18', 'Kent', 'S', 'R', 'Light', 'S', 140),
('19', 'Benson & Hedges', 'S', 'R', 'Normal', 'N', 125),
('19', 'Pall Mall', 'S', 'R', 'Light', 'N', 145),
('2', 'Camel', 'N', 'N', 'Normal', 'N', 150),
('20', 'Kent', 'N', 'N', 'Normal', 'N', 175),
('21', 'Chesterfield', 'S', 'R', 'Normal', 'S', 105),
('21', 'L&M', 'S', 'R', 'UltraLight', 'N', 110),
('22', 'Djarum', 'S', 'N', 'Light', 'N', 155),
('23', 'Gudang Garam', 'S', 'R', 'Normal', 'S', 165),
('23', 'Lucky Strike', 'S', 'R', 'Normal', 'S', 115),
('24', 'Camel', 'N', 'N', 'Normal', 'N', 120),
('24', 'Salem', 'N', 'N', 'Light', 'N', 95),
('25', 'Parliament', 'N', 'N', 'UltraLight', 'S', 80),
('25', 'Winston', 'S', 'R', 'Light', 'S', 90),
('26', 'Dunhill', 'S', 'R', 'UltraLight', 'N', 135),
('27', 'Benson & Hedges', 'S', 'R', 'Light', 'S', 165),
('27', 'L&M', 'S', 'R', 'UltraLight', 'N', 150),
('28', 'Pall Mall', 'N', 'N', 'Normal', 'N', 190),
('29', 'Chesterfield', 'N', 'N', 'UltraLight', 'N', 145),
('3', 'Chesterfield', 'S', 'R', 'Normal', 'S', 90),
('30', 'Benson & Hedges', 'S', 'R', 'Light', 'S', 135),
('30', 'Djarum', 'S', 'N', 'Light', 'N', 165),
('30', 'Lucky Strike', 'N', 'N', 'Light', 'N', 200),
('4', 'Chesterfield', 'N', 'N', 'UltraLight', 'N', 80),
('4', 'Djarum', 'S', 'N', 'Light', 'N', 110),
('4', 'Djarum', 'S', 'R', 'Normal', 'S', 130),
('5', 'Dunhill', 'N', 'N', 'Normal', 'N', 160),
('5', 'Kent', 'N', 'N', 'Normal', 'N', 200),
('6', 'Dunhill', 'S', 'R', 'UltraLight', 'N', 140),
('6', 'Gudang Garam', 'S', 'N', 'Light', 'N', 60),
('7', 'Gudang Garam', 'S', 'R', 'Normal', 'S', 70),
('7', 'Kent', 'S', 'R', 'Light', 'S', 180),
('8', 'Kool', 'S', 'N', 'Light', 'S', 140),
('8', 'Kool', 'S', 'R', 'Normal', 'N', 150),
('9', 'L&M', 'N', 'N', 'Normal', 'N', 130);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cigarrillo`
--

CREATE TABLE `cigarrillo` (
  `CigMar` varchar(20) NOT NULL,
  `CigFil` char(1) NOT NULL,
  `CigCol` char(1) NOT NULL,
  `CigClaTra` varchar(10) NOT NULL,
  `CigCarMen` char(1) NOT NULL,
  `CigCanNic` decimal(2,1) DEFAULT NULL,
  `CigCanAlq` decimal(4,2) DEFAULT NULL,
  `CigPreVen` decimal(3,2) DEFAULT NULL,
  `CigPreCos` decimal(3,2) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `cigarrillo`
--

INSERT INTO `cigarrillo` (`CigMar`, `CigFil`, `CigCol`, `CigClaTra`, `CigCarMen`, `CigCanNic`, `CigCanAlq`, `CigPreVen`, `CigPreCos`) VALUES
('Benson & Hedges', 'S', 'R', 'Light', 'S', '0.8', '8.00', '5.50', '3.00'),
('Benson & Hedges', 'S', 'R', 'Normal', 'N', '1.2', '12.00', '5.00', '2.50'),
('Camel', 'N', 'N', 'Normal', 'N', '1.1', '10.50', '4.80', '2.30'),
('Camel', 'S', 'R', 'Light', 'N', '0.7', '7.50', '5.00', '2.70'),
('Chesterfield', 'N', 'N', 'UltraLight', 'N', '0.5', '5.00', '5.20', '2.90'),
('Chesterfield', 'S', 'R', 'Normal', 'S', '1.3', '12.50', '4.90', '2.40'),
('Djarum', 'S', 'N', 'Light', 'N', '0.9', '9.50', '6.20', '3.10'),
('Djarum', 'S', 'R', 'Normal', 'S', '1.5', '15.00', '6.50', '3.20'),
('Dunhill', 'N', 'N', 'Normal', 'N', '1.1', '10.00', '5.80', '2.80'),
('Dunhill', 'S', 'R', 'UltraLight', 'N', '0.6', '6.00', '6.00', '3.30'),
('Gudang Garam', 'S', 'N', 'Light', 'N', '0.8', '8.50', '6.30', '3.20'),
('Gudang Garam', 'S', 'R', 'Normal', 'S', '1.4', '14.00', '6.70', '3.50'),
('Kent', 'N', 'N', 'Normal', 'N', '1.2', '11.50', '5.90', '2.70'),
('Kent', 'S', 'R', 'Light', 'S', '0.9', '9.00', '6.10', '3.00'),
('Kool', 'S', 'N', 'Light', 'S', '0.7', '7.80', '5.70', '2.90'),
('Kool', 'S', 'R', 'Normal', 'N', '1.1', '10.80', '5.40', '2.60'),
('L&M', 'N', 'N', 'Normal', 'N', '1.3', '12.30', '5.50', '2.50'),
('L&M', 'S', 'R', 'UltraLight', 'N', '0.6', '6.50', '5.90', '3.10'),
('Lucky Strike', 'N', 'N', 'Light', 'N', '1.3', '6.80', '5.00', '3.20'),
('Lucky Strike', 'S', 'R', 'Normal', 'S', '1.2', '12.00', '5.60', '2.70'),
('Marlboro', 'S', 'R', 'Light', 'S', '0.7', '7.50', '6.20', '3.30'),
('Marlboro', 'S', 'R', 'Normal', 'N', '1.1', '11.00', '6.00', '3.00'),
('Pall Mall', 'N', 'N', 'Normal', 'N', '1.0', '10.00', '4.70', '2.20'),
('Pall Mall', 'S', 'R', 'Light', 'N', '0.6', '6.00', '4.90', '2.40'),
('Parliament', 'N', 'N', 'UltraLight', 'S', '0.5', '5.50', '5.40', '2.80'),
('Parliament', 'S', 'R', 'Normal', 'N', '1.1', '11.20', '5.10', '2.60'),
('Salem', 'N', 'N', 'Light', 'N', '0.7', '7.70', '5.90', '2.90'),
('Salem', 'S', 'R', 'Normal', 'S', '1.3', '13.00', '5.70', '2.80'),
('Winston', 'S', 'R', 'Light', 'S', '0.8', '8.80', '6.00', '3.10'),
('Winston', 'S', 'R', 'Normal', 'N', '1.2', '12.50', '5.80', '2.90');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compra`
--

CREATE TABLE `compra` (
  `ComIdeFisEst` varchar(10) NOT NULL,
  `ComMar` varchar(20) NOT NULL,
  `ComFil` char(1) NOT NULL,
  `ComCol` char(1) NOT NULL,
  `ComClaTra` varchar(10) NOT NULL,
  `ComCarMen` char(1) NOT NULL,
  `ComFec` date NOT NULL,
  `ComCan` int(4) DEFAULT NULL,
  `ComPre` decimal(10,2) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `compra`
--

INSERT INTO `compra` (`ComIdeFisEst`, `ComMar`, `ComFil`, `ComCol`, `ComClaTra`, `ComCarMen`, `ComFec`, `ComCan`, `ComPre`) VALUES
('1', 'Benson & Hedges', 'S', 'R', 'Light', 'S', '2020-01-10', 20, '5.50'),
('1', 'Benson & Hedges', 'S', 'R', 'Normal', 'N', '2021-02-15', 25, '6.00'),
('1', 'Camel', 'S', 'R', 'Light', 'N', '2022-03-20', 30, '6.50'),
('10', 'L&M', 'S', 'R', 'UltraLight', 'N', '2019-04-25', 10, '4.50'),
('10', 'Lucky Strike', 'S', 'R', 'Normal', 'S', '2023-05-30', 15, '5.00'),
('10', 'Marlboro', 'S', 'R', 'Normal', 'N', '2024-06-05', 20, '6.50'),
('11', 'Lucky Strike', 'N', 'N', 'Light', 'N', '2018-07-10', 10, '4.00'),
('11', 'Marlboro', 'S', 'R', 'Light', 'S', '2017-08-15', 20, '5.50'),
('11', 'Salem', 'N', 'N', 'Light', 'N', '2016-09-20', 15, '5.00'),
('11', 'Winston', 'S', 'R', 'Light', 'S', '2015-10-25', 25, '6.00'),
('12', 'Pall Mall', 'N', 'N', 'Normal', 'N', '2014-11-30', 30, '4.50'),
('12', 'Salem', 'S', 'R', 'Normal', 'S', '2013-12-05', 20, '5.50'),
('14', 'Pall Mall', 'S', 'R', 'Light', 'N', '2012-01-10', 15, '5.00'),
('14', 'Salem', 'S', 'R', 'Normal', 'S', '2011-02-15', 25, '6.00'),
('15', 'Parliament', 'N', 'N', 'UltraLight', 'S', '2010-03-20', 10, '4.00'),
('15', 'Parliament', 'S', 'R', 'Normal', 'N', '2009-04-25', 20, '5.50'),
('15', 'Winston', 'S', 'R', 'Normal', 'N', '2008-05-30', 15, '5.00'),
('16', 'Marlboro', 'S', 'R', 'Light', 'S', '2007-06-05', 25, '6.00'),
('16', 'Parliament', 'S', 'R', 'Normal', 'N', '2006-07-10', 20, '5.50'),
('16', 'Winston', 'S', 'R', 'Normal', 'N', '2005-08-15', 30, '6.50'),
('17', 'Camel', 'S', 'R', 'Light', 'N', '2004-09-20', 10, '4.50'),
('17', 'Gudang Garam', 'S', 'N', 'Light', 'N', '2003-10-25', 15, '5.00'),
('17', 'Winston', 'S', 'R', 'Light', 'S', '2002-11-30', 20, '5.50'),
('18', 'Dunhill', 'S', 'R', 'UltraLight', 'N', '2001-12-05', 25, '6.00'),
('18', 'Kent', 'S', 'R', 'Light', 'S', '2000-01-10', 30, '6.50'),
('19', 'Benson & Hedges', 'S', 'R', 'Normal', 'N', '2019-02-15', 10, '4.50'),
('19', 'Pall Mall', 'S', 'R', 'Light', 'N', '2018-03-20', 15, '5.00'),
('2', 'Camel', 'N', 'N', 'Normal', 'N', '2017-04-25', 20, '5.50'),
('20', 'Kent', 'N', 'N', 'Normal', 'N', '2016-05-30', 25, '6.00'),
('21', 'Chesterfield', 'S', 'R', 'Normal', 'S', '2015-06-05', 30, '6.50'),
('21', 'L&M', 'S', 'R', 'UltraLight', 'N', '2014-07-10', 10, '4.50'),
('22', 'Djarum', 'S', 'N', 'Light', 'N', '2013-08-15', 15, '5.00'),
('23', 'Gudang Garam', 'S', 'R', 'Normal', 'S', '2012-09-20', 20, '5.50'),
('23', 'Lucky Strike', 'S', 'R', 'Normal', 'S', '2011-10-25', 25, '6.00'),
('24', 'Camel', 'N', 'N', 'Normal', 'N', '2010-11-30', 30, '6.50'),
('24', 'Salem', 'N', 'N', 'Light', 'N', '2009-12-05', 10, '4.50'),
('25', 'Parliament', 'N', 'N', 'UltraLight', 'S', '2008-01-10', 15, '5.00'),
('25', 'Winston', 'S', 'R', 'Light', 'S', '2007-02-15', 20, '5.50'),
('26', 'Dunhill', 'S', 'R', 'UltraLight', 'N', '2006-03-20', 25, '6.00'),
('27', 'Benson & Hedges', 'S', 'R', 'Light', 'S', '2005-04-25', 30, '6.50'),
('27', 'L&M', 'S', 'R', 'UltraLight', 'N', '2004-05-30', 10, '4.50'),
('28', 'Pall Mall', 'N', 'N', 'Normal', 'N', '2003-06-05', 15, '5.00'),
('29', 'Chesterfield', 'N', 'N', 'UltraLight', 'N', '2002-07-10', 20, '5.50'),
('3', 'Chesterfield', 'S', 'R', 'Normal', 'S', '2001-08-15', 25, '6.00'),
('3', 'Chesterfield', 'S', 'R', 'Normal', 'S', '2004-03-24', 20, '3.50'),
('30', 'Benson & Hedges', 'S', 'R', 'Light', 'S', '2000-09-20', 30, '6.50'),
('30', 'Djarum', 'S', 'N', 'Light', 'N', '2019-10-25', 10, '4.50'),
('30', 'Lucky Strike', 'N', 'N', 'Light', 'N', '2018-11-30', 15, '5.00'),
('4', 'Chesterfield', 'N', 'N', 'UltraLight', 'N', '2017-12-05', 30, '6.50'),
('4', 'Djarum', 'S', 'N', 'Light', 'N', '2016-01-10', 25, '6.00'),
('5', 'Dunhill', 'N', 'N', 'Normal', 'N', '2013-06-13', 35, '4.50'),
('5', 'Dunhill', 'N', 'N', 'Normal', 'N', '2015-02-15', 30, '6.50'),
('5', 'Kent', 'N', 'N', 'Normal', 'N', '2014-03-20', 10, '4.50'),
('6', 'Dunhill', 'S', 'R', 'UltraLight', 'N', '2013-04-25', 15, '5.00'),
('6', 'Gudang Garam', 'S', 'N', 'Light', 'N', '2012-05-30', 20, '5.50'),
('7', 'Gudang Garam', 'S', 'R', 'Normal', 'S', '2011-06-05', 25, '6.00'),
('7', 'Kent', 'S', 'R', 'Light', 'S', '2010-07-10', 30, '6.50'),
('8', 'Kool', 'S', 'N', 'Light', 'S', '2008-09-20', 15, '5.00'),
('8', 'Kool', 'S', 'R', 'Normal', 'N', '2009-08-15', 10, '4.50'),
('9', 'L&M', 'N', 'N', 'Normal', 'N', '2007-10-25', 20, '5.50');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estanco`
--

CREATE TABLE `estanco` (
  `EstIdeFisEst` varchar(10) NOT NULL,
  `EstNumExp` int(10) NOT NULL,
  `EstNom` varchar(30) NOT NULL,
  `EstUbi` int(10) NOT NULL
) ;

--
-- Volcado de datos para la tabla `estanco`
--

INSERT INTO `estanco` (`EstIdeFisEst`, `EstNumExp`, `EstNom`, `EstUbi`) VALUES
('1', 1001, 'Estanco A', 1),
('10', 1008, 'Estanco J', 16),
('11', 1009, 'Estanco K', 5),
('12', 1010, 'Estanco L', 7),
('14', 1011, 'Estanco N', 11),
('15', 1011, 'Estanco O', 13),
('16', 1012, 'Estanco P', 15),
('17', 1013, 'Estanco Q', 17),
('18', 1014, 'Estanco R', 20),
('19', 1015, 'Estanco S', 23),
('2', 1001, 'Estanco B', 24),
('20', 1016, 'Estanco T', 26),
('21', 1016, 'Estanco U', 29),
('22', 1017, 'Estanco V', 18),
('23', 1018, 'Estanco W', 19),
('24', 1019, 'Estanco X', 2),
('25', 1020, 'Estanco Y', 21),
('26', 1021, 'Estanco Z', 22),
('27', 1021, 'Estanco AA', 25),
('28', 1022, 'Estanco BB', 30),
('29', 1023, 'Estanco CC', 28),
('3', 1002, 'Estanco C', 3),
('30', 1023, 'Estanco DD', 27),
('4', 1003, 'Estanco D', 10),
('5', 1004, 'Estanco XXX', 8),
('6', 1005, 'Estanco F', 12),
('7', 1006, 'Estanco G', 6),
('8', 1006, 'Estanco H', 14),
('9', 1007, 'Estanco I', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fabricante`
--

CREATE TABLE `fabricante` (
  `FabNom` varchar(30) NOT NULL,
  `FabPai` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `fabricante`
--

INSERT INTO `fabricante` (`FabNom`, `FabPai`) VALUES
('Altria', 'USA'),
('British American Tobacco', 'UK'),
('Djarum', 'Indonesia'),
('Gudang Garam', 'Indonesia'),
('Imperial Brands', 'UK'),
('Japan Tobacco', 'Japon'),
('Philip Morris', 'USA'),
('Reynolds American', 'USA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `produccion`
--

CREATE TABLE `produccion` (
  `ProMar` varchar(20) NOT NULL,
  `ProFabNom` varchar(30) DEFAULT NULL,
  `ProCar` int(2) DEFAULT 10,
  `ProEmb` int(2) DEFAULT 20
) ;

--
-- Volcado de datos para la tabla `produccion`
--

INSERT INTO `produccion` (`ProMar`, `ProFabNom`, `ProCar`, `ProEmb`) VALUES
('Benson & Hedges', 'Philip Morris', 10, 20),
('Camel', 'Reynolds American', 50, 300),
('Chesterfield', 'Philip Morris', 10, 20),
('Djarum', 'Djarum', 10, 30),
('Dunhill', 'British American Tobacco', 10, 20),
('Gudang Garam', 'Gudang Garam', 10, 60),
('Kent', 'British American Tobacco', 10, 20),
('Kool', 'British American Tobacco', 32, 85),
('L&M', 'Philip Morris', 20, 650),
('Lucky Strike', 'British American Tobacco', 10, 20),
('Marlboro', 'Philip Morris', 45, 135),
('Pall Mall', 'British American Tobacco', 15, 40),
('Parliament', 'Philip Morris', 24, 30),
('Salem', 'Japan Tobacco', 15, 65),
('Winston', 'Japan Tobacco', 50, 205);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubigeo`
--

CREATE TABLE `ubigeo` (
  `UbiCod` int(10) NOT NULL,
  `UbiLoc` varchar(15) NOT NULL,
  `UbiPro` varchar(15) NOT NULL,
  `UbiDic` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ubigeo`
--

INSERT INTO `ubigeo` (`UbiCod`, `UbiLoc`, `UbiPro`, `UbiDic`) VALUES
(1, 'Cerro Colorado', 'Arequipa', 'Calle Miraflores 135'),
(2, 'Mar de Plata', 'Buenos Aires', 'Av. Corrientes 1470'),
(3, 'Rosario', 'Santa Fe', 'Av. Oroño 789'),
(4, 'Mar de Plata', 'Buenos Aires', 'Av. Colón 456'),
(5, 'Salta', 'Salta', 'Calle Mitre 125'),
(6, 'Bariloche', 'Río Negro', 'Av. Bustillo 25'),
(7, 'La Plata', 'Buenos Aires', 'Calle 28 de Julio 96'),
(8, 'San Miguel', 'Tucumán', 'Av. Sarmiento 734'),
(9, 'Neuquén', 'Neuquén', 'Calle Belgrano 365'),
(10, 'Córdoba', 'Córdoba', 'Calle Rivadavia 123'),
(11, 'Mendoza', 'Mendoza', 'Av. San Martín 456'),
(12, 'San Juan', 'San Juan', 'Calle Libertador 789'),
(13, 'Tigre', 'Buenos Aires', 'Av. Liniers 1011'),
(14, 'Bahía Blanca', 'Buenos Aires', 'Calle Alsina 202'),
(15, 'San Rafael', 'Mendoza', 'Calle Balloffet 333'),
(16, 'Trelew', 'Chubut', 'Av. Fontana 444'),
(17, 'Comodoro Rivada', 'Chubut', 'Calle Rivadavia 555'),
(18, 'Posadas', 'Misiones', 'Av. Uruguay 666'),
(19, 'Resistencia', 'Chaco', 'Calle Güemes 777'),
(20, 'Corrientes', 'Corrientes', 'Av. 3 de Abril 888'),
(21, 'Formosa', 'Formosa', 'Calle San Martín 999'),
(22, 'Santa Rosa', 'La Pampa', 'Av. Luro 111'),
(23, 'San Luis', 'San Luis', 'Calle Rivadavia 222'),
(24, 'Río Gallegos', 'Santa Cruz', 'Av. Kirchner 333'),
(25, 'Viedma', 'Río Negro', 'Calle Moreno 444'),
(26, 'Paraná', 'Entre Ríos', 'Av. Urquiza 555'),
(27, 'Santa Fe', 'Santa Fe', 'Calle San Martín 666'),
(28, 'San Fernando de', 'Catamarca', 'Av. Güemes 777'),
(29, 'La Rioja', 'La Rioja', 'Calle Rivadavia 888'),
(30, 'San Salvador', 'Jujuy', 'Av. El Éxodo 999');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `VenIdeFisEst` varchar(10) NOT NULL,
  `VenMar` varchar(20) NOT NULL,
  `VenFil` char(1) NOT NULL,
  `VenCol` char(1) NOT NULL,
  `VenClaTra` varchar(10) NOT NULL,
  `VenCarMen` char(1) NOT NULL,
  `VenFec` date NOT NULL,
  `VenCan` int(4) DEFAULT NULL,
  `VenPre` decimal(10,2) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `venta`
--

INSERT INTO `venta` (`VenIdeFisEst`, `VenMar`, `VenFil`, `VenCol`, `VenClaTra`, `VenCarMen`, `VenFec`, `VenCan`, `VenPre`) VALUES
('1', 'Benson & Hedges', 'S', 'R', 'Light', 'S', '2000-01-15', 50, '5.50'),
('1', 'Benson & Hedges', 'S', 'R', 'Normal', 'N', '2010-05-22', 45, '9.10'),
('1', 'Camel', 'S', 'R', 'Light', 'N', '2015-09-10', 60, '8.75'),
('10', 'L&M', 'S', 'R', 'UltraLight', 'N', '2020-03-14', 60, '8.50'),
('10', 'Lucky Strike', 'S', 'R', 'Normal', 'S', '2023-11-07', 40, '6.80'),
('10', 'Marlboro', 'S', 'R', 'Normal', 'N', '2005-12-25', 90, '11.00'),
('11', 'Lucky Strike', 'N', 'N', 'Light', 'N', '2009-03-08', 15, '4.60'),
('11', 'Marlboro', 'S', 'R', 'Light', 'S', '2011-02-28', 85, '8.20'),
('11', 'Salem', 'N', 'N', 'Light', 'N', '2000-06-15', 55, '9.50'),
('11', 'Winston', 'S', 'R', 'Light', 'S', '2022-08-30', 70, '5.60'),
('12', 'Pall Mall', 'N', 'N', 'Normal', 'N', '2003-11-15', 45, '8.30'),
('12', 'Salem', 'S', 'R', 'Normal', 'S', '2001-04-20', 70, '10.00'),
('14', 'Pall Mall', 'S', 'R', 'Light', 'N', '2004-05-22', 80, '9.40'),
('14', 'Salem', 'S', 'R', 'Normal', 'S', '2006-12-19', 55, '7.50'),
('15', 'Parliament', 'N', 'N', 'UltraLight', 'S', '2012-10-05', 60, '6.50'),
('15', 'Parliament', 'S', 'R', 'Normal', 'N', '2014-09-11', 65, '8.80'),
('15', 'Winston', 'S', 'R', 'Normal', 'N', '2007-03-26', 50, '9.90'),
('16', 'Marlboro', 'S', 'R', 'Light', 'S', '2013-08-16', 75, '10.70'),
('16', 'Parliament', 'S', 'R', 'Normal', 'N', '2008-11-03', 90, '11.00'),
('16', 'Winston', 'S', 'R', 'Normal', 'N', '2016-05-12', 85, '8.20'),
('17', 'Camel', 'S', 'R', 'Light', 'N', '2009-07-27', 70, '7.60'),
('17', 'Gudang Garam', 'S', 'N', 'Light', 'N', '2021-01-01', 80, '9.10'),
('17', 'Winston', 'S', 'R', 'Light', 'S', '2024-02-29', 55, '6.90'),
('18', 'Dunhill', 'S', 'R', 'UltraLight', 'N', '2017-06-20', 45, '10.00'),
('18', 'Kent', 'S', 'R', 'Light', 'S', '2002-12-25', 70, '9.50'),
('19', 'Benson & Hedges', 'S', 'R', 'Normal', 'N', '2010-03-15', 65, '8.75'),
('19', 'Pall Mall', 'S', 'R', 'Light', 'N', '2003-07-10', 50, '7.20'),
('2', 'Camel', 'N', 'N', 'Normal', 'N', '2005-09-05', 55, '6.80'),
('20', 'Kent', 'N', 'N', 'Normal', 'N', '2020-11-20', 75, '9.70'),
('21', 'Chesterfield', 'S', 'R', 'Normal', 'S', '2012-12-12', 60, '10.30'),
('21', 'L&M', 'S', 'R', 'UltraLight', 'N', '2023-05-22', 80, '8.10'),
('22', 'Djarum', 'S', 'N', 'Light', 'N', '2015-01-18', 45, '9.90'),
('23', 'Gudang Garam', 'S', 'R', 'Normal', 'S', '2000-07-04', 70, '7.00'),
('23', 'Lucky Strike', 'S', 'R', 'Normal', 'S', '2006-06-25', 85, '10.90'),
('24', 'Camel', 'N', 'N', 'Normal', 'N', '2014-10-15', 65, '6.50'),
('24', 'Salem', 'N', 'N', 'Light', 'N', '2008-08-08', 90, '10.00'),
('25', 'Parliament', 'N', 'N', 'UltraLight', 'S', '2019-03-30', 50, '5.80'),
('25', 'Winston', 'S', 'R', 'Light', 'S', '2001-02-12', 75, '9.20'),
('26', 'Dunhill', 'S', 'R', 'UltraLight', 'N', '2021-06-14', 60, '8.50'),
('27', 'Benson & Hedges', 'S', 'R', 'Light', 'S', '2004-09-25', 65, '7.40'),
('27', 'L&M', 'S', 'R', 'UltraLight', 'N', '2009-01-13', 45, '6.20'),
('28', 'Pall Mall', 'N', 'N', 'Normal', 'N', '2016-03-22', 85, '10.40'),
('29', 'Chesterfield', 'N', 'N', 'UltraLight', 'N', '2011-12-05', 50, '8.30'),
('3', 'Chesterfield', 'S', 'R', 'Normal', 'S', '2003-10-19', 90, '9.10'),
('30', 'Benson & Hedges', 'S', 'R', 'Light', 'S', '2018-04-17', 70, '6.90'),
('30', 'Djarum', 'S', 'N', 'Light', 'N', '2013-05-22', 55, '7.80'),
('30', 'Lucky Strike', 'N', 'N', 'Light', 'N', '2006-11-29', 60, '8.50'),
('4', 'Chesterfield', 'N', 'N', 'UltraLight', 'N', '2022-07-30', 45, '9.50'),
('4', 'Djarum', 'S', 'N', 'Light', 'N', '2002-01-21', 90, '10.60'),
('4', 'Djarum', 'S', 'R', 'Normal', 'S', '2011-09-19', 75, '5.50'),
('5', 'Dunhill', 'N', 'N', 'Normal', 'N', '2008-03-13', 50, '6.90'),
('5', 'Kent', 'N', 'N', 'Normal', 'N', '2015-11-07', 85, '8.20'),
('6', 'Dunhill', 'S', 'R', 'UltraLight', 'N', '2001-08-24', 70, '10.10'),
('6', 'Gudang Garam', 'S', 'N', 'Light', 'N', '2012-10-30', 60, '9.30'),
('7', 'Gudang Garam', 'S', 'R', 'Normal', 'S', '2020-06-29', 45, '8.80'),
('7', 'Kent', 'S', 'R', 'Light', 'S', '2007-12-09', 90, '5.60'),
('8', 'Kool', 'S', 'N', 'Light', 'S', '2014-01-26', 75, '9.70'),
('8', 'Kool', 'S', 'R', 'Normal', 'N', '2016-11-03', 85, '10.50'),
('9', 'L&M', 'N', 'N', 'Normal', 'N', '2009-04-20', 65, '6.30'),
('9', 'L&M', 'N', 'N', 'Normal', 'N', '2013-07-18', 50, '8.10');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `almacen`
--
ALTER TABLE `almacen`
  ADD PRIMARY KEY (`AlmIdeFisEst`,`AlmCigMar`,`AlmCigFil`,`AlmCigCol`,`AlmClaTra`,`AlmCarMen`),
  ADD KEY `fk_alm_cig` (`AlmCigMar`,`AlmCigFil`,`AlmCigCol`,`AlmClaTra`,`AlmCarMen`);

--
-- Indices de la tabla `cigarrillo`
--
ALTER TABLE `cigarrillo`
  ADD PRIMARY KEY (`CigMar`,`CigFil`,`CigCol`,`CigClaTra`,`CigCarMen`);

--
-- Indices de la tabla `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`ComIdeFisEst`,`ComMar`,`ComFil`,`ComCol`,`ComClaTra`,`ComCarMen`,`ComFec`);

--
-- Indices de la tabla `estanco`
--
ALTER TABLE `estanco`
  ADD PRIMARY KEY (`EstIdeFisEst`),
  ADD UNIQUE KEY `sk_est` (`EstUbi`);

--
-- Indices de la tabla `fabricante`
--
ALTER TABLE `fabricante`
  ADD PRIMARY KEY (`FabNom`);

--
-- Indices de la tabla `produccion`
--
ALTER TABLE `produccion`
  ADD PRIMARY KEY (`ProMar`),
  ADD KEY `fk_pro_fab` (`ProFabNom`);

--
-- Indices de la tabla `ubigeo`
--
ALTER TABLE `ubigeo`
  ADD PRIMARY KEY (`UbiCod`);

--
-- Indices de la tabla `venta`
--
ALTER TABLE `venta`
  ADD PRIMARY KEY (`VenIdeFisEst`,`VenMar`,`VenFil`,`VenCol`,`VenClaTra`,`VenCarMen`,`VenFec`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `almacen`
--
ALTER TABLE `almacen`
  ADD CONSTRAINT `fk_Alm_est` FOREIGN KEY (`AlmIdeFisEst`) REFERENCES `estanco` (`EstIdeFisEst`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_alm_cig` FOREIGN KEY (`AlmCigMar`,`AlmCigFil`,`AlmCigCol`,`AlmClaTra`,`AlmCarMen`) REFERENCES `cigarrillo` (`CigMar`, `CigFil`, `CigCol`, `CigClaTra`, `CigCarMen`) ON DELETE CASCADE;

--
-- Filtros para la tabla `cigarrillo`
--
ALTER TABLE `cigarrillo`
  ADD CONSTRAINT `fk_cig_pro` FOREIGN KEY (`CigMar`) REFERENCES `produccion` (`ProMar`) ON DELETE CASCADE;

--
-- Filtros para la tabla `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `fk_com_alm` FOREIGN KEY (`ComIdeFisEst`,`ComMar`,`ComFil`,`ComCol`,`ComClaTra`,`ComCarMen`) REFERENCES `almacen` (`AlmIdeFisEst`, `AlmCigMar`, `AlmCigFil`, `AlmCigCol`, `AlmClaTra`, `AlmCarMen`) ON DELETE CASCADE;

--
-- Filtros para la tabla `estanco`
--
ALTER TABLE `estanco`
  ADD CONSTRAINT `fk_est_ubi` FOREIGN KEY (`EstUbi`) REFERENCES `ubigeo` (`UbiCod`) ON DELETE CASCADE;

--
-- Filtros para la tabla `produccion`
--
ALTER TABLE `produccion`
  ADD CONSTRAINT `fk_pro_fab` FOREIGN KEY (`ProFabNom`) REFERENCES `fabricante` (`FabNom`) ON DELETE CASCADE;

--
-- Filtros para la tabla `venta`
--
ALTER TABLE `venta`
  ADD CONSTRAINT `fk_ven_alm` FOREIGN KEY (`VenIdeFisEst`,`VenMar`,`VenFil`,`VenCol`,`VenClaTra`,`VenCarMen`) REFERENCES `almacen` (`AlmIdeFisEst`, `AlmCigMar`, `AlmCigFil`, `AlmCigCol`, `AlmClaTra`, `AlmCarMen`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
