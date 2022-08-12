-- SQL script that creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student. 
-- Note: An average score can be a decimal 

-- DELIMITER $$

-- CREATE PROCEDURE ComputeAverageScoreForUser(
-- 	IN user_id INT)
-- BEGIN
-- 	SELECT SUM(score) / COUNT(score) from corrections WHERE user_id=user_id INTO @average;
-- 	UPDATE users SET average_score=@average 
-- 	WHERE id=user_id;
-- END; $
-- DELIMITER ;


DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	SELECT SUM(score) / COUNT(score)
	INTO @average_score
	FROM corrections
	WHERE corrections.user_id = user_id;
	UPDATE users SET average_score = @average_score
	WHERE id = user_id;
END;$$
