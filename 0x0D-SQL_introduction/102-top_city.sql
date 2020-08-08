-- display top 3 by the avg of the city
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 OR month=8 GROUP BY CITY ORDER BY avg_temp DESC LIMIT 3;
