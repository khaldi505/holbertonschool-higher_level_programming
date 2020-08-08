-- script that creates the database
-- hbtn_0d_2 and the user user_0d_2.
create database IF not exists hbtn_0d_2;
create user if not exists user_0d_2@localhost identified by "user_0d_2_pwd";
grant SELECT on hbtn_0d_2 . * TO 'user_0d_2'@'localhost';
flush privileges;
