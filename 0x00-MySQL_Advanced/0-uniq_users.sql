-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`email` varchar(255) NOT NULL UNIQUE,
	`name` varchar(255),
	PRIMARY KEY (`id`)
);
