-- print all city from california
-- blabla
SELECT id, name FROM cities WHERE state_id=(SELECT id from states WHERE name="California") ORDER BY cities.id;
