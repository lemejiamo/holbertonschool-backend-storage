-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TABLE IF NOT EXISTS `users` (
      `id` INT PRIMARY KEY AUTO_INCREMENT,
      `email` VARCHAR(255) NOT NULL UNIQUE,
      `name` VARCHAR(255) NOT NULL
);
