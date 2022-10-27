-- Below is CLI command to import sql data into local MySQL db (TO-RUN from /spm-backend dir):
-- mysql -uroot < tests/sql/test_spm.sql

-- MySQL dump 10.13  Distrib 8.0.28, for macos12.0 (arm64)
--
-- Host: spm-db.c300l1maonyq.ap-southeast-1.rds.amazonaws.com    Database: test_spm_db
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Current Database: `test_spm_db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `test_spm_db` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `test_spm_db`;


--
-- Table structure for table `Course`
--

DROP TABLE IF EXISTS `Course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Course` (
  `Course_ID` varchar(20) NOT NULL,
  `Course_Name` varchar(45) NOT NULL,
  `Course_Desc` varchar(255) NOT NULL,
  `Course_Type` varchar(10) NOT NULL,
  `Course_Status` varchar(15) NOT NULL,
  `Course_Category` varchar(50) NOT NULL,
  PRIMARY KEY (`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course`
--

LOCK TABLES `Course` WRITE;
/*!40000 ALTER TABLE `Course` DISABLE KEYS */;
INSERT INTO `Course` VALUES 
('COR001','testCourse1','Description for testCourse1','Internal','Active','Core'),
('COR002','testCourse2','Description for testCourse2','Internal','Active','Core'),
('COR003','testCourse3','Description for testCourse3','Internal','Active','Core');

/*!40000 ALTER TABLE `Course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Job_Role`
--

DROP TABLE IF EXISTS `Job_Role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Job_Role` (
  `Job_ID` int NOT NULL AUTO_INCREMENT,
  `Job_Role` varchar(20) NOT NULL,
  `Job_Title` varchar(20) NOT NULL,
  `Department` varchar(20) NOT NULL,
  `Description` TEXT NOT NULL,
  PRIMARY KEY (`Job_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=220 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Job_Role`
--

LOCK TABLES `Job_Role` WRITE;
/*!40000 ALTER TABLE `Job_Role` DISABLE KEYS */;
INSERT INTO `Job_Role` VALUES 
(1,'testRole1','Staff','Operations','testRole1 Description');
/*!40000 ALTER TABLE `Job_Role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Learning_Journey`
--

DROP TABLE IF EXISTS `Learning_Journey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Learning_Journey` (
  `Learning_Journey_ID` int NOT NULL AUTO_INCREMENT,
  `Learning_Journey_Name` varchar(45) NOT NULL,
  `Staff_ID` int NOT NULL,
  `Description` TEXT DEFAULT NULL,
  `Job_Role_ID` int NOT NULL,
  PRIMARY KEY (`Learning_Journey_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Learning_Journey`
--

LOCK TABLES `Learning_Journey` WRITE;
/*!40000 ALTER TABLE `Learning_Journey` DISABLE KEYS */;
INSERT INTO `Learning_Journey` VALUES 
(1,'testLearningJourney1',1,'testLearningJourney1 Description',1);
/*!40000 ALTER TABLE `Learning_Journey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Skill`
--

DROP TABLE IF EXISTS `Skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Skill` (
  `Skill_ID` char(13) NOT NULL,
  `name` varchar(64) NOT NULL,
  PRIMARY KEY (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Skill`
--

LOCK TABLES `Skill` WRITE;
/*!40000 ALTER TABLE `Skill` DISABLE KEYS */;
INSERT INTO `Skill` VALUES 
('S001','testSkill1'),
('S002','testSkill2'),
('S003','testSkill3');
/*!40000 ALTER TABLE `Skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Learning_Journey_has_Course`
--

DROP TABLE IF EXISTS `Learning_Journey_has_Course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Learning_Journey_has_Course` (
  `Course_ID` varchar(20) NOT NULL,
  `Learning_Journey_ID` int NOT NULL,
  PRIMARY KEY (`Course_ID`,`Learning_Journey_ID`),
  KEY `Learning_Journey_ID` (`Learning_Journey_ID`),
  CONSTRAINT `Learning_Journey_has_Course_ibfk_1` FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`),
  CONSTRAINT `Learning_Journey_has_Course_ibfk_2` FOREIGN KEY (`Learning_Journey_ID`) REFERENCES `Learning_Journey` (`Learning_Journey_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Learning_Journey_has_Course`
--

LOCK TABLES `Learning_Journey_has_Course` WRITE;
/*!40000 ALTER TABLE `Learning_Journey_has_Course` DISABLE KEYS */;
INSERT INTO `Learning_Journey_has_Course` VALUES 
('COR001',1);
/*!40000 ALTER TABLE `Learning_Journey_has_Course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Course_has_Skill`
--

DROP TABLE IF EXISTS `Course_has_Skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Course_has_Skill` (
  `Skill_ID` varchar(13) NOT NULL,
  `Course_ID` varchar(20) NOT NULL,
  KEY `Course_ID` (`Course_ID`),
  KEY `Skill_ID` (`Skill_ID`),
  CONSTRAINT `Course_has_Skill_ibfk_1` FOREIGN KEY (`Course_ID`) REFERENCES `Course` (`Course_ID`),
  CONSTRAINT `Course_has_Skill_ibfk_2` FOREIGN KEY (`Skill_ID`) REFERENCES `Skill` (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Course_has_Skill`
--

LOCK TABLES `Course_has_Skill` WRITE;
/*!40000 ALTER TABLE `Course_has_Skill` DISABLE KEYS */;
INSERT INTO `Course_has_Skill` VALUES 
('S001','COR001'),
('S001','COR002'),
('S002','COR002')
('S002','COR003')
('S003','COR001')
('S003','COR003');
/*!40000 ALTER TABLE `Course_has_Skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Role_has_Skill`
--

DROP TABLE IF EXISTS `Role_has_Skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Role_has_Skill` (
  `Job_ID` int NOT NULL,
  `Skill_ID` char(13) NOT NULL,
  KEY `Job_ID` (`Job_ID`),
  KEY `Skill_ID` (`Skill_ID`),
  CONSTRAINT `Role_has_Skill_ibfk_1` FOREIGN KEY (`Job_ID`) REFERENCES `Job_Role` (`Job_ID`),
  CONSTRAINT `Role_has_Skill_ibfk_2` FOREIGN KEY (`Skill_ID`) REFERENCES `Skill` (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `Role_has_Skill` WRITE;
/*!40000 ALTER TABLE `Role_has_Skill` DISABLE KEYS */;
INSERT INTO `Role_has_Skill` VALUES 
(1,'S001'),
(1,'S002'),
(1,'S003');
/*!40000 ALTER TABLE `Role_has_Skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'test_spm_db'
--
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-18  9:34:37
