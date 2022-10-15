--write a SQL query to list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred.
--SELECT title FROM movies JOIN stars ON stars.movie_id=movies.id JOIN people ON people.id=stars.person_id WHERE people.name='Johnny Depp' AND people.name='Helena Bonham Carter

SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Johnny Depp" AND movies.title IN(
SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter");