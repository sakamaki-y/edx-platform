-- MySQL dump 10.13  Distrib 5.6.30, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: edxtest
-- ------------------------------------------------------
-- Server version	5.6.30-0ubuntu0.14.04.1

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
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-07-28 05:31:09.586750'),(2,'auth','0001_initial','2016-07-28 05:31:10.000403'),(3,'admin','0001_initial','2016-07-28 05:31:10.120708'),(4,'assessment','0001_initial','2016-07-28 05:31:13.524795'),(5,'contenttypes','0002_remove_content_type_name','2016-07-28 05:31:13.683990'),(6,'auth','0002_alter_permission_name_max_length','2016-07-28 05:31:13.748168'),(7,'auth','0003_alter_user_email_max_length','2016-07-28 05:31:13.812113'),(8,'auth','0004_alter_user_username_opts','2016-07-28 05:31:13.849921'),(9,'auth','0005_alter_user_last_login_null','2016-07-28 05:31:13.909860'),(10,'auth','0006_require_contenttypes_0002','2016-07-28 05:31:13.914671'),(11,'branding','0001_initial','2016-07-28 05:31:14.100767'),(12,'bulk_email','0001_initial','2016-07-28 05:31:14.463799'),(13,'bulk_email','0002_data__load_course_email_template','2016-07-28 05:31:14.507652'),(14,'instructor_task','0001_initial','2016-07-28 05:31:14.672464'),(15,'certificates','0001_initial','2016-07-28 05:31:15.773129'),(16,'certificates','0002_data__certificatehtmlviewconfiguration_data','2016-07-28 05:31:15.794688'),(17,'certificates','0003_data__default_modes','2016-07-28 05:31:15.825172'),(18,'certificates','0004_certificategenerationhistory','2016-07-28 05:31:15.988946'),(19,'certificates','0005_auto_20151208_0801','2016-07-28 05:31:16.075249'),(20,'commerce','0001_data__add_ecommerce_service_user','2016-07-28 05:31:16.102679'),(21,'cors_csrf','0001_initial','2016-07-28 05:31:16.234211'),(22,'course_action_state','0001_initial','2016-07-28 05:31:16.560051'),(23,'course_global','0001_initial','2016-07-28 05:31:16.601198'),(24,'course_groups','0001_initial','2016-07-28 05:31:17.749359'),(25,'course_modes','0001_initial','2016-07-28 05:31:17.886397'),(26,'course_modes','0002_coursemode_expiration_datetime_is_explicit','2016-07-28 05:31:17.945130'),(27,'course_modes','0003_auto_20151113_1443','2016-07-28 05:31:17.979474'),(28,'course_modes','0004_auto_20151113_1457','2016-07-28 05:31:18.137125'),(29,'course_overviews','0001_initial','2016-07-28 05:31:18.257404'),(30,'course_overviews','0002_add_course_catalog_fields','2016-07-28 05:31:18.511410'),(31,'course_overviews','0003_courseoverviewgeneratedhistory','2016-07-28 05:31:18.549601'),(32,'course_overviews','0004_courseoverview_org','2016-07-28 05:31:18.607938'),(33,'course_overviews','0005_delete_courseoverviewgeneratedhistory','2016-07-28 05:31:18.634495'),(34,'course_structures','0001_initial','2016-07-28 05:31:18.677619'),(35,'courseware','0001_initial','2016-07-28 05:31:21.606796'),(36,'credit','0001_initial','2016-07-28 05:31:23.289985'),(37,'dark_lang','0001_initial','2016-07-28 05:31:23.503665'),(38,'dark_lang','0002_data__enable_on_install','2016-07-28 05:31:23.532040'),(39,'default','0001_initial','2016-07-28 05:31:24.145512'),(40,'default','0002_add_related_name','2016-07-28 05:31:24.354189'),(41,'default','0003_alter_email_max_length','2016-07-28 05:31:24.430755'),(42,'django_comment_common','0001_initial','2016-07-28 05:31:25.034522'),(43,'django_notify','0001_initial','2016-07-28 05:31:26.078785'),(44,'django_openid_auth','0001_initial','2016-07-28 05:31:26.410428'),(45,'edx_proctoring','0001_initial','2016-07-28 05:31:30.342877'),(46,'edxval','0001_initial','2016-07-28 05:31:32.022835'),(47,'edxval','0002_data__default_profiles','2016-07-28 05:31:32.064004'),(48,'embargo','0001_initial','2016-07-28 05:31:33.187677'),(49,'embargo','0002_data__add_countries','2016-07-28 05:31:33.645513'),(50,'external_auth','0001_initial','2016-07-28 05:31:34.290279'),(51,'ga_organization','0001_initial','2016-07-28 05:31:34.661689'),(52,'ga_contract','0001_initial','2016-07-28 05:31:36.110508'),(53,'ga_achievement','0001_initial','2016-07-28 05:31:36.484203'),(54,'ga_advanced_course','0001_initial','2016-07-28 05:31:36.794750'),(55,'ga_invitation','0001_initial','2016-07-28 05:31:38.600328'),(56,'ga_contract_operation','0001_initial','2016-07-28 05:31:40.123762'),(57,'ga_course_overviews','0001_initial','2016-07-28 05:31:40.226622'),(58,'ga_manager','0001_initial','2016-07-28 05:31:41.318197'),(59,'ga_manager','0002_data__default_manager_permission','2016-07-28 05:31:41.364797'),(60,'ga_ratelimitbackend','0001_initial','2016-07-28 05:31:41.429305'),(61,'student','0001_initial','2016-07-28 05:31:53.908949'),(62,'shoppingcart','0001_initial','2016-07-28 05:32:07.192636'),(63,'shoppingcart','0002_auto_20151208_1034','2016-07-28 05:32:09.302591'),(64,'ga_shoppingcart','0001_initial','2016-07-28 05:32:09.916742'),(65,'ga_survey','0001_initial','2016-07-28 05:32:10.556045'),(66,'ga_task','0001_initial','2016-07-28 05:32:11.182339'),(67,'lms_xblock','0001_initial','2016-07-28 05:32:11.774084'),(68,'milestones','0001_initial','2016-07-28 05:32:13.129616'),(69,'milestones','0002_data__seed_relationship_types','2016-07-28 05:32:13.185388'),(70,'mobile_api','0001_initial','2016-07-28 05:32:13.809392'),(71,'notes','0001_initial','2016-07-28 05:32:14.496845'),(72,'oauth2','0001_initial','2016-07-28 05:32:18.031978'),(73,'oauth2_provider','0001_initial','2016-07-28 05:32:18.720310'),(74,'oauth_provider','0001_initial','2016-07-28 05:32:21.285358'),(75,'organizations','0001_initial','2016-07-28 05:32:21.561036'),(76,'programs','0001_initial','2016-07-28 05:32:22.276636'),(77,'programs','0002_programsapiconfig_cache_ttl','2016-07-28 05:32:22.962472'),(78,'programs','0003_auto_20151120_1613','2016-07-28 05:32:25.790690'),(79,'self_paced','0001_initial','2016-07-28 05:32:26.534515'),(80,'sessions','0001_initial','2016-07-28 05:32:26.623053'),(81,'sites','0001_initial','2016-07-28 05:32:26.696590'),(82,'splash','0001_initial','2016-07-28 05:32:27.437447'),(83,'status','0001_initial','2016-07-28 05:32:29.081379'),(84,'student','0002_auto_20151208_1034','2016-07-28 05:32:30.548014'),(85,'submissions','0001_initial','2016-07-28 05:32:31.533990'),(86,'submissions','0002_auto_20151119_0913','2016-07-28 05:32:32.716863'),(87,'survey','0001_initial','2016-07-28 05:32:33.813403'),(88,'teams','0001_initial','2016-07-28 05:32:36.366035'),(89,'third_party_auth','0001_initial','2016-07-28 05:32:40.626493'),(90,'track','0001_initial','2016-07-28 05:32:40.703960'),(91,'user_api','0001_initial','2016-07-28 05:32:46.851104'),(92,'util','0001_initial','2016-07-28 05:32:47.698947'),(93,'util','0002_data__default_rate_limit_config','2016-07-28 05:32:47.757936'),(94,'verify_student','0001_initial','2016-07-28 05:32:57.402740'),(95,'verify_student','0002_auto_20151124_1024','2016-07-28 05:32:58.463254'),(96,'verify_student','0003_auto_20151113_1443','2016-07-28 05:33:00.481537'),(97,'wiki','0001_initial','2016-07-28 05:33:27.603156'),(98,'wiki','0002_remove_article_subscription','2016-07-28 05:33:27.669653'),(99,'workflow','0001_initial','2016-07-28 05:33:28.060023'),(100,'xblock_django','0001_initial','2016-07-28 05:33:29.183179'),(101,'contentstore','0001_initial','2016-07-28 05:33:53.035334'),(102,'course_creators','0001_initial','2016-07-28 05:33:53.139696'),(103,'ga_maintenance_cms','0001_initial','2016-07-28 05:33:53.185964'),(104,'xblock_config','0001_initial','2016-07-28 05:33:53.733115');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-28 14:33:57