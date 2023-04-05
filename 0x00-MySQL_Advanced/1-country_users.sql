--  SQL script that creates a users table
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(225) NOT NULL, 
	name VARCHAR(225),
	country ENUM ('US', 'CO', 'TN') DEFAULT 'US',
	PRIMARY KEY (id),
	UNIQUE (email)
);
