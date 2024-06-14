-- creates a data base and a table inside it
-- cities the table contains id, state_id and name as columns
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
		PRIMARY KEY(`id`),
		id INT NOT NULL UNIQUE AUTO_INCREMENT,
		state_id INT NOT NULL,
		name VARCHAR(256) NOT NULL,
		FOREIGN KEY(`state_id`)
		REFERENCES hbtn_0d_usa.states(`id`)
);
