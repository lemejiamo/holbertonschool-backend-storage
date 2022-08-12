-- SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE AddBonus(
  IN user_id INT, 
  IN project_name VARCHAR(255), 
  IN score FLOAT)
BEGIN
	SELECT EXISTS(SELECT id from projects WHERE name=project_name) INTO @RESULT; 	
	
	IF @RESULT = 0 THEN
   		INSERT INTO projects (name) VALUES (project_name); 
	END IF;
  
   INSERT INTO corrections (
   		user_id,
   		project_id,
   		score) 
   	VALUES (
   		user_id,
   		(SELECT id FROM projects where name=project_name LIMIT 1),
   		score);
END; $
DELIMITER ;
