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

DROP SCHEMA IF EXISTS `spm_db`;
CREATE SCHEMA IF NOT EXISTS `spm_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_db`;

-- Course Table 
DROP TABLE IF EXISTS `Course`;
CREATE TABLE Course (
    Course_ID varchar(20) NOT NULL,
    Course_Name varchar(45) NOT NULL,
    Course_Desc varchar(255) NOT NULL,
    Course_Type varchar(10) NOT NUll,
    Course_Status varchar(15) NOT NUll,
    Course_Category varchar(50) NOT NUll,
    PRIMARY KEY (Course_ID)
);
-- population of data
INSERT INTO Course (`Course_ID`, `Course_Name`, `Course_Desc`, `Course_Type`, `Course_Status`, `Course_Category`) VALUES 
('IS212',
'Software Project Management',
'Equip student with knowledge about agile approach regarding software project development ',
'Type_1',
'Open',
'Course_Category_1'),
('BAP101',
'Enterprise Business System',
'Enterprise Business System Description',
'Type_1',
'Open',
'Course_Category_1'),
('BAP102',
'Sales Management System',
'Sales Management System Description',
'Type_1',
'Open',
'Course_Category_1'),
('BAP103',
'Busioness Process and Modeling',
'Busioness Process and Modeling Description',
'Type_1',
'Open',
'Course_Category_1');

-- --------------------------------------------------------
--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `Skill`;
CREATE TABLE IF NOT EXISTS `Skill` (
  `Skill_ID` char(13) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Skill` (`Skill_ID`, `name`) VALUES
('S001', 'Critical Thinking'),
('S002', 'People Management'),
('S003', 'Business Applications');
COMMIT;
-- --------------------------------------------------------
--
-- Table structure for table `Job_Role`
--
DROP TABLE IF EXISTS `Job_Role`;
CREATE TABLE Job_Role (
    Job_ID int NOT NULL auto_increment,
    Job_Role varchar(20) NOT NULL,
    Job_Title varchar(20) NOT NULL,
    Department varchar(20) NOT NUll,
    PRIMARY KEY (Job_ID)
);
-- population of data
INSERT INTO `Job_Role` (`Job_Role`, `Job_Title`, `Department`) VALUES 
('CEO','The big boss','C-suite'),
('Operations manager','Manager', 'operations'),
('Operations Slave','Staff','HR');

--
-- Table structure for table `Learning_Journey`
--

DROP TABLE IF EXISTS `Learning_Journey`;
CREATE TABLE IF NOT EXISTS `Learning_Journey` (
  `Learning_Journey_ID` int NOT NULL AUTO_INCREMENT,
  `Learning_Journey_Name` varchar(45) NOT NULL,
  `Staff_ID` int NOT NULL,
  `Description` varchar(256),
  `Role_Job_ID` int NOT NULL,
  PRIMARY KEY (`Learning_Journey_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Learning_Journey` (`Learning_Journey_Name`, `Staff_ID`, `Description`, `Role_Job_ID`) VALUES
('Learning Journey for Full Stack Developer Role', 1, 'lorem ipsum', 1),
('Learning Journey for Dummies', 1, 'lorem ipsum for dummies', 2),
('Advanced Learning Journey', 2, 'lorem ipsum for dummies', 3);
COMMIT;

--
-- Table structure for table `Registration`
--

DROP TABLE IF EXISTS `Registration`;
CREATE TABLE IF NOT EXISTS `Registration` (
  `Reg_ID` int NOT NULL,
  `Course_ID` varchar(20) NOT NULL,
  `Staff_ID` int NOT NULL,
  `Reg_Status` varchar(20) NOT NULL,
  `Completion_Status` varchar(20),
  PRIMARY KEY (`Reg_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Registration` (`Reg_ID`, `Course_ID`, `Staff_ID`, `Reg_Status`, `Completion_Status`) VALUES
(1, 1, 1, 'Registered',  'Completed'),
(2, 1, 2, 'Registered',  'OnGoing'),
(3, 2, 1, 'Waitlist',  ''),
(4, 2, 2, 'Rejected',  '');
COMMIT;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
CREATE TABLE IF NOT EXISTS `Staff` (
  `Staff_ID` int NOT NULL AUTO_INCREMENT,
  `Staff_FName` varchar(50) NOT NULL,
  `Staff_LName` varchar(50) NOT NULL,
  `Dept` varchar(50) NOT NULL,
  `Email` varchar(50),
  `Role_ID` int NOT NULL,
  PRIMARY KEY (`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Staff` (`Staff_FName`, `Staff_LName`, `Dept`, `Email`, `Role_ID`) VALUES
('John', 'Sim', 'Chairman',  'jack.sim@allinone.com.sg', 1),
('Jack', 'Sim', 'CEO',  'jack.sim@allinone.com.sg', 1),
('Derek', 'Tan', 'Sales',  'Derek.Tan@allinone.com.sg', 3),
('Susan', 'Goh', 'Sales',  'Susan.Goh@allinone.com.sg', 2),
('Noah', 'Goh', 'Ops',  'Noah.Goh@allinone.com.sg', 4);
COMMIT;

--
-- Table structure for table `Access_Role`
--

DROP TABLE IF EXISTS `Access_Role`;
CREATE TABLE IF NOT EXISTS `Access_Role` (
  `Role_ID` int NOT NULL AUTO_INCREMENT,
  `Role_Name` varchar(20) NOT NULL,
  PRIMARY KEY (`Role_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Access_Role` (`Role_Name`) VALUES
('Admin'),
('User'),
('Manager'),
('Trainer');
COMMIT;

--
-- Table structure for table `Learning_Journey_has_Course`
--

DROP TABLE IF EXISTS `Learning_Journey_has_Course`;
CREATE TABLE IF NOT EXISTS `Learning_Journey_has_Course` (
  `Course_ID` varchar(20) NOT NULL,
  `Learning_Journey_ID` int NOT NULL,
  PRIMARY KEY (`Course_ID`, `Learning_Journey_ID`),
  FOREIGN KEY (`Course_ID`) REFERENCES Course (`Course_ID`),
  FOREIGN KEY (`Learning_Journey_ID`) REFERENCES Learning_Journey (`Learning_Journey_ID`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Learning_Journey_has_Course` (`Course_ID`, `Learning_Journey_ID`) VALUES
('BAP101', 1),
('IS212', 1),
('BAP101', 2),
('BAP102', 2),
('BAP103', 2),
('IS212', 3),
('BAP101', 3),
('BAP102', 3);

COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

--
-- Table structure for association table `Role_has_Skill`
--
DROP TABLE IF EXISTS `Role_has_Skill`;
CREATE TABLE IF NOT EXISTS `Role_has_Skill` (
    `Job_ID` int NOT NULL,
    `Skill_ID` char(13) NOT NULL,
    FOREIGN KEY (`Job_ID`) REFERENCES Job_Role(`Job_ID`),
    FOREIGN KEY (`Skill_ID`) REFERENCES Skill(`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Role_has_Skill` (`Job_ID`, `Skill_ID`) VALUES
(1,'S001'),
(1,'S002'),
(2,'S002'),
(2,'S001');

--
-- Table structure for association table `Course_has_Skill`
--
DROP TABLE IF EXISTS `Course_has_Skill`;
CREATE TABLE IF NOT EXISTS `Course_has_Skill` (
    `Skill_ID` VARCHAR(13) NOT NULL,
    `Course_ID` varchar(20) NOT NULL,
    FOREIGN KEY (`Course_ID`) REFERENCES Course(`Course_ID`),
    FOREIGN KEY (`Skill_ID`) REFERENCES Skill(`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Course_has_Skill` (`Skill_ID`, `Course_ID`) VALUES
('S001', 'IS212'),
('S002', 'IS212'),
('S001','BAP101'),
('S002','BAP101'),
('S003','BAP101'),
('S003','BAP102'),
('S003','BAP103');

--
-- Table structure for association table `User_has_Skill`
--
DROP TABLE IF EXISTS `User_has_Skill`;
CREATE TABLE IF NOT EXISTS `User_has_Skill` (
    `Skill_ID` char(13) NOT NULL,
    `Staff_ID` int NOT NULL,
    `Date_Acquired` DATE NOT NULL,
    FOREIGN KEY (`Skill_ID`) REFERENCES Skill(`Skill_ID`),
    FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `User_has_Skill` (`Skill_ID`, `Staff_ID`, `Date_Acquired`) VALUES
('S001', 1, '2021-12-31'),
('S002', 1, '2022-03-03'),
('S001', 2, '2021-01-01'),
('S003', 3, '2022-01-01');

COMMIT;
