-- SQL script that creates a function SafeDiv 
-- that divides (and returns) the first by the second number or returns 0 
-- if the second number is equal to 0.

DELIMITER $$

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
	DECLARE division FLOAT;
	IF b = 0 THEN
		SET division = 0;
	ELSE
		SET division = a / b;
	END IF;
	RETURN division;
END;$$
DELIMITER ;