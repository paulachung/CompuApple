-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-10-2024 a las 16:40:32
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tecnologia_v3`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `airpods`
--

CREATE TABLE `airpods` (
  `id` int(11) NOT NULL,
  `producttype` varchar(20) NOT NULL DEFAULT 'airpods',
  `img` varchar(255) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `batteryLifeAirpods` varchar(50) DEFAULT NULL,
  `noiseCancellation` tinyint(1) DEFAULT NULL,
  `sensoresAirpods` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `applevisionpro`
--

CREATE TABLE `applevisionpro` (
  `id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `screenSizeVison` varchar(50) DEFAULT NULL,
  `batteryVisionPro` varchar(50) DEFAULT NULL,
  `sensoresVisionPro` varchar(255) DEFAULT NULL,
  `modosVisionPro` varchar(255) DEFAULT NULL,
  `juegos` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `applewatch`
--

CREATE TABLE `applewatch` (
  `id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `batteryLifeWach` varchar(50) DEFAULT NULL,
  `sensoresWach` varchar(100) DEFAULT NULL,
  `modos` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ipad`
--

CREATE TABLE `ipad` (
  `id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `screenSizeIpad` varchar(50) DEFAULT NULL,
  `capacidadIpad` varchar(50) DEFAULT NULL,
  `memoriaipad` varchar(50) DEFAULT NULL,
  `procesadorIpad` varchar(100) DEFAULT NULL,
  `camaraIpad` varchar(100) DEFAULT NULL,
  `softwareIpad` varchar(100) DEFAULT NULL,
  `conexioninalambricaIpad` varchar(100) DEFAULT NULL,
  `audioIpad` varchar(100) DEFAULT NULL,
  `geolocalizacionIpad` varchar(100) DEFAULT NULL,
  `bateriaIpad` varchar(100) DEFAULT NULL,
  `sensoresIpad` varchar(100) DEFAULT NULL,
  `tuchIdIpad` varchar(50) DEFAULT NULL,
  `siriIpad` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `iphone`
--

CREATE TABLE `iphone` (
  `id` int(11) NOT NULL,
  `producttype` varchar(20) NOT NULL DEFAULT 'iphone',
  `img` varchar(200) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `screenSizeIphone` varchar(50) DEFAULT NULL,
  `resolutionIphone` varchar(100) DEFAULT NULL,
  `resistenciaIphone` varchar(255) DEFAULT NULL,
  `procesadorIphone` varchar(100) DEFAULT NULL,
  `camaraIphone` varchar(100) DEFAULT NULL,
  `faceidIphone` varchar(50) DEFAULT NULL,
  `memoryIphone` varchar(50) DEFAULT NULL,
  `geolocalizacion` varchar(100) DEFAULT NULL,
  `reproduccionIphone` text DEFAULT NULL,
  `sensoresIphone` text DEFAULT NULL,
  `grabacionIphone` text DEFAULT NULL,
  `siriIphone` varchar(100) DEFAULT NULL,
  `bateriaIphone` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mac`
--

CREATE TABLE `mac` (
  `id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color` varchar(50) NOT NULL,
  `dimensiones` varchar(100) NOT NULL,
  `screenSizeMac` varchar(50) DEFAULT NULL,
  `capacidadMac` varchar(50) DEFAULT NULL,
  `memoriaMac` varchar(50) DEFAULT NULL,
  `procesadorMac` varchar(100) DEFAULT NULL,
  `softwareMac` varchar(100) DEFAULT NULL,
  `conexionInalambricaMac` varchar(100) DEFAULT NULL,
  `audioMac` varchar(100) DEFAULT NULL,
  `tecladoMac` varchar(100) DEFAULT NULL,
  `camaraMac` varchar(100) DEFAULT NULL,
  `formatoMac` varchar(100) DEFAULT NULL,
  `bateriaMac` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `mac`
--

INSERT INTO `mac` (`id`, `img`, `productName`, `price`, `color`, `dimensiones`, `screenSizeMac`, `capacidadMac`, `memoriaMac`, `procesadorMac`, `softwareMac`, `conexionInalambricaMac`, `audioMac`, `tecladoMac`, `camaraMac`, `formatoMac`, `bateriaMac`) VALUES
(10, 'static/uploads/IPAD.jpg', 'sdfk', 678.00, 'ksdl', 'h', 'ljs', 'ljflslshfj', 'jh', 'kjh', 'kj', 'hjh', 'jh', 'jhhk', 'kjh', 'kjh', 'kj'),
(11, 'static/uploads/IPAD.jpg', 'sdfk', 678.00, 'ksdl', 'h', 'ljs', 'ljflslshfj', 'jh', 'kjh', 'kj', 'hjh', 'jh', 'jhhk', 'kjh', 'kjh', 'kj');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `nombre`, `email`, `direccion`, `telefono`, `password`, `is_admin`) VALUES
(1, 'jose', 'jose@msg.com', 'clasel12', '82793874', 'scrypt:32768:8:1$zPL3oVWYOv9aLAVV$a6bfecc0a7bdd66972dc1f7599353901820b5d25b62aff995d94029e346d536694089a642e51a97cb6524c9b17ae69b90643f91c661a03fbb40d6fd28bb98420', 1),
(2, 'manu', 'manu@gmail.com', 'calle 123', '32341223', 'scrypt:32768:8:1$dgBo2j1fTJIwp3BN$7c04381629fe1192136c9c0ce5b18c0361277a270daf4afdafda20f3d0828a2c83bd662eba0986ce8e29df66ab4378f5765b9b56a23157864bfa6d662414ab45', 0),
(3, 'm', 'm@a', 'calle', 'slfjlksf', 'scrypt:32768:8:1$TyMYQi8iJcPeBHbh$e4f87b400e676a3c7007bce10091784d580177c20ce81c64179042ead69823c5d8a519d2af5af5b9aff4eb4fdc42c477e3a596aeb05e375a3c9d6f21301b99e9', 0),
(4, '  ', 'a@a', ' ', ' ', 'scrypt:32768:8:1$JwRElsO6aRrEk7SO$502449a0b0ff9af8cf46dd023761362ffffcb9978e8e603e02c54a730888c9097b5f9dffc0514475ef2c6cc971d7157bcf1933ab31f53e9609960dfbf455ea86', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `airpods`
--
ALTER TABLE `airpods`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `applevisionpro`
--
ALTER TABLE `applevisionpro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `applewatch`
--
ALTER TABLE `applewatch`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ipad`
--
ALTER TABLE `ipad`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `iphone`
--
ALTER TABLE `iphone`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `mac`
--
ALTER TABLE `mac`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `airpods`
--
ALTER TABLE `airpods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `applevisionpro`
--
ALTER TABLE `applevisionpro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `applewatch`
--
ALTER TABLE `applewatch`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ipad`
--
ALTER TABLE `ipad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `iphone`
--
ALTER TABLE `iphone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT de la tabla `mac`
--
ALTER TABLE `mac`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
