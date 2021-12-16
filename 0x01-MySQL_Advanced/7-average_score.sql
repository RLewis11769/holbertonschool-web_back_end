-- Create stored procedure that computes average score for all students for given student
-- Takes user_id input parameter
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
BEGIN
	SET @avg := (
		SELECT AVG(score)
		FROM corrections
		WHERE corrections.user_id = user_id);
	UPDATE users
	SET average_score = @avg
	WHERE id = user_id;
END $$

DELIMITER ;
