-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.5.8-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- public_toilet 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `public_toilet` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `public_toilet`;

-- 테이블 public_toilet.all_toilet_num 구조 내보내기
CREATE TABLE IF NOT EXISTS `all_toilet_num` (
  `location` varchar(50) NOT NULL,
  `toilet_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`location`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.auth_group 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.auth_group_permissions 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.auth_permission 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2257 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.auth_user 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.auth_user_groups 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.auth_user_user_permissions 구조 내보내기
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_buk 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_buk` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_dong 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_dong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_dongnae 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_dongnae` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_jin 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_jin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=145 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_jung 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_jung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_nam 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_nam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_saha 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_saha` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_sasang 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_sasang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_seo 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_seo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_suyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_suyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_yeongdo 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_yeongdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.busan_yeonje 구조 내보내기
CREATE TABLE IF NOT EXISTS `busan_yeonje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=144 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_boeun 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_boeun` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_cheongju 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_cheongju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=184 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_chungju 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_chungju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_danyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_danyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_eumseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_eumseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=371 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_jecheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_jecheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_jincheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_jincheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=233 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_okjcheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_okjcheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungbuk_yeongdong 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungbuk_yeongdong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=313 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_asan 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_asan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=274 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_boryeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_boryeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_buyeo 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_buyeo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=334 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_cheongyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_cheongyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_geumsan 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_geumsan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_gongju 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_gongju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_gyeryong 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_gyeryong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_nonsan 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_nonsan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_seocheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_seocheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.chungnam_seosan 구조 내보내기
CREATE TABLE IF NOT EXISTS `chungnam_seosan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daegu_buk 구조 내보내기
CREATE TABLE IF NOT EXISTS `daegu_buk` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=762 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daegu_dalseo 구조 내보내기
CREATE TABLE IF NOT EXISTS `daegu_dalseo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=477 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daegu_dalseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `daegu_dalseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=562 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daegu_jung 구조 내보내기
CREATE TABLE IF NOT EXISTS `daegu_jung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=511 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daegu_nam 구조 내보내기
CREATE TABLE IF NOT EXISTS `daegu_nam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=501 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daegu_suseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `daegu_suseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=737 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daejeon_daedeok 구조 내보내기
CREATE TABLE IF NOT EXISTS `daejeon_daedeok` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=230 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daejeon_east 구조 내보내기
CREATE TABLE IF NOT EXISTS `daejeon_east` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daejeon_west 구조 내보내기
CREATE TABLE IF NOT EXISTS `daejeon_west` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.daejeon_yuseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `daejeon_yuseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.django_admin_log 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.django_content_type 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=565 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.django_migrations 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.django_session 구조 내보내기
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_donghae 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_donghae` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_goseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_goseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_hongcheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_hongcheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=365 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_hwacheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_hwacheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_inje 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_inje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=142 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_jeongseon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_jeongseon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_pyeongchang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_pyeongchang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_wonju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_wonju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=330 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_yanggu 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_yanggu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_yangyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_yangyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gangwon_yeongwol 구조 내보내기
CREATE TABLE IF NOT EXISTS `gangwon_yeongwol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=150 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gwangju_east 구조 내보내기
CREATE TABLE IF NOT EXISTS `gwangju_east` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=209 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gwangju_gwangsan 구조 내보내기
CREATE TABLE IF NOT EXISTS `gwangju_gwangsan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gwangju_north 구조 내보내기
CREATE TABLE IF NOT EXISTS `gwangju_north` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=272 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gwangju_south 구조 내보내기
CREATE TABLE IF NOT EXISTS `gwangju_south` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gwangju_west 구조 내보내기
CREATE TABLE IF NOT EXISTS `gwangju_west` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=262 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_andong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_andong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_bonghwa 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_bonghwa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=223 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_cheongdo 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_cheongdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_chilgok 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_chilgok` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_gimcheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_gimcheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_goryeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_goryeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_gumi 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_gumi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=195 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_gunwi 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_gunwi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_gyeongju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_gyeongju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_gyeongsan 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_gyeongsan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_mungyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_mungyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=184 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_pohang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_pohang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_sangju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_sangju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=170 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_uiseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_uiseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_uljin 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_uljin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_ulleung 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_ulleung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_yecheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_yecheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_yeongcheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_yeongcheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_yeongdeok 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_yeongdeok` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongbuk_yeongyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongbuk_yeongyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=159 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_ansan 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_ansan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=464 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_anseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_anseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_anyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_anyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=192 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_bucheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_bucheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=411 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_dongducheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_dongducheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_gapyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_gapyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=194 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_gimpo 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_gimpo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_goyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_goyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1397 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_gunpo 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_gunpo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_guri 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_guri` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_gwangju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_gwangju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_gwangmyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_gwangmyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=306 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_hanam 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_hanam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_hwaseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_hwaseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_icheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_icheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_namyangju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_namyangju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_osan 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_osan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_paju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_paju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_pyeongtaek 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_pyeongtaek` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_seongnam 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_seongnam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(100) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_siheung 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_siheung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=260 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_suwon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_suwon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=224 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_uijeongbu 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_uijeongbu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_yangju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_yangju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_yangpyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_yangpyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=391 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_yeoju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_yeoju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_yeoncheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_yeoncheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeonggi_yongin 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeonggi_yongin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_changwon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_changwon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=238 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_geoje 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_geoje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_gimhae 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_gimhae` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_goseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_goseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_hadong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_hadong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=154 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_haman 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_haman` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_hamyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_hamyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_jinju 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_jinju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=450 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_miryang 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_miryang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=261 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_namhae 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_namhae` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_sacheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_sacheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_tongyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_tongyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=202 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.gyeongnam_uiryeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `gyeongnam_uiryeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_east 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_east` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_ganghwa 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_ganghwa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_gyeyang 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_gyeyang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_junggu 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_junggu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_ongjin 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_ongjin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_southeast 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_southeast` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_west 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_west` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.incheon_yeonsu 구조 내보내기
CREATE TABLE IF NOT EXISTS `incheon_yeonsu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeju_seogwipo 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeju_seogwipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=317 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_buan 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_buan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_gochang 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_gochang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_gunsan 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_gunsan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_imsil 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_imsil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_jeongeup 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_jeongeup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_jinan 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_jinan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=323 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_samwon 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_samwon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_sunchang 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_sunchang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonbuk_wanju 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonbuk_wanju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_boseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_boseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_gangjin 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_gangjin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_goheung 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_goheung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_gokseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_gokseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_gurye 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_gurye` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_haenam 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_haenam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_hampyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_hampyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_hwasun 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_hwasun` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=345 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_jangheung 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_jangheung` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_jangseong 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_jangseong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_mokpo 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_mokpo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_suncheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_suncheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_wando 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_wando` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_yeongam 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_yeongam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_yeonggwang 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_yeonggwang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.jeonnam_yeosu 구조 내보내기
CREATE TABLE IF NOT EXISTS `jeonnam_yeosu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.sejong 구조 내보내기
CREATE TABLE IF NOT EXISTS `sejong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_dobong 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_dobong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_dongjak 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_dongjak` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_eunpyeong 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_eunpyeong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=220 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_gangdong 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_gangdong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_gangnam 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_gangnam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_gangseo 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_gangseo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_geumcheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_geumcheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=108 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_guro 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_guro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_gwanak 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_gwanak` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_jongro 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_jongro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_jungnang 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_jungnang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_mapo 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_mapo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_nowon 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_nowon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=198 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_seocho 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_seocho` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_seodaemun 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_seodaemun` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_seongbuk 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_seongbuk` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_seongdong 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_seongdong` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_songpa 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_songpa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=274 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_yangcheon 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_yangcheon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_yeongdeungpo 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_yeongdeungpo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.seoul_yongsan 구조 내보내기
CREATE TABLE IF NOT EXISTS `seoul_yongsan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.ulsan_east 구조 내보내기
CREATE TABLE IF NOT EXISTS `ulsan_east` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.ulsan_north 구조 내보내기
CREATE TABLE IF NOT EXISTS `ulsan_north` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.ulsan_south 구조 내보내기
CREATE TABLE IF NOT EXISTS `ulsan_south` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

-- 테이블 public_toilet.ulsan_ulju 구조 내보내기
CREATE TABLE IF NOT EXISTS `ulsan_ulju` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `toilet_name` varchar(50) DEFAULT NULL,
  `male_female` char(1) DEFAULT NULL,
  `male_disabled_toilet_public_toiletnum` int(11) DEFAULT NULL,
  `open_time` varchar(50) DEFAULT NULL,
  `management_agency` varchar(50) DEFAULT NULL,
  `male_toilent_num` int(11) DEFAULT NULL,
  `male_disabled_urinal_num` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `land_address` varchar(100) DEFAULT NULL,
  `female_toilet_num` int(11) DEFAULT NULL,
  `sortation` varchar(50) DEFAULT NULL,
  `male_urinal_num` int(11) DEFAULT NULL,
  `longitude` float(12,7) DEFAULT NULL,
  `female_child_toilet_num` int(11) DEFAULT NULL,
  `road_address` varchar(100) DEFAULT NULL,
  `male_child_toilet_num` int(11) DEFAULT NULL,
  `male_child_urinal_num` int(11) DEFAULT NULL,
  `latitude` float(12,7) DEFAULT NULL,
  `female_disabled_toilet_num` int(11) DEFAULT NULL,
  `installation_year` varchar(50) DEFAULT NULL,
  `update_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 내보낼 데이터가 선택되어 있지 않습니다.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
