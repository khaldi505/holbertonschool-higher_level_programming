-- script that lists the number of 
-- records with the same score in the table
SELECT score, COUNT(score) as number FROM second_table GROUP BY score DESC;
