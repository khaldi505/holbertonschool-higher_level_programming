-- script that lists all the cities of California that can be
-- found in the database hbtn_0d_usa
SELECT cities.id, cities.name FROM cities, states
WHERE states.name = 'California'
AND states.id = cities.state_id
ORDER BY cities.id ASC;
