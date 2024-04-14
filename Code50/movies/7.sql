-- write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically by title
SELECT movies.title, ratings.rating
FROM movies, ratings
WHERE movies.year = 2010
AND ratings.movie_id = movies.id
ORDER BY rating DESC, title ASC;