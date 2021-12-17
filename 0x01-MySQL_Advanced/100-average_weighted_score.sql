-- Create stored procedure that compus and stores average weighted score for given student
-- Average is calculated by dividing score * weight by total weight
-- Score stored in corrections, weight stored in projects, add average to users
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
	IN user_id INT
)
BEGIN
	SET @avg:= (
		SELECT SUM(score * weight) / SUM(weight * 100) * 100
		FROM corrections
		JOIN projects
		ON corrections.project_id = projects.id
		WHERE user_id = corrections.user_id);
	UPDATE users
	SET average_score = @avg
	WHERE user_id = users.id;
END //
