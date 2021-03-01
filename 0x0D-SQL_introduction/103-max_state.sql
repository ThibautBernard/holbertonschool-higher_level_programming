-- import a database and print the max temperature of a state
use hbtn_0c_0;
source temperatures.sql;
SELECT state, MAX(value) as avg_tmp FROM temperatures GROUP BY state ORDER BY state;
