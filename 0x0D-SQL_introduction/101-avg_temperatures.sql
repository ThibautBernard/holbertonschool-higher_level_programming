-- import a database and print average of temperature of groupe of city
-- use hbtn_0c_0;
-- source temperatures.sql;
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
