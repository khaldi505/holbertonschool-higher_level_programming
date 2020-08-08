-- script that creates the MySQL server user user_0d_1.
-- with  all privileges on your MySQL server
CREATE USER IF NOT EXISTS user_0d_1@localhost
identified by "user_0d_1_pwd";
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
