-- import a database and print the max temperature of a state
-- use hbtn_0c_0;
-- source temperatures.sql;
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
