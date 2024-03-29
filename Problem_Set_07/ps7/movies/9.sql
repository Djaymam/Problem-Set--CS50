--write a SQL query to list the names of all people who starred in a movie released in 2004, ordered by birth year.
SELECT DISTINCT name FROM people
JOIN stars ON people.id=stars.movie_id
JOIN movies ON stars.movie_id=movies.id
WHERE year=2004 
ORDER BY people.birth ACD;