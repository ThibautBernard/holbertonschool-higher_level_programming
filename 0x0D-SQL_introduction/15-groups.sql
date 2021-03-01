-- display number with the same value
SELECT score, count(score) 'number' FROM second_table GROUP BY score HAVING COUNT(score) > 0 ORDER BY score DESC;

