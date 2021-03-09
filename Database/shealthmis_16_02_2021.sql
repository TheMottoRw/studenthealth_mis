-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: shealthmis
-- ------------------------------------------------------
-- Server version	5.7.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrators` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `names` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `password` varchar(70) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrators`
--

LOCK TABLES `administrators` WRITE;
/*!40000 ALTER TABLE `administrators` DISABLE KEYS */;
INSERT INTO `administrators` VALUES (1,'Kabatesi Benitha','0784360416','MTIzNDU=','2020-04-28 16:11:51');
/*!40000 ALTER TABLE `administrators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consultation`
--

DROP TABLE IF EXISTS `consultation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consultation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student` int(11) DEFAULT NULL,
  `height` varchar(15) DEFAULT NULL,
  `weight` varchar(15) DEFAULT NULL,
  `symptoms` text,
  `medications` varchar(255) DEFAULT NULL,
  `medication_qty` varchar(255) DEFAULT NULL,
  `conditions` varchar(300) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `student` (`student`),
  CONSTRAINT `consultation_ibfk_1` FOREIGN KEY (`student`) REFERENCES `students` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consultation`
--

LOCK TABLES `consultation` WRITE;
/*!40000 ALTER TABLE `consultation` DISABLE KEYS */;
INSERT INTO `consultation` VALUES (1,1,'192','109','Umuriro,kubabara igifu igihe ariye ibintu bikomeye','','','3 per day','2020-04-28 17:39:20'),(2,2,'1.76','46','Kubabara mu gifu,umuriro ukabije','','','Kimwe mu gitondo ikindi saa sita ikindi nimugoroba','2020-06-11 00:29:23');
/*!40000 ALTER TABLE `consultation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `failed_jobs`
--

DROP TABLE IF EXISTS `failed_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `failed_jobs` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `failed_jobs`
--

LOCK TABLES `failed_jobs` WRITE;
/*!40000 ALTER TABLE `failed_jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `failed_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medication_given`
--

DROP TABLE IF EXISTS `medication_given`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medication_given` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `consultation_id` int(11) DEFAULT NULL,
  `medication` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `nurse` int(11) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `medication` (`medication`),
  KEY `consultation_id` (`consultation_id`),
  KEY `nurse` (`nurse`),
  CONSTRAINT `medication_given_ibfk_1` FOREIGN KEY (`medication`) REFERENCES `medications` (`id`),
  CONSTRAINT `medication_given_ibfk_2` FOREIGN KEY (`consultation_id`) REFERENCES `consultation` (`id`),
  CONSTRAINT `medication_given_ibfk_3` FOREIGN KEY (`nurse`) REFERENCES `nurses` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medication_given`
--

LOCK TABLES `medication_given` WRITE;
/*!40000 ALTER TABLE `medication_given` DISABLE KEYS */;
INSERT INTO `medication_given` VALUES (1,2,1,3,1,'2020-06-11 22:43:21'),(2,2,1,3,1,'2020-06-11 22:44:38'),(3,2,4,21,1,'2020-06-11 22:56:04'),(4,1,1,3,1,'2020-06-11 23:21:15');
/*!40000 ALTER TABLE `medication_given` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medication_history`
--

DROP TABLE IF EXISTS `medication_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medication_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medication_id` int(11) DEFAULT NULL,
  `current_qty` varchar(30) DEFAULT NULL,
  `added_quantity` varchar(30) DEFAULT NULL,
  `total_qty` varchar(30) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `batch_no` varchar(15) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `medication_id` (`medication_id`),
  CONSTRAINT `medication_history_ibfk_1` FOREIGN KEY (`medication_id`) REFERENCES `medications` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medication_history`
--

LOCK TABLES `medication_history` WRITE;
/*!40000 ALTER TABLE `medication_history` DISABLE KEYS */;
INSERT INTO `medication_history` VALUES (1,4,'109','2','111','2020-06-12','JKDS90','2020-06-11 17:12:20'),(2,1,'17','31','48','2020-08-08','SDS934O','2020-06-11 17:22:24'),(3,4,'111','4','115','2020-09-10','KLSD90','2020-06-11 17:22:40');
/*!40000 ALTER TABLE `medication_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medications`
--

DROP TABLE IF EXISTS `medications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `names` varchar(50) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `available_stock` varchar(30) DEFAULT NULL,
  `unit` varchar(30) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medications`
--

LOCK TABLES `medications` WRITE;
/*!40000 ALTER TABLE `medications` DISABLE KEYS */;
INSERT INTO `medications` VALUES (1,'Hydrocynone','Ifasha mu kugabanya umuriro','42','Pieces','2020-04-28 17:24:57'),(4,'Hubeprofen','Igabanya uburibwe','94','Kemo','2020-06-10 23:42:57'),(6,'Amoxcylline','Irinda Malaria ikongera imbaraga mu mubiri','7','Item','2020-06-11 23:53:04');
/*!40000 ALTER TABLE `medications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrations`
--

DROP TABLE IF EXISTS `migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `migrations` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrations`
--

LOCK TABLES `migrations` WRITE;
/*!40000 ALTER TABLE `migrations` DISABLE KEYS */;
INSERT INTO `migrations` VALUES (1,'2014_10_12_000000_create_users_table',1),(2,'2019_08_19_000000_create_failed_jobs_table',1);
/*!40000 ALTER TABLE `migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nurses`
--

DROP TABLE IF EXISTS `nurses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nurses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `names` varchar(70) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `password` varchar(60) DEFAULT NULL,
  `delete_status` varchar(5) DEFAULT 'No',
  `delete_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nurses`
--

LOCK TABLES `nurses` WRITE;
/*!40000 ALTER TABLE `nurses` DISABLE KEYS */;
INSERT INTO `nurses` VALUES (1,'Muvunnyi Gilbert','0726183049','MTIzNDU=','No','2020-06-10 23:26:57','2020-06-10 23:26:57'),(2,'Claude Munyemana','0789456123','MTIzNDU=','No','2021-02-16 16:06:02','2021-02-16 16:06:02');
/*!40000 ALTER TABLE `nurses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `names` varchar(70) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `regno` varchar(10) NOT NULL,
  `has_insurance` varchar(10) DEFAULT NULL,
  `insurance_type` varchar(50) DEFAULT NULL,
  `insurance_number` varchar(30) DEFAULT NULL,
  `regdate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Manzi','0726183049','17rp01001','Yes','RSSB','1232423','2020-04-28 17:20:31'),(2,'Kabatesi Benitha','0783123901','17RP010902','Yes','MMI','KDFD987FG','2020-06-10 22:34:16'),(3,'Munyana Shanita','0783124573','17RP010908','Yes','Mediplan','123MS','2020-06-10 22:36:37'),(4,'Kamanda Promesse','078945434','17RP90012','Yes','Mutuelle','MK34K3','2020-06-10 22:41:45'),(5,'James Mukama','078345677','17RP01923','Yes','RSSB','SDD099','2020-06-10 23:16:17'),(6,'Kamanda Alain','0732456890','19RP5623','Yes','Britam','WE45X','2020-06-11 21:24:17'),(7,'Iradukunda Liliane','0732456890','18RP3478','Yes','Britam','KDF908','2020-06-11 21:24:41'),(8,'Musangwa','078900988','12sdl090','Yes','MMI','122JDID99','2020-06-25 15:42:51'),(9,'Musangwa','078900988','12sdl090','Yes','MMI','122JDID99','2020-06-25 15:43:43'),(10,'Musangwa','078900988','12sdl090','Yes','MMI','122JDID99','2020-06-25 15:59:17'),(11,'Grace','789545654','128GRGSD',NULL,NULL,NULL,'2020-06-25 15:59:27'),(12,'Mugwiza','789545654','128GRGSD',NULL,NULL,NULL,'2020-06-25 15:59:27'),(13,'Grace','789545654','128GRGSD',NULL,NULL,NULL,'2020-06-25 16:00:53'),(15,'Bufu Asua','07894543565','0027RP08',NULL,NULL,NULL,'2020-06-25 16:01:39'),(21,'Manzi Roger','08795454','232343',NULL,NULL,NULL,'2020-07-17 11:00:44'),(22,'Musangwa Pascal Kabierre','078923234','1234344',NULL,NULL,NULL,'2020-07-17 11:03:42'),(23,'Muneza Jayp','0789090322','6456454',NULL,NULL,NULL,'2020-07-17 11:05:02'),(24,'Roger Gasumuni','07895454','7RP08232',NULL,NULL,NULL,'2020-07-17 11:39:34'),(25,'','0726183049','',NULL,NULL,NULL,'2020-08-12 22:58:07'),(26,'MUVUNYI GIlbert','0785412365','17RP09121','Yes','MMI','m212121','2021-02-16 16:13:39');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `remember_token` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-16 16:48:27
