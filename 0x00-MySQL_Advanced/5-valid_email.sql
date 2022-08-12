-- QL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.
DROP TRIGGER holberton.valid_email; 
DELIMITER $
CREATE TRIGGER `valid_email_BU` BEFORE UPDATE ON `users` FOR EACH ROW BEGIN
  IF NEW.email != OLD.email THEN
    set NEW.valid_email=0;
  END IF;
END;

DELIMITER ;