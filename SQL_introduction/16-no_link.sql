-- List all records where the name column is not empty, ordered by score (descending)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
