-- write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
SELECT title
FROM movies
INNER JOIN ratings ON movies.id = ratings.movie_id
INNER JOIN people ON stars.person_id = people.id
INNER JOIN stars on ratings.movie_id = stars.movie_id
WHERE people.name = 'Chadwick Boseman'
ORDER BY ratings.rating DESC
LIMIT 5;


-- SELECT title
-- FROM movies
-- WHERE id IN (
--     SELECT movie_id
--     FROM ratings
--     WHERE movie_id IN (
--         SELECT movie_id
--         FROM stars
--         WHERE person_id in (
--             SELECT id
--             FROM people
--             WHERE name = 'Chadwick Boseman'
--         )
--     )
-- )
-- LIMIT 5;
