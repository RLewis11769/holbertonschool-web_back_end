-- Creates stored procedure that add new correction for given student
-- Takes inputs user_id, project_name, and score
-- Define own variable proj_id, marked as distinct from system variables with @
DELIMITER $$

CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN project_name VARCHAR(255),
	IN score INT)
BEGIN
	SET @proj_id := (
		SELECT id
		FROM projects
		WHERE name = project_name);
	IF (@proj_id IS NULL) THEN
		INSERT INTO projects (name)
		VALUES (project_name);
		SET @proj_id := LAST_INSERT_ID();
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, @proj_id, score);
END $$

DELIMITER ;
