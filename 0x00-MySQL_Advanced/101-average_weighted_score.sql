-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE status INT DEFAULT FALSE;
	DECLARE u_id INT;
	DECLARE av_score FLOAT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET status = TRUE;
    OPEN cur;
        ins_loop: LOOP
            FETCH cur INTO u_id;
            IF status THEN
			    LEAVE ins_loop;
		    END IF;
            SELECT SUM(score * weight) / SUM(weight) 
            into av_score FROM corrections
            INNER JOIN projects ON project_id = projects.id WHERE corrections.user_id = u_id;
            UPDATE users AS u SET average_score = av_score WHERE u.id = u_id;
        END LOOP;
    CLOSE cur;
END //

