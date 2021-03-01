-- import a database and print average of temperature of groupe of city during july and august
SELECT city, AVG(value) as avg_tmp FROM temperatures WHERE month >= 7 and month <= 8 GROUP BY city ORDER BY avg_tmp DESC LIMIT 3;
