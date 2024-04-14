-- write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.
SELECT p.name FROM people p
WHERE p.id IN
(
    SELECT s.person_id FROM stars s
    WHERE s.movie_id IN
    (
        SELECT s.movie_id FROM stars s
        WHERE s.person_id IN
        (
            SELECT p.id FROM people p
            WHERE p.name = 'Kevin Bacon'
            AND p.birth = 1958
        )
    )
)
AND p.name != 'Kevin Bacon';



-- SELECT p.name
-- FROM people p
-- INNER JOIN stars s ON movies.id = s.movie_id
-- INNER JOIN people p ON s.person_id = (
--     SELECT p.id
--     FROM people p
--     WHERE name = 'Kevin Bacon'
--     AND birth = 1958
-- );



-- SELECT m.title
-- FROM movies m
-- INNER JOIN stars s ON m.id = s.movie_id
-- INNER JOIN people p ON s.person_id = p.id
-- WHERE p.name IN ('Johnny Depp', 'Helena Bonham Carter')
-- GROUP BY m.title
-- HAVING COUNT(m.id) = 2;
