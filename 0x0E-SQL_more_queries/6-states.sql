-- create db, databse with autoincrement
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);
