-- CREATE TABLE USERS WITH DEFAULT CONUNTRY
-- BECAUSE WITH DEFAULT IS BEST

DROP TABLE IF EXISTS `users`;
CREATE TABLE  `users` (
       `id` int NOT NULL  AUTO_INCREMENT,
       `email` varchar(255) NOT NULL UNIQUE,
       `name` varchar(255) NOT NULL,
       `country` ENUM ('US', 'CO', 'TN') DEFAULT 'US'
	   PRIMARY KEY (`id`)
);
