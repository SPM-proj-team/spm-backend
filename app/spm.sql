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
    Description varchar(256),
    PRIMARY KEY (Job_ID)
);
-- population of data
INSERT INTO `Job_Role` (`Job_Role`, `Job_Title`, `Department`, `Description`) VALUES 
('CEO','The big boss','C-suite', 'lorem ipsum'),
('Operations manager','Manager', 'operations', 'lorem ipsum'),
('Operations Slave','Staff','HR', 'lorem ipsum');

-- INSERT INTO `Job_Role` (`Job_Role`, `Job_Title`, `Department`) VALUES  ('Outbound SDR', 'CEO', 'Sales'), ('Frontend Engineer', 'Manager', 'Technology'), ('CTO', 'Staff', 'Technology'), ('Co-Founder', 'CEO', 'HR'), ('Fraud Investigator', 'Manager', 'Operations'), ('Inbound BDR', 'Staff', 'Legal'), ('Database Manager', 'CEO', 'Sales'), ('Support Specialist', 'Manager', 'Technology'), ('Outbound BDR', 'Staff', 'Technology'), ('Outbound SDR', 'CEO', 'HR'), ('Database Manager', 'Manager', 'Operations'), ('Customer Support Team Lead', 'Staff', 'Legal'), ('Accountant', 'CEO', 'Sales'), ('IT Manager', 'Manager', 'Technology'), ('Product Marketing Specialist', 'Staff', 'Technology'), ('CEO', 'CEO', 'HR'), ('CFO', 'Manager', 'Operations'), ('Infrastructure Engineer', 'Staff', 'Legal'), ('COO', 'CEO', 'Sales'), ('Database Manager', 'Manager', 'Technology'), ('Inbound BDR', 'Staff', 'Technology'), ('Support Specialist', 'CEO', 'HR'), ('Outbound BDR', 'Manager', 'Operations'), ('Sales Engineer', 'Staff', 'Legal'), ('Product Manager', 'CEO', 'Sales'), ('Inbound BDR', 'Manager', 'Technology'), ('Solutions Architect', 'Staff', 'Technology'), ('Support Specialist', 'CEO', 'HR'), ('Accountant', 'Manager', 'Operations'), ('Outbound SDR', 'Staff', 'Legal'), ('Inbound BDR', 'CEO', 'Sales'), ('CMO', 'Manager', 'Technology'), ('Data Analyst', 'Staff', 'Technology'), ('Backend Engineer', 'CEO', 'HR'), ('Inbound SDR', 'Manager', 'Operations'), ('Co-Founder', 'Staff', 'Legal'), ('Database Manager', 'CEO', 'Sales'), ('Fraud Investigator', 'Manager', 'Technology'), ('Customer Engineer', 'Staff', 'Technology'), ('Support Specialist', 'CEO', 'HR'), ('Product Marketing Specialist', 'Manager', 'Operations'), ('Customer Engineer', 'Staff', 'Legal'), ('Internal Tools Lead', 'CEO', 'Sales'), ('Sales Team Lead', 'Manager', 'Technology'), ('Accountant', 'Staff', 'Technology'), ('Co-Founder', 'CEO', 'HR'), ('Database Manager', 'Manager', 'Operations'), ('Support Specialist', 'Staff', 'Legal'), ('Fraud Investigator', 'CEO', 'Sales'), ('Fullstack Engineer', 'Manager', 'Technology'), ('Customer Engineer', 'Staff', 'Technology'), ('CTO', 'CEO', 'HR'), ('Customer Support Team Lead', 'Manager', 'Operations'), ('Project Manager', 'Staff', 'Legal'), ('Outbound BDR', 'CEO', 'Sales'), ('Product Marketing Specialist', 'Manager', 'Technology'), ('IT Manager', 'Staff', 'Technology'), ('COO', 'CEO', 'HR'), ('Fullstack Engineer', 'Manager', 'Operations'), ('Customer Support Team Lead', 'Staff', 'Legal'), ('Inbound BDR', 'CEO', 'Sales'), ('CTO', 'Manager', 'Technology'), ('Sales Engineer', 'Staff', 'Technology'), ('Fraud Investigator', 'CEO', 'HR'), ('Database Manager', 'Manager', 'Operations'), ('Frontend Engineer', 'Staff', 'Legal'), ('Database Manager', 'CEO', 'Sales'), ('Account Executive', 'Manager', 'Technology'), ('Fraud Investigator', 'Staff', 'Technology'), ('Customer Engineer', 'CEO', 'HR'), ('Account Executive', 'Manager', 'Operations'), ('Product Manager', 'Staff', 'Legal'), ('CFO', 'CEO', 'Sales'), ('Internal Tools Lead', 'Manager', 'Technology'), ('Accountant', 'Staff', 'Technology'), ('Database Manager', 'CEO', 'HR'), ('Support Specialist', 'Manager', 'Operations'), ('Frontend Engineer', 'Staff', 'Legal'), ('Internal Tools Lead', 'CEO', 'Sales'), ('Customer Engineer', 'Manager', 'Technology'), ('Fullstack Engineer', 'Staff', 'Technology'), ('Frontend Engineer', 'CEO', 'HR'), ('CMO', 'Manager', 'Operations'), ('Outbound BDR', 'Staff', 'Legal'), ('DevOps Engineer', 'CEO', 'Sales'), ('Content Moderator', 'Manager', 'Technology'), ('Solutions Architect', 'Staff', 'Technology'), ('Customer Support Team Lead', 'CEO', 'HR'), ('Data Analyst', 'Manager', 'Operations'), ('Engineering Manager', 'Staff', 'Legal'), ('CEO', 'CEO', 'Sales'), ('CMO', 'Manager', 'Technology'), ('IT Manager', 'Staff', 'Technology'), ('Inbound BDR', 'CEO', 'HR'), ('CMO', 'Manager', 'Operations'), ('Project Manager', 'Staff', 'Legal'), ('Customer Support Team Lead', 'CEO', 'Sales'), ('Product Marketing Specialist', 'Manager', 'Technology'), ('Backend Engineer', 'Staff', 'Technology'), ('Solutions Architect', 'CEO', 'HR'), ('Accountant', 'Manager', 'Operations'), ('COO', 'Staff', 'Legal'), ('CMO', 'CEO', 'Sales'), ('Database Manager', 'Manager', 'Technology'), ('Database Manager', 'Staff', 'Technology'), ('Outbound BDR', 'CEO', 'HR'), ('COO', 'Manager', 'Operations'), ('Founder', 'Staff', 'Legal'), ('CTO', 'CEO', 'Sales'), ('Solutions Architect', 'Manager', 'Technology'), ('Engineering Manager', 'Staff', 'Technology'), ('Content Moderator', 'CEO', 'HR'), ('CEO', 'Manager', 'Operations'), ('CTO', 'Staff', 'Legal'), ('Content Moderator', 'CEO', 'Sales'), ('Accountant', 'Manager', 'Technology'), ('Account Executive', 'Staff', 'Technology'), ('Business Analyst', 'CEO', 'HR'), ('Solutions Architect', 'CEO', 'Operations'), ('Account Executive', 'Manager', 'Legal'), ('COO', 'Staff', 'Sales'), ('Project Manager', 'CEO', 'Technology'), ('Content Moderator', 'Manager', 'Technology'), ('CTO', 'Staff', 'HR'), ('Solutions Architect', 'CEO', 'Operations'), ('Co-Founder', 'Manager', 'Legal'), ('Customer Engineer', 'Staff', 'Sales'), ('CTO', 'CEO', 'Technology'), ('DevOps Engineer', 'Manager', 'Technology'), ('Customer Support Team Lead', 'Staff', 'HR'), ('Database Manager', 'CEO', 'Operations'), ('Inbound BDR', 'Manager', 'Legal'), ('Fullstack Engineer', 'Staff', 'Sales'), ('CFO', 'CEO', 'Technology'), ('Data Analyst', 'Manager', 'Technology'), ('Account Executive', 'Staff', 'HR'), ('Project Manager', 'CEO', 'Operations'), ('Accountant', 'Manager', 'Legal'), ('Database Manager', 'Staff', 'Sales'), ('Account Executive', 'CEO', 'Technology'), ('Account Executive', 'Manager', 'Technology'), ('Software Engineer', 'Staff', 'HR'), ('Outbound SDR', 'CEO', 'Operations'), ('Product Marketing Specialist', 'Manager', 'Legal'), ('Infrastructure Engineer', 'Staff', 'Sales'), ('Engineering Manager', 'CEO', 'Technology'), ('Product Marketing Specialist', 'Manager', 'Technology'), ('Fullstack Engineer', 'Staff', 'HR'), ('IT Manager', 'CEO', 'Operations'), ('Inbound BDR', 'Manager', 'Legal'), ('Outbound BDR', 'Staff', 'Sales'), ('Internal Tools Lead', 'CEO', 'Technology'), ('Engineering Manager', 'Manager', 'Technology'), ('Engineering Manager', 'Staff', 'HR'), ('Backend Engineer', 'CEO', 'Operations'), ('Product Marketing Specialist', 'Manager', 'Legal'), ('Fraud Investigator', 'Staff', 'Sales'), ('Customer Support Team Lead', 'CEO', 'Technology'), ('Backend Engineer', 'Manager', 'Technology'), ('DevOps Engineer', 'Staff', 'HR'), ('Fraud Investigator', 'CEO', 'Operations'), ('Data Analyst', 'Manager', 'Legal'), ('DevOps Engineer', 'Staff', 'Sales'), ('Frontend Engineer', 'CEO', 'Technology'), ('DevOps Engineer', 'Manager', 'Technology'), ('Co-Founder', 'Staff', 'HR'), ('Sales Engineer', 'CEO', 'Operations'), ('Outbound BDR', 'Manager', 'Legal'), ('Accountant', 'Staff', 'Sales'), ('Sales Team Lead', 'CEO', 'Technology'), ('CTO', 'Manager', 'Technology'), ('Customer Engineer', 'Staff', 'HR'), ('CTO', 'CEO', 'Operations'), ('Customer Success Team Lead', 'Manager', 'Legal'), ('Fraud Investigator', 'Staff', 'Sales'), ('Project Manager', 'CEO', 'Technology'), ('Inbound SDR', 'Manager', 'Technology'), ('Support Specialist', 'Staff', 'HR'), ('Account Executive', 'CEO', 'Operations'), ('Inbound SDR', 'Manager', 'Legal'), ('Database Manager', 'Staff', 'Sales'), ('Database Manager', 'CEO', 'Technology'), ('IT Manager', 'Manager', 'Technology'), ('Customer Success Team Lead', 'Staff', 'HR'), ('Solutions Architect', 'CEO', 'Operations'), ('CFO', 'Manager', 'Legal'), ('Business Analyst', 'Staff', 'Sales'), ('CFO', 'CEO', 'Technology'), ('Outbound SDR', 'Manager', 'Technology'), ('Solutions Architect', 'Staff', 'HR'), ('DevOps Engineer', 'CEO', 'Operations'), ('Content Moderator', 'Manager', 'Legal'), ('Database Manager', 'Staff', 'Sales'), ('Frontend Engineer', 'CEO', 'Technology'), ('Product Manager', 'Manager', 'Technology'), ('Solutions Architect', 'Staff', 'HR'), ('Account Executive', 'CEO', 'Operations'), ('Internal Tools Lead', 'Manager', 'Legal'), ('Inbound SDR', 'Staff', 'Sales'), ('CMO', 'Staff', 'Technology');

--
-- Table structure for table `Learning_Journey`
--

DROP TABLE IF EXISTS `Learning_Journey`;
CREATE TABLE IF NOT EXISTS `Learning_Journey` (
  `Learning_Journey_ID` int NOT NULL AUTO_INCREMENT,
  `Learning_Journey_Name` varchar(45) NOT NULL,
  `Staff_ID` int NOT NULL,
  `Description` varchar(256),
  `Job_Role_ID` int NOT NULL,
  PRIMARY KEY (`Learning_Journey_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `Learning_Journey` (`Learning_Journey_Name`, `Staff_ID`, `Description`, `Job_Role_ID`) VALUES
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
