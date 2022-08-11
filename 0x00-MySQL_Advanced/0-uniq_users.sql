-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE TABLE IF NOT EXISTS `users` (
      `id` int PRIMARY KEY AUTO_INCREMENT,
      `email` varchar(255) NOT NULL UNIQUE,
      `name` varchar(255) NOT NULL
)
