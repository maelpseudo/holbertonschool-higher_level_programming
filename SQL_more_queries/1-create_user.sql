-- Attempts to create the user 'user_0d_1' with the specified password if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grants all privileges to 'user_0d_1' on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Applies the changes made by the GRANT statement
FLUSH PRIVILEGES;
