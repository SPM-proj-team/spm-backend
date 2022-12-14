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
(1,'testRole1','Staff','Operations','testRole1 Description'),
(2,'testRole2','Manager','Sales','testRole2 Description');
/*!40000 ALTER TABLE `Job_Role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Role_has_Skill`
--

DROP TABLE IF EXISTS `Role_has_Skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Role_has_Skill` (
  `Job_ID` int NOT NULL,
  `Skill_ID` int NOT NULL,
  KEY `Job_ID` (`Job_ID`),
  KEY `Skill_ID` (`Skill_ID`),
  CONSTRAINT `Role_has_Skill_ibfk_1` FOREIGN KEY (`Job_ID`) REFERENCES `Job_Role` (`Job_ID`),
  CONSTRAINT `Role_has_Skill_ibfk_2` FOREIGN KEY (`Skill_ID`) REFERENCES `Skill` (`Skill_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

LOCK TABLES `Role_has_Skill` WRITE;
/*!40000 ALTER TABLE `Role_has_Skill` DISABLE KEYS */;
INSERT INTO `Role_has_Skill` VALUES 
(1,1),
(1,2),
(2,3),
(2,4);
/*!40000 ALTER TABLE `Role_has_Skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Skill`
--

DROP TABLE IF EXISTS `Skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Skill` (
  `Skill_ID` int NOT NULL AUTO_INCREMENT,
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
(1,'testSkill1'),
(2,'testSkill2'),
(3,'testSkill3'),
(4,'testSkill4');
/*!40000 ALTER TABLE `Skill` ENABLE KEYS */;
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
