-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-06-2024 a las 14:49:59
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
('Kool', 'N', 'R', 'SuperLight', 'N', '9.9', '23.00', '9.99', '9.99'),
('Pall Mall', 'N', 'N', 'SuperLight', 'N', '9.9', '20.00', '2.99', '6.99');

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
  `ComPre` int(8) DEFAULT NULL
) ;

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
('1', 1211111, 'NombreExp', 3);

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
('Djarum', 'Philip Morris', 10, 30),
('Dunhill', 'British American Tobacco', 10, 20),
('Gudang Garam', 'Gudang Garam', 10, 60),
('Kent', 'British American Tobacco', 10, 20),
('Kool', 'British American Tobacco', 32, 85),
('L&M', 'Philip Morris', 20, 650),
('Lucky Strike', 'British American Tobacco', 10, 20),
('Marlboro', 'Philip Morris', 45, 135),
('Pall Mall', 'British American Tobacco', 15, 40),
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
(1, 'Arequipa', 'Arequipa', 'Av. Brasil'),
(2, 'Peru', 'Arequipa', 'Av. Veneco 123'),
(3, 'Cerro Colorado', 'Arequipa', 'Calle Palomares 123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `venta`
--

CREATE TABLE `venta` (
  `VenIdeFistEst` varchar(10) NOT NULL,
  `VenMar` varchar(20) NOT NULL,
  `VenFil` char(1) NOT NULL,
  `VenCol` char(1) NOT NULL,
  `VenClaTra` varchar(10) NOT NULL,
  `VenCarMen` char(1) NOT NULL,
  `VenFec` date NOT NULL,
  `VenCan` int(4) DEFAULT NULL,
  `VenPre` int(8) DEFAULT NULL
) ;

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
  ADD UNIQUE KEY `sk_est` (`EstNumExp`),
  ADD KEY `fk_est_ubi` (`EstUbi`);

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
  ADD PRIMARY KEY (`VenIdeFistEst`,`VenMar`,`VenFil`,`VenCol`,`VenClaTra`,`VenCarMen`,`VenFec`);

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
  ADD CONSTRAINT `fk_ven_alm` FOREIGN KEY (`VenIdeFistEst`,`VenMar`,`VenFil`,`VenCol`,`VenClaTra`,`VenCarMen`) REFERENCES `almacen` (`AlmIdeFisEst`, `AlmCigMar`, `AlmCigFil`, `AlmCigCol`, `AlmClaTra`, `AlmCarMen`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
