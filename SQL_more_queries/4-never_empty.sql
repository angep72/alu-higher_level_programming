-- The script that creates the table id not null and it should not fail 
CREATE TABLE IF NOT EXISTS (
	id INT  DEFAULT 1,
	name VARCHAR(256)
	);
