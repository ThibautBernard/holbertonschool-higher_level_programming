-- print all city from california

SELECT id, name FROM cities WHERE state_id=(SELECT id from states WHERE name="California");
