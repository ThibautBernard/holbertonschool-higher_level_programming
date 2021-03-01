-- import a database and print the max temperature of a state
SELECT state, MAX(value) as avg_temp FROM temperatures GROUP BY state ORDER BY state;
