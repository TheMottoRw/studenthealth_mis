-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: shealthmis
-- ------------------------------------------------------
-- Server version	8.0.20-0ubuntu0.20.04.1

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

--
-- Table structure for table `administrators`
--

DROP TABLE IF EXISTS `administrators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrators` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(70) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `consultation`
--

DROP TABLE IF EXISTS `consultation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consultation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `student` int DEFAULT NULL,
  `height` varchar(15) DEFAULT NULL,
  `weight` varchar(15) DEFAULT NULL,
  `symptoms` text,
  `medications` varchar(255) DEFAULT NULL,
  `medication_qty` varchar(255) DEFAULT NULL,
  `conditions` varchar(300) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `student` (`student`),
  CONSTRAINT `consultation_ibfk_1` FOREIGN KEY (`student`) REFERENCES `students` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medication_given`
--

DROP TABLE IF EXISTS `medication_given`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medication_given` (
  `id` int NOT NULL AUTO_INCREMENT,
  `consultation_id` int DEFAULT NULL,
  `medication` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `nurse` int DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `medication` (`medication`),
  KEY `consultation_id` (`consultation_id`),
  KEY `nurse` (`nurse`),
  CONSTRAINT `medication_given_ibfk_1` FOREIGN KEY (`medication`) REFERENCES `medications` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `medication_given_ibfk_2` FOREIGN KEY (`consultation_id`) REFERENCES `consultation` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `medication_given_ibfk_3` FOREIGN KEY (`nurse`) REFERENCES `nurses` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medication_history`
--

DROP TABLE IF EXISTS `medication_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medication_history` (
  `id` int NOT NULL AUTO_INCREMENT,
  `medication_id` int DEFAULT NULL,
  `current_qty` varchar(30) DEFAULT NULL,
  `added_quantity` varchar(30) DEFAULT NULL,
  `total_qty` varchar(30) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `batch_no` varchar(15) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `medication_id` (`medication_id`),
  CONSTRAINT `medication_history_ibfk_1` FOREIGN KEY (`medication_id`) REFERENCES `medications` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `medications`
--

DROP TABLE IF EXISTS `medications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `available_stock` varchar(30) DEFAULT NULL,
  `unit` varchar(30) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nurses`
--

DROP TABLE IF EXISTS `nurses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nurses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(70) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(60) DEFAULT NULL,
  `delete_status` varchar(5) DEFAULT 'No',
  `delete_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `names` varchar(70) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `regno` varchar(10) NOT NULL,
  `has_insurance` varchar(10) DEFAULT NULL,
  `insurance_type` varchar(50) DEFAULT NULL,
  `insurance_number` varchar(30) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-13 11:40:29
