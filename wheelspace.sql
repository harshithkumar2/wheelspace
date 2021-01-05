-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 05, 2021 at 03:23 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wheelspace`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `email`, `name`, `password`) VALUES
(1, 'har@g.cm', 'ha', '$5$rounds=535000$KrbzRt9jVPenA9Z.$d6ThL3g4Y2NT3SXRjZVDvdEei6GjkaFonidr1KfEmtC'),
(2, 'harsh@g.com', 'harshith', '$5$rounds=535000$U7ulvU2SlCym6r9l$/YDzN9wGa0wFtqJqVyNzqeGFY/pqw8vLVaoCxrjKPkC'),
(3, 'aa@g.com', 'ha', '$5$rounds=535000$JTSV7rf5ZlNcbmZt$17R/sxtSt0uyqhJvyQqq5w7gkQ9DriR2elLK64jRrC0');

-- --------------------------------------------------------

--
-- Table structure for table `offline_extended`
--

CREATE TABLE `offline_extended` (
  `id` int(11) NOT NULL,
  `license_no` varchar(100) DEFAULT NULL,
  `dates` date DEFAULT NULL,
  `duration` float(4,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `offline_extended`
--

INSERT INTO `offline_extended` (`id`, `license_no`, `dates`, `duration`) VALUES
(1, 'ka12mnvudfdf2', '2021-01-06', 1.50),
(10, 'ka12mnvudfdf2', '2021-01-08', 2.50),
(11, 'ka12mnvudfdf2', '2021-01-15', 4.00),
(12, 'ka12mnvudfdf2', '2021-01-15', 4.00),
(13, 'ka12mnvudfdf2', '2021-01-21', 1.20),
(14, 'ka12mnvudfdf2', '2021-01-03', 2.00),
(15, 'ka12mnvudfdf2', '2021-01-13', 3.00),
(16, 'ka12mnvudfdf2', '2021-01-13', 3.00),
(17, 'ka12mnvudfdf2', '2021-01-05', 12.00),
(18, 'ka12mnvudfdf2', '2021-01-15', 1.00),
(19, 'ka12mnvudfdf2', '2021-01-07', 3.00),
(20, 'ka12mnvudfdf2', '2021-01-15', 1.00);

-- --------------------------------------------------------

--
-- Table structure for table `offline_user`
--

CREATE TABLE `offline_user` (
  `license_no` varchar(50) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `vech_no` varchar(20) DEFAULT NULL,
  `vech_type` varchar(20) DEFAULT NULL,
  `duration` float(4,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `offline_user`
--

INSERT INTO `offline_user` (`license_no`, `name`, `email`, `phone`, `vech_no`, `vech_type`, `duration`) VALUES
('ka12mnvudfdf2', 'harshith', 'harsh@g.com', '1234', 'KA18MN2343', '4 wheeler', 1.40);

-- --------------------------------------------------------

--
-- Table structure for table `online_booking`
--

CREATE TABLE `online_booking` (
  `id` int(11) NOT NULL,
  `license_no` varchar(100) DEFAULT NULL,
  `vech_no` varchar(50) DEFAULT NULL,
  `vech_type` varchar(50) DEFAULT NULL,
  `duration` float(4,2) DEFAULT NULL,
  `dates` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `online_booking`
--

INSERT INTO `online_booking` (`id`, `license_no`, `vech_no`, `vech_type`, `duration`, `dates`) VALUES
(2, 'ka19mncbv', 'ka19mc3344', '4 wheeler', 2.00, '2021-01-03'),
(3, 'ka19mncbv', 'test', '2 wheeler', 4.00, '2021-01-04'),
(4, 'ka17mnqwe', 'ka13wer', '4 wheeler', 3.00, '2021-01-07'),
(5, 'ka19mncbv', 'ka12s', '4 wheeler', 2.00, '2021-01-05');

-- --------------------------------------------------------

--
-- Table structure for table `online_user`
--

CREATE TABLE `online_user` (
  `license_no` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `online_user`
--

INSERT INTO `online_user` (`license_no`, `name`, `email`, `phone`, `password`) VALUES
('ka17mnqwe', 'adithya', 'ad@g.com', '123455', '$5$rounds=535000$cyCuBMn.0vvJUsVS$5jJseLOTWGxZm3XGBObCCINRnDxHbOWLdjS9zPxYDR6'),
('ka19mncbv', 'harshith', 'harsh@g.com', '1234567890', '$5$rounds=535000$vOY/GBmIJftf.Tjl$2r1UkUaGNLK3VYlSXtymYjCj1qWMK813ZzHqciR2hz3');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `name`, `email`, `phone`, `password`) VALUES
(1, 'harshithk', 'harsh@g.com', '123', '$5$rounds=535000$T5U6.V4slVfZd1Nb$ccbvNeXgWvgd8cQywF5AMg7TVPM3Vsbqb35MuFqJ6m/'),
(2, 'staffs', 'st@g.comm', '123', '$5$rounds=535000$XZzO8QPRKCGBXtu1$jcrEA2sw98E5ZyMGCkH4TWoW4XQqkSXhjLMicWZ8kt1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `offline_extended`
--
ALTER TABLE `offline_extended`
  ADD PRIMARY KEY (`id`),
  ADD KEY `license_no` (`license_no`);

--
-- Indexes for table `offline_user`
--
ALTER TABLE `offline_user`
  ADD PRIMARY KEY (`license_no`);

--
-- Indexes for table `online_booking`
--
ALTER TABLE `online_booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `license_no` (`license_no`);

--
-- Indexes for table `online_user`
--
ALTER TABLE `online_user`
  ADD PRIMARY KEY (`license_no`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `offline_extended`
--
ALTER TABLE `offline_extended`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `online_booking`
--
ALTER TABLE `online_booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `offline_extended`
--
ALTER TABLE `offline_extended`
  ADD CONSTRAINT `offline_extended_ibfk_1` FOREIGN KEY (`license_no`) REFERENCES `offline_user` (`license_no`) ON DELETE CASCADE;

--
-- Constraints for table `online_booking`
--
ALTER TABLE `online_booking`
  ADD CONSTRAINT `online_booking_ibfk_1` FOREIGN KEY (`license_no`) REFERENCES `online_user` (`license_no`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
