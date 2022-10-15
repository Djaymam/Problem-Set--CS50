--write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
--SELECT title FROM movies JOIN stars ON stars.movie_id=movies.id JOIN people ON people.id=stars.person_id JOIN ratings ON ratings.movie_id=movies.id WHERE stars.person_id='Chadwick Boseman' LIMIT 5 GROUP BY ratings.rating DESC ORDER BY ratings.rating ASC;
SELECT movies.title from people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
JOIN ratings on movies.id = ratings.movie_id
WHERE people.name = "Chadwick Boseman"
ORDER BY rating DESC
LIMIT 5;