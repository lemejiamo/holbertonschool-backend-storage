-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!

DROP TABLE IF EXISTS `users`;
CREATE TABLE If NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`id`)
);
