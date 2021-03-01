-- import a database and print average of temperature of groupe of city during july and august
-- use hbtn_0c_0;
-- source temperatures.sql;
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month >= 7 and month <= 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
