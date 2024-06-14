-- list all cities that can be found in the database
-- in a certain state
SELECT id, name FROM cities WHERE state_id IN
(SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
