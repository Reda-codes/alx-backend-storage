-- SQL script that creates a stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
BEGIN
	DECLARE avg_score FLOAT;
	SELECT AVG(score) into avg_score from corrections where corrections.user_id = user_id;
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END //

DELIMITER ;