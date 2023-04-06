-- SQL script that creates a stored procedure AddBonus
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name varchar(255), IN score int)
BEGIN
		DECLARE project_id INT;
		SELECT id INTO project_id FROM projects WHERE name = project_name;
		IF project_id IS NULL THEN
			INSERT INTO projects (name) VALUES (project_name);
			SET project_id = LAST_INSERT_ID();
		END IF;
        INSERT INTO corrections (user_id, project_id, score)
        values (user_id, project_id, score);
END //

DELIMITER ;