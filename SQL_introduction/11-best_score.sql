-- Lists score, name from second_table ordered by desc score
-- Greater than or equal to 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
