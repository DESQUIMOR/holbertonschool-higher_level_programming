-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;

-- Use the database
USE hbtn_0e_0_usa;

-- Drop table if it exists
DROP TABLE IF EXISTS states;

-- Create the table
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert sample data
INSERT INTO states (name) VALUES
("California"),
("Arizona"),
("Texas"),
("New York"),
("Nevada");

