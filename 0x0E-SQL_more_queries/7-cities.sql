-- create db, table and relation with two tables iwth foreign key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id int NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, state_id int, FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE, name VARCHAR(256) NOT NULL);
