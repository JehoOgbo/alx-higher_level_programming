-- Use a join to list all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, s.name
FROM cities
INNER JOIN states AS s
ON cities.`state_id` = s.id
ORDER BY cities.id;
