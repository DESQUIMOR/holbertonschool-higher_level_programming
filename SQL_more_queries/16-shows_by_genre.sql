-- List all shows and all genres linked to each show, displaying NULL if no genre is linked
SELECT tv_shows.title, genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN genres ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title ASC, genres.name ASC;
