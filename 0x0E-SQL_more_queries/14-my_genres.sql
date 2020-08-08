-- list all the generes of the show given 

SELECT tv_genres.name AS name 
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
