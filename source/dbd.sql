/**/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`vitamin` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `vitamin`;

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `predicted` int(5) NOT NULL,
  `diseaserecomend` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`predicted`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `disease` */

insert  into `disease`(`predicted`,`diseaserecomend`) values (1,'Xerophthalmia '),(2,'anemia '),(3,'bruising, gum and dental problems, dry hair and skin, and anemia'),(4,'Osteomalacia\r\n'),(5,'Crohns disease\r\n'),(6,'cystic fibrosis\r\n'),(7,'diabetes\r\n'),(8,'chronic kidney disease\r\n'),(9,'Fungal infection\r\n'),(10,'Allergy\r\n'),(11,'GERD\r\n'),(12,'Chronic cholestasis\r\n'),(13,'Drug Reaction\r\n'),(14,'Peptic ulcer diseae\r\n'),(15,'AIDS\r\n'),(16,'Diabetes \r\n'),(17,'Gastroenteritis\r\n'),(18,'Bronchial Asthma\r\n'),(19,'Hypertension \r\n'),(20,'Migraine\r\n'),(21,'Cervical spondylosis\r\n'),(22,'Paralysis (brain hemorrhage)\r\n'),(23,'Jaundice\r\n'),(24,'Malaria\r\n'),(25,'Chicken pox\r\n'),(26,'Dengue\r\n'),(27,'Typhoid\r\n'),(28,'hepatitis A\r\n'),(29,'Hepatitis B\r\n'),(30,'Hepatitis C\r\n'),(31,'Hepatitis D\r\n'),(32,'Hepatitis E\r\n'),(33,'Alcoholic hepatitis\r\n'),(34,'Tuberculosis\r\n'),(35,'Common Cold\r\n'),(36,'Pneumonia\r\n'),(37,'Dimorphic hemmorhoids(piles)\r\n'),(38,'Heart attack\r\n'),(39,'Varicose veins\r\n'),(40,'Hypothyroidism\r\n'),(41,'Hyperthyroidism\r\n'),(42,'Hypoglycemia\r\n'),(43,'Osteoarthristis\r\n'),(44,'Arthritis\r\n'),(45,'Acne\r\n'),(46,'Urinary tract infection\r\n'),(47,'Psoriasis\r\n'),(48,'Impetigo\r\n'),(49,'Xerophthalmia \r\n'),(50,'Osteomalacia\r\n');

/*Table structure for table `food` */

DROP TABLE IF EXISTS `food`;

CREATE TABLE `food` (
  `vitamin` varchar(100) DEFAULT NULL,
  `food` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `result` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `food` */

insert  into `food`(`vitamin`,`food`,`image`,`result`) values ('vita','orange','orange.jpg','1'),('vitb','apple','apple.jpg','1');

/*Table structure for table `recomend` */

DROP TABLE IF EXISTS `recomend`;

CREATE TABLE `recomend` (
  `predicted` int(5) DEFAULT NULL,
  `recomend` varchar(1000) DEFAULT NULL,
  `image` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recomend` */

insert  into `recomend`(`predicted`,`recomend`,`image`) values (1,'Fruits and Dryfruits','fd.jpg'),(2,'Fruits and cereals and  vegetables and  millets and Dryfruits','fd.jpg'),(3,'cheese and curd and milk and meat and Dryfruits','fd.jpg'),(4,'Fruits and cereals and vegetables and millets and Dryfruits and cheese and curd and milk and meat','fd.jpg'),(5,'cereals and vegetables and millets and Dryfruits and cheese and curd and milk and meat','fd.jpg'),(6,'cereals and vegetables and millets and Dryfruits','fd.jpg');

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `register` */

insert  into `register`(`id`,`username`,`password`,`email`,`mobile`,`address`) values (1,'shan','shan','shan@gmail.com','898898989','hyderabad'),(3,'chotu','123','moulalicce225@gmail.com','+918639966858','15-8-424'),(4,'raj','raj','raj@gmail.com','8888888888','hyderabad');

/*Table structure for table `upload` */

DROP TABLE IF EXISTS `upload`;

CREATE TABLE `upload` (
  `username` varchar(100) DEFAULT NULL,
  `vita` varchar(100) DEFAULT NULL,
  `vitb` varchar(100) DEFAULT NULL,
  `vitc` varchar(100) DEFAULT NULL,
  `vitd` varchar(100) DEFAULT NULL,
  `vite` varchar(100) DEFAULT NULL,
  UNIQUE KEY `id` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `upload` */

insert  into `upload`(`username`,`vita`,`vitb`,`vitc`,`vitd`,`vite`) values ('chotu','1','0','1','0','1');


