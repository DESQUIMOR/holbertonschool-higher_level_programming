-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the new database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Refresh privileges
FLUSH PRIVILEGES;
