-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE id NOT IN (
	SELECT show_id
	FROM tv_show_genres
	WHERE genre_id = 5
)
ORDER BY title ASC;
