/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP TABLE IF EXISTS `metal_bands`;
CREATE TABLE `metal_bands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `band_name` varchar(255) DEFAULT NULL,
  `fans` int(11) DEFAULT NULL,
  `formed` year DEFAULT NULL,
  `origin` varchar(255) DEFAULT NULL,
  `split` year DEFAULT NULL,
  `style` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `metal_bands` (`band_name`, `fans`, `formed`, `id`, `origin`, `split`, `style`)
VALUES ('Iron Maiden', '4195', '1975', '1', 'United Kingdom', NULL, 'New wave of british heavy,Heavy'),
('Metallica', '3712', '1981', '3', 'USA', NULL, 'Heavy,Bay area thrash'),
('Megadeth', '3105', '1983', '4', 'USA', '1983', 'Thrash,Heavy,Hard rock'),
('Slayer', '2955', '1981', '6', 'USA', '1981', 'Thrash'),
('Death', '2690', '1983', '7', 'USA', '2001', 'Progressive death,Death,Progressive thrash'),
('Dream Theater', '2329', '1985', '8', 'USA', '1985', 'Progressive'),
('Black Sabbath', '2307', '1968', '9', 'United Kingdom', NULL, 'Doom,Heavy,Hard rock'),
('Nightwish', '2183', '1996', '10', 'Finland', '1996', 'Symphonic power,Gothic,Symphonic'),
('Behemoth', '1721', '1991', '21', 'Poland', NULL, 'Death,Black,Blackened death'),
('Tool', '1506', '1988', '28', 'USA', '1988', 'Progressive,Alternative'),
('Epica', '1450', '2002', '31', 'The Netherlands', NULL, 'Symphonic'),
('System Of A Down', '956', '1995', '118', 'USA', '1995', 'Alternative'),
('Within Temptation', '956', '1996', '119', 'The Netherlands', NULL, 'Symphonic,Gothic'),
('Slipknot', '928', '1995', '123', 'USA', NULL, 'Alternative,Nu'),
('AC/DC', '923', '1973', '124', 'Australia', '1973', 'Hard rock,Blues rock'),
('Apocalyptica', '656', '1993', '159', 'Finland', NULL, 'Symphonic heavy'),
('DragonForce', '607', '1999', '166', 'United Kingdom', '1999', 'Power'),
('Lacuna Coil', '604', '1994', '167', 'Italy', NULL, 'Gothic,Alternative'),
('Ghost', '547', '2008', '185', 'Sweden', NULL, 'Heavy,Psychedelic rock'),
('Guns N\' Roses', '481', '1985', '214', 'USA', '1985', 'Hard rock'),
('Alice Cooper', '362', '1964', '257', 'USA', NULL, 'Hard rock,Glam rock,New,Wave ,Heavy'),
('KISS', '352', '1972', '263', 'USA', NULL, 'Hard rock,Symphonic rock,Glam,Heavy'),
('Rage Against The Machine', '344', '1991', '266', 'USA', '1991', 'Alternative,Nu'),
('Five Finger Death Punch', '342', '2005', '268', 'USA', '2005', 'Groove metal'),
('Nine Inch Nails', '341', '1988', '270', 'USA', '1988', 'Industrial rock,Industrial'),
('Marilyn Manson', '298', '1989', '303', 'USA', NULL, 'Industrial rock,Alternative,Industrial,Glam rock,Alternative rock'),
('Godsmack', '296', '1995', '307', 'USA', NULL, 'Alternative,Hard rock'),
('Volbeat', '264', '2001', '329', 'Denmark', NULL, 'Heavy,Hard rock'),
('Mötley Crüe', '236', '1981', '367', 'USA', '2015', 'Glam rock,Glam'),
('Lordi', '195', '1992', '426', 'Finland', '1992', 'Hard rock,Glam'),
('Amberian Dawn', '158', '2006', '498', 'Finland', '2006', 'Symphonic power'),
('Blackmore\'s Night', '102', '1997', '682', 'United Kingdom', '1997', 'Folk rock'),
('Halestorm', '73', '1998', '887', 'USA', NULL, 'Hard rock'),
('Babymetal', '71', '2010', '898', 'Japan', '2010', 'J-,Pop,Melodic death'),
('Unleash The Archers', '52', '2007', '1122', 'Canada', '2007', 'Heavy,Power'),
('Hanoi Rocks', '18', '1979', '2020', 'Finland', '1979', 'Glam rock'),
('Nasty Idols', '2', '1987', '4278', 'Sweden', '1987', 'Heavy,Glam,Glam rock')
;


/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;