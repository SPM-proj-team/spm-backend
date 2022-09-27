-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 14, 2019 at 06:42 AM
-- Server version: 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `availability`
--
DROP SCHEMA IF EXISTS `spm_db`;
CREATE SCHEMA IF NOT EXISTS `spm_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_db`;

-- --------------------------------------------------------
--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
CREATE TABLE IF NOT EXISTS `skill` (
  `Skill_ID` char(13) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `skill` (`Skill_ID`, `name`) VALUES
('S001', 'Critical Thinking'),
('S002', 'People Management');
COMMIT;

--
-- Table structure for table `Learning_Journey`
--

DROP TABLE IF EXISTS `Learning_Journey`;
CREATE TABLE IF NOT EXISTS `Learning_Journey` (
  `Learning_Journey_ID` int NOT NULL AUTO_INCREMENT,
  `Learning_Journey_Name` varchar(45) NOT NULL,
  `Staff_ID` int NOT NULL,
  `Description` varchar(256),
  PRIMARY KEY (`Learning_Journey_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Learning_Journey` (`Learning_Journey_Name`, `Staff_ID`, `Description`) VALUES
('Learning Journey for Full Stack Developer Role', 1, 'lorem ipsum'),
('Learning Journey for Dummies', 1, 'lorem ipsum for dummies');
COMMIT;

--
-- Table structure for table `Courses`
--

DROP TABLE IF EXISTS `Courses`;
CREATE TABLE IF NOT EXISTS `Courses` (
  `Course_ID` varchar(20) NOT NULL,
  `Course_Name` varchar(45) NOT NULL,
  `Course_Desc` varchar(255) NOT NULL,
  `Course_Status` varchar(15) NOT NULL,
  `Course_Type` varchar(10) NOT NULL,
  `Course_Category` varchar(50) NOT NULL,
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Courses` (
  `Course_ID`, 
  `Course_Name`, 
  `Course_Desc`, 
  `Course_Status`, 
  `Course_Type`, 
  `Course_Category`
  ) VALUES
('IS212', 'Software Project Management', 'For students to learn Agile philosophies', 'Active', 'Internal', 'IT'),
('COR3301', 'Ethics', 'For learners to gain morality', 'Active', 'External', 'Core'),
('MGMT001', 'Management for Dummies', 'For stupid people to learn basic management', 'Active', 'Internal', 'Management'),
('PHY001', 'Organisational Behavior', 'For managers to learn how to manage employees', 'Active', 'External', 'Management'),
('COR1305', 'Spreadsheet Modelling', 'To learn Excel and skills like VLookup', 'Active', 'Internal', 'IT'),
('IS412', 'Enterprise Business Solutions', 'To learn SAP products and develop real world solutions', 'Active', 'Internal', 'IT'),
('IS211', 'Interactive Design Prototyping', 'To learn basic UI/UX skills and make wireframes', 'Active', 'Internal', 'IT');
COMMIT;

--
-- Table structure for table `Learning_Journey_has_Course`
--

DROP TABLE IF EXISTS `Learning_Journey_has_Course`;
CREATE TABLE IF NOT EXISTS `Learning_Journey_has_Course` (
  `Course_ID` varchar(20) NOT NULL,
  `Learning_Journey_ID` int NOT NULL,
  PRIMARY KEY (`Course_ID`, `Learning_Journey_ID`),
  FOREIGN KEY (`Course_ID`) REFERENCES Courses (`Course_ID`),
  FOREIGN KEY (`Learning_Journey_ID`) REFERENCES Learning_Journey (`Learning_Journey_ID`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Learning_Journey_has_Course` (`Course_ID`, `Learning_Journey_ID`) VALUES
('IS412', 1),
('IS212', 1),
('IS211', 1),
('MGMT001', 2),
('COR1305', 2);
COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
