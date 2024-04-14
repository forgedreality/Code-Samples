-- write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
SELECT m.title
FROM movies m
INNER JOIN stars s ON m.id = s.movie_id
INNER JOIN people p ON s.person_id = p.id
WHERE p.name IN ('Johnny Depp', 'Helena Bonham Carter')
GROUP BY m.title
HAVING COUNT(m.id) = 2;


-- SELECT title
-- FROM movies
-- WHERE id IN (
--     SELECT movie_id
--     FROM stars
--     WHERE person_id IN (
--         SELECT id
--         FROM people
--         WHERE name IN ('Johnny Depp', 'Helena Bonham Carter')
--     )
-- )
-- GROUP BY title;



-- INNER JOIN stars on movies.id = stars.movie_id
-- INNER JOIN people ON stars.person_id = people.id
-- WHERE people.name =
