-- lists all shows that have at least one genre linked
SELECT t_s.title, g.genre_id
  FROM tv_shows AS t_s
  		INNER JOIN tv_show_genres AS g
		ON t_s.id = g.show_id
  ORDER BY t_s.title, g.genre_id;
