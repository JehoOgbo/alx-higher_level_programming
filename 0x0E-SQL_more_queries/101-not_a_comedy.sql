-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows
WHERE id NOT IN (
	SELECT show_id
	FROM tv_show_genres
	WHERE genre_id IN (
		SELECT id
		FROM tv_genres
		WHERE name="Comedy"
	)
)
ORDER BY title ASC;
