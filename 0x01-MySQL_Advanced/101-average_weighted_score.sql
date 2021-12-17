-- Create stored procedure that computes and stores average weighted score for every student
-- Average is calculated by dividing score * weight by total weight
-- Score stored in corrections, weight stored in projects, add average to users
-- Can't store in variable because does all at once
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	JOIN corrections
	ON corrections.user_id = users.id
	SET average_score = (
		SELECT SUM(score * weight) / SUM(weight * 100) * 100
		FROM corrections
		JOIN projects
		ON corrections.project_id = projects.id
		WHERE users.id = corrections.user_id);
END $$
