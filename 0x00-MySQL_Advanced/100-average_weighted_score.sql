-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SELECT SUM(score * weight) / SUM(weight) 
    into avg_score FROM corrections 
    INNER JOIN projects ON corrections.project_id = projects.id 
    where corrections.user_id = user_id;
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END //

