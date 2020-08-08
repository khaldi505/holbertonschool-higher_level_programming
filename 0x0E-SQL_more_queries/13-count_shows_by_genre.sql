-- lists all genres from hbtn_0d_tv_shows
-- displays the number of shows linked to each.

SELECT tv_genres.name AS genre, COUNT(tv_genres.name)
AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY genre
ORDER BY number_of_shows DESC;
